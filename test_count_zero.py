import unittest
from src.count_zero_marco import conta_zeros


teste_1 = 1
teste_2 = 6
teste_3 = 0
teste_4 = 2
teste_5 = 5


class Tester(unittest.TestCase):
    
    def test_conta_zeros(self):
        self.assertEqual(conta_zeros('aiudhsauihda-0'), teste_1)
        self.assertEqual(conta_zeros('suahdiua000ahduhsuidh0000jasdoisj000000'), teste_2)
        self.assertEqual(conta_zeros('pizza'), teste_3)
        self.assertEqual(conta_zeros('asudhaiusdh00 hdiaushdasu0dh'), teste_4)
        self.assertEqual(conta_zeros('aushdiauh0dfsdfsd0s0sdfsdf00sdfdffd000dfsdfdfs000hththr0000egtrhrthr00000'), teste_5)
        pass


if __name__ == '__main__':

    unittest.main()
