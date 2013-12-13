import unittest
from reversebinary import ReverseBinary

class TestCase(unittest.TestCase):
	def setUp(self):
		self.reverseBinary = ReverseBinary()

	def testConversion(self):
                # puoi usare self.assertEquals(x,y) al posto di assert
		assert self.reverseBinary.convert(1) == 1
		assert self.reverseBinary.convert(13) == 11
		assert self.reverseBinary.convert(47) == 61
		assert self.reverseBinary.convert(1000000000) == 1365623

if __name__ == "__main__":
        # python2.7 non ti serve più questa cosa, non mi ricordo bene, mi
        # sembra che basti avviare da linea di comando:
        # 
        #   python -m unittest
        # 
        # in ogni caso io uso python "nose"
	unittest.main();
