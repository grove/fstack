# Shipping-fee implementation result

Implemented the agreed behavior in **two behavior cycles**, within the maximum of four. The final public function remains `shipping_fee(order_cents, pickup=False)`. All required local checks ran, and the final full suite passed.

## Final behavior and source

```python
def shipping_fee(order_cents, pickup=False):
    if pickup or order_cents >= 5000:
        return 0
    return 500
```

Standard delivery costs 500 cents below an order value of 5000 cents and is free at 5000 cents or above. Pickup returns zero for every valid order value. The implementation adds only the condition needed for these rules. The existing test method is preserved exactly, the function's arguments and default are unchanged, and no validation was added.

## Public test boundary and independent expectations

Tests call the public `shipping_fee` function directly. Expected fees are literal values taken from the supplied requirements, not values computed from the implementation.

| Public call examples | Expected cents | Reason from the supplied contract |
| --- | ---: | --- |
| Standard orders at 0, 2500, and 4999 cents | 500 | These orders are below 5000 cents. |
| Standard orders at 5000, 5001, and 10000 cents | 0 | Free delivery starts inclusively at 5000 cents. |
| Pickup orders at 0, 2500, 4999, 5000, and 10000 cents | 0 | Pickup is always free. |
| `shipping_fee(4999, pickup=False)` | 500 | Explicit standard delivery still carries the below-threshold fee. |

The 2500-cent standard-order example is the original test. The final suite contains five test methods and twelve concrete fee assertions across ordinary and subtest cases. Both zero and the immediate threshold neighbors are represented.

## Observed baseline

Ran `python -m unittest -v` before adding tests or changing production code. The original one-test suite passed with exit code 0. The implementation at that point always returned 500.

Actual command metadata, stdout, stderr, and the original source/test files are preserved in `evidence/baseline/`.

## Cycle 1: Free standard delivery at and above 5000 cents

Added `test_standard_delivery_is_free_at_or_above_threshold`, covering 5000, 5001, and 10000 cents with an expected result of zero. Added neighboring checks for standard delivery at 0 and 4999 cents, expecting 500.

**Red command:**

```text
python -m unittest -v test_fees.ShippingFeeTests.test_standard_delivery_is_free_at_or_above_threshold
```

Against unchanged production code, the command exited 1. All three free-delivery subcases failed with `AssertionError: 0 != 500`; the run reported `Ran 1 test` and `FAILED (failures=3)`. This demonstrated the missing free-delivery behavior, not a fixture or execution error.

Changed production code to return zero when `order_cents >= 5000`, retaining the 500-cent fallback.

**Green commands:** reran the same focused command, then `python -m unittest -v`. Both exited 0. The focused test passed, and the broader suite reported `Ran 3 tests` and `OK`.

Evidence is preserved in `evidence/cycle-1-red/` and `evidence/cycle-1-green/`. The tests are identical between their red and green snapshots.

## Cycle 2: Pickup is always free

Added `test_pickup_is_always_free`, covering valid order values below, at, and above the threshold. Added a neighboring explicit `pickup=False` example at 4999 cents.

**Red command:**

```text
python -m unittest -v test_fees.ShippingFeeTests.test_pickup_is_always_free
```

Against the production code from cycle 1, the command exited 1. Pickup at 0, 2500, and 4999 cents failed with `AssertionError: 0 != 500`; the run reported `Ran 1 test` and `FAILED (failures=3)`. The below-threshold examples discriminate pickup behavior independently of free standard delivery.

Changed the existing conditional to `if pickup or order_cents >= 5000:`. No other production change was needed.

**Green commands:** reran the same focused command, then `python -m unittest -v`. Both exited 0. The focused test passed. The full suite passed all five methods.

Evidence is preserved in `evidence/cycle-2-red/` and `evidence/cycle-2-green/`. The tests are identical between their red and green snapshots.

## Final verification and evidence

The second command in `evidence/cycle-2-green/command-2.json` is the final broader verification, run against the completed candidate:

```text
python -m unittest -v
Ran 5 tests in 0.001s
OK
```

Its actual full output is retained in `evidence/cycle-2-green/stderr-2.txt`; stdout was empty and the exit code was 0. Historical failures remain intact in the red-stage directories and do not describe failures of the final candidate.

Each stage contains snapshots named `fees.py` and `test_fees.py`, command arguments and exit status in JSON, and separate unmodified stdout/stderr captures. Additional local integrity checks passed for the existing test source, public argument signature, unchanged tests across each red/green transition, production continuity between cycles, and equality of the final files with the verified final snapshots. Their results are recorded in `evidence/integrity-checks.txt`. SHA-256 hashes of the final production and test files are recorded in `evidence/final-sha256.json`.

## Limits

The tests exercise representative valid nonnegative integer orders and Boolean pickup values; they do not enumerate every integer. The implementation expresses the entire threshold rule and pickup override directly. Caller-side argument validation, invalid-input behavior, and new API requirements were outside the agreed scope and were not added or tested. There were no missing execution prerequisites. Work and evidence stayed inside this workspace and used local Python standard-library facilities.
