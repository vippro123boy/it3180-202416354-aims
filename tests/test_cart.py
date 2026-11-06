import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_digital_video_disc(DigitalVideoDisc(f"DVD {i}")))
        # Đĩa thứ 21 phải bị từ chối
        self.assertFalse(cart.add_digital_video_disc(DigitalVideoDisc("DVD 21")))

if __name__ == "__main__":
    unittest.main()