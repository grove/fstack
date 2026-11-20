"""Exercise packaging integrity and evaluator/worker separation."""
from copy import deepcopy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from common import (MAX_BYTES, catalog, frontmatter, load_json, package_files,
                    read_bytes, validate_case, write_bundle)
from export import export
from prepare_eval import prepare
from render import render
from validate import validate

SKILL = '''---
name: fstack-example-method
description: "Investigate a bounded question. Use when an observation needs explanation."
---

# Example method

## Starting point

Read the question and supplied records.

## Method

1. State the claim.
2. Inspect the relevant records.

## What to return

Return the supported claim and the observations that support it.

## Boundaries

Do not invent missing execution or change external systems.

## Worked example

An unavailable log leaves the cause unresolved.
'''


class ToolChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT.parent)
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'library'
        self.skill = self.repo / 'skills/fstack-example-method'
        self.skill.mkdir(parents=True)
        (self.skill / 'SKILL.md').write_text(SKILL)
        (self.repo / 'LICENSE').write_text('Example license bytes.\n')
        self.index = {'version':'1.0.0','skills':[{'name':'fstack-example-method','group':'understanding','purpose':'Investigate a bounded question.'}]}
        (self.repo / 'catalog.json').write_text(json.dumps(self.index))
        (self.repo / 'evals/cases').mkdir(parents=True)
        self.case = {
            'id':'fstack-example-method','skill':'fstack-example-method',
            'task':'Investigate the reported missing result. Do not modify source.',
            'context':'A supplied log reports a timeout. No live service is available.',
            'expected':['GRADER-ONLY-EXPECTED-SENTINEL'],
            'forbidden':['GRADER-ONLY-FORBIDDEN-SENTINEL'],
            'evidence':['GRADER-ONLY-EVIDENCE-SENTINEL'], 'mode':'reasoning'}
        self.case_path = self.repo / 'evals/cases/fstack-example-method.json'
        self.case_path.write_text(json.dumps(self.case))

    def test_export_contains_only_selected_complete_package_and_license(self):
        output = self.base / 'export'
        self.assertEqual(1, export(output, root=self.repo))
        package = output / 'fstack-example-method'
        self.assertEqual({'SKILL.md','LICENSE'}, {p.name for p in package.iterdir()})
        self.assertEqual(SKILL,(package/'SKILL.md').read_text())
        self.assertEqual((self.repo/'LICENSE').read_bytes(),(package/'LICENSE').read_bytes())
        self.assertFalse((output/'catalog.json').exists())

    def test_export_carries_referenced_local_resources(self):
        (self.skill/'references').mkdir()
        (self.skill/'references/example.txt').write_text('Required example data.')
        (self.skill/'SKILL.md').write_text(SKILL+'\nRead [example](references/example.txt).\n')
        output = self.base/'export'
        export(output,root=self.repo)
        self.assertEqual('Required example data.',(output/'fstack-example-method/references/example.txt').read_text())

    def test_export_rejects_broken_or_external_local_dependency(self):
        (self.skill/'SKILL.md').write_text(SKILL+'\nRead [global protocol](../../protocol.md).\n')
        with self.assertRaisesRegex(ValueError,'non-contained'):
            export(self.base/'export',root=self.repo)
        self.assertFalse((self.base/'export').exists())

    def test_nonempty_destination_is_preserved(self):
        output=self.base/'export';output.mkdir()
        (output/'user.txt').write_text('Keep this.')
        with self.assertRaisesRegex(ValueError,'empty directory'):
            export(output,root=self.repo)
        self.assertEqual('Keep this.',(output/'user.txt').read_text())

    def test_empty_destination_is_supported(self):
        output=self.base/'export';output.mkdir()
        self.assertEqual(1,export(output,root=self.repo))

    def test_duplicate_or_unknown_selection_fails_before_writes(self):
        for selected in [[],['fstack-example-method']*2,['fstack-unknown']]:
            with self.subTest(selected=selected),self.assertRaises(ValueError):
                export(self.base/'export',selected,root=self.repo)
            self.assertFalse((self.base/'export').exists())

    def test_export_refuses_source_directory_destinations(self):
        for directory in ('skills', 'docs', 'examples', '.github', '.git'):
            with self.subTest(directory=directory),self.assertRaisesRegex(ValueError,'overlap'):
                export(self.repo/directory/'new-copy',root=self.repo)

    @unittest.skipUnless(hasattr(os,'symlink'),'Symbolic links unavailable')
    def test_package_symlink_is_not_copied(self):
        outside=self.base/'outside.txt';outside.write_text('outside')
        (self.skill/'linked.txt').symlink_to(outside)
        with self.assertRaisesRegex(ValueError,'Symbolic-link'):
            export(self.base/'export',root=self.repo)

    @unittest.skipUnless(hasattr(os,'symlink'),'Symbolic links unavailable')
    def test_output_symlink_is_not_followed(self):
        destination=self.base/'real';destination.mkdir()
        alias=self.base/'alias';alias.symlink_to(destination,target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'symbolic links'):
            export(alias,root=self.repo)
        self.assertEqual([],list(destination.iterdir()))

    def test_failed_bundle_does_not_leave_partial_output(self):
        output=self.base/'export'
        with self.assertRaises(OSError):
            write_bundle(output,{'conflict':b'a','conflict/file.txt':b'b'},root=self.repo)
        self.assertFalse(output.exists())
        self.assertEqual([],list(self.base.glob('.fstack-stage-*')))

    def test_render_preserves_task_as_data_and_handles_backticks(self):
        task='Read this supplied text: ```embedded``` and do not send it.'
        result=render('fstack-example-method',task,root=self.repo)
        self.assertIn(SKILL,result)
        self.assertIn('````text',result)
        self.assertIn(task,result)
        self.assertIn('does not grant additional permissions',result)

    def test_render_rejects_unknown_skill_or_empty_task(self):
        with self.assertRaisesRegex(ValueError,'Unknown skill'):
            render('fstack-unknown','task',root=self.repo)
        with self.assertRaisesRegex(ValueError,'empty'):
            render('fstack-example-method','   ',root=self.repo)

    def test_prepared_packet_omits_every_grader_field(self):
        output=self.base/'packet'
        prepare('fstack-example-method',output,root=self.repo)
        contents='\n'.join(p.read_text() for p in output.rglob('*') if p.is_file())
        self.assertIn(self.case['task'],contents)
        self.assertIn(self.case['context'],contents)
        self.assertNotIn('GRADER-ONLY-',contents)
        self.assertTrue((output/'skill/SKILL.md').is_file())
        self.assertTrue((output/'skill/LICENSE').is_file())
        self.assertFalse(any(p.suffix=='.json' for p in output.rglob('*')))

    def test_workspace_case_materializes_only_supplied_fixtures(self):
        case=deepcopy(self.case)
        case.update(mode='workspace',fixtures=[{'path':'src/example.py','content':'answer = 7\n'}])
        self.case_path.write_text(json.dumps(case))
        output=self.base/'packet'
        prepare('fstack-example-method',output,root=self.repo)
        self.assertEqual('answer = 7\n',(output/'workspace/src/example.py').read_text())
        self.assertFalse((output/'workspace/.keep').exists())

    def test_fixture_traversal_absolute_and_metadata_paths_are_rejected(self):
        for path in ['../escape','/absolute','C:\\escape','safe/../../escape','.git/config','a//b','a/./b']:
            case=deepcopy(self.case)
            case.update(mode='workspace',fixtures=[{'path':path,'content':'content'}])
            with self.subTest(path=path),self.assertRaises(ValueError):
                validate_case(case,catalog(self.repo))

    def test_fixture_collisions_are_rejected(self):
        for paths in [('A.txt','a.txt'),('a','a/b')]:
            case=deepcopy(self.case)
            case.update(mode='workspace',fixtures=[{'path':p,'content':'data'} for p in paths])
            with self.subTest(paths=paths),self.assertRaisesRegex(ValueError,'collision|colliding'):
                validate_case(case,catalog(self.repo))

    def test_mode_and_rubric_integrity_are_checked(self):
        changes=[{'mode':'workspace'},{'mode':'other'},{'expected':[]},{'evidence':[False]},
                 {'forbidden':['same','same']},{'skill':'fstack-unknown'},{'unknown':'value'}]
        for change in changes:
            with self.subTest(change=change),self.assertRaises(ValueError):
                validate_case({**self.case,**change},catalog(self.repo))

    def test_frontmatter_is_valid_scalar_yaml_not_an_ambiguous_type(self):
        for value in ['false','[one, two]','bad: scalar']:
            with self.subTest(value=value),self.assertRaises(ValueError):
                frontmatter('---\nname: fstack-example-method\ndescription: '+value+'\n---\n')
        self.assertEqual('fstack-example-method',frontmatter(SKILL)['name'])

    def test_duplicate_json_keys_and_nonstandard_constants_fail(self):
        path=self.base/'bad.json'
        for text in ['{"status":"failed","status":"passed"}','{"metric":NaN}']:
            path.write_text(text)
            with self.subTest(text=text),self.assertRaises(ValueError):
                load_json(path)

    @unittest.skipUnless(hasattr(os,'mkfifo'),'FIFO unavailable')
    def test_nonregular_input_cannot_hang_the_reader(self):
        path=self.base/'fifo';os.mkfifo(path)
        with self.assertRaisesRegex(ValueError,'regular file'):
            read_bytes(path)

    def test_input_size_is_bounded(self):
        path=self.base/'large'
        with path.open('wb') as stream:stream.truncate(MAX_BYTES+1)
        with self.assertRaisesRegex(ValueError,'exceeds'):
            read_bytes(path)

    def test_catalog_duplicate_and_mismatched_names_fail(self):
        self.index['skills'].append(deepcopy(self.index['skills'][0]))
        (self.repo/'catalog.json').write_text(json.dumps(self.index))
        with self.assertRaisesRegex(ValueError,'Duplicate skill'):
            catalog(self.repo)

    def test_repository_is_consistent(self):
        errors,counts=validate(ROOT)
        self.assertEqual([],errors)
        self.assertEqual(counts['skills'],counts['cases'])


if __name__=='__main__':
    unittest.main()
