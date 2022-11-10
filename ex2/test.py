import unittest
from ex2 import RubbleWallet, DollarWallet, EuroWallet



class TestWallet(unittest.TestCase):

    def test_add(self):
        self.assertEqual(RubbleWallet("X", 10) + 20, RubbleWallet("X", 30))

    def test_iadd(self):
        wallet_to_test = RubbleWallet("X", 10) 
        wallet_to_test += 20 
        self.assertEqual(wallet_to_test, RubbleWallet("X", 30))

    def test_radd(self):
        self.assertEqual(20 + RubbleWallet("X", 10), RubbleWallet("X", 30))

    def test_add_dollar_to_ruble(self):
        self.assertEqual(RubbleWallet("X", 20) + DollarWallet("D", 10), RubbleWallet("X", 620))

    def test_add_ruble_to_dollar(self):
        self.assertEqual(DollarWallet("D", 2) + RubbleWallet("X", 60), DollarWallet("D", 3))

    def test_iadd_ruble_to_dollar(self):
        wallet_to_test = DollarWallet("D", 2)
        wallet_to_test += RubbleWallet("X", 60)
        self.assertEqual(wallet_to_test,  DollarWallet("D", 3))




    def test_sub(self):
        self.assertEqual(RubbleWallet("X", 50) - 20, RubbleWallet("X", 30))

    def test_isub(self):
        wallet_to_test = RubbleWallet("X", 50) 
        wallet_to_test -= 20 
        self.assertEqual(wallet_to_test, RubbleWallet("X", 30))

    def test_rsub(self):
        self.assertEqual(20 - RubbleWallet("X", 15), RubbleWallet("X", 5))

    def test_sub_dollar_from_ruble(self):
        self.assertEqual(RubbleWallet("X", 620) - DollarWallet("D", 10), RubbleWallet("X", 20))

    def test_sub_ruble_from_dollar(self):
        self.assertEqual(DollarWallet("D", 2) - RubbleWallet("X", 60), DollarWallet("D", 1))

    def test_isub_ruble_from_dollar(self):
        wallet_to_test = DollarWallet("D", 2)
        wallet_to_test -= RubbleWallet("X", 60)
        self.assertEqual(wallet_to_test,  DollarWallet("D", 1))






    def test_mul(self):
        self.assertEqual(RubbleWallet("X", 10) * 20, RubbleWallet("X", 200))

    def test_imul(self):
        wallet_to_test = RubbleWallet("X", 10)
        wallet_to_test *= 20
        self.assertEqual(wallet_to_test, RubbleWallet("X", 200))

    def test_rmul(self):
        self.assertEqual(20 * RubbleWallet("X", 10), RubbleWallet("X", 200))



    def test_div(self):
        self.assertEqual(RubbleWallet("X", 200) / 20, RubbleWallet("X", 10))

    def test_idiv(self):
        wallet_to_test = RubbleWallet("X", 200)
        wallet_to_test /= 20
        self.assertEqual(wallet_to_test, RubbleWallet("X", 10))




    def test_eq(self):
        self.assertEqual(DollarWallet("A", 15), DollarWallet("B", 15))

    def test_spend_all(self):
        wallet_to_test = RubbleWallet("X", 100)
        wallet_to_test.spend_all()
        self.assertEqual(wallet_to_test.get_amount(), 0)

    def test_to_base(self):
        self.assertEqual(DollarWallet("X", 1).to_base(), 60)

    def test_str(self):
        self.assertEqual(str(DollarWallet("Q", 150)), 'Dollar Wallet Q 150')





def main():
    unittest.main()


if __name__ == "__main__":
    main()