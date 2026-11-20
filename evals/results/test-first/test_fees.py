import unittest
from fees import shipping_fee


class ShippingFeeTests(unittest.TestCase):
    def test_standard_small_order(self):
        self.assertEqual(500, shipping_fee(2500))


    def test_standard_delivery_below_threshold_boundaries(self):
        for order_cents in (0, 4999):
            with self.subTest(order_cents=order_cents):
                self.assertEqual(500, shipping_fee(order_cents))

    def test_standard_delivery_is_free_at_or_above_threshold(self):
        for order_cents in (5000, 5001, 10000):
            with self.subTest(order_cents=order_cents):
                self.assertEqual(0, shipping_fee(order_cents))


    def test_pickup_is_always_free(self):
        for order_cents in (0, 2500, 4999, 5000, 10000):
            with self.subTest(order_cents=order_cents):
                self.assertEqual(0, shipping_fee(order_cents, pickup=True))

    def test_explicit_standard_delivery_preserves_fee(self):
        self.assertEqual(500, shipping_fee(4999, pickup=False))


if __name__ == "__main__":
    unittest.main()
