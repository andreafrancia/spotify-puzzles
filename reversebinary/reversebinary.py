# non è pythonico fare una classe che serve per contenere una funziona.
# basterebbe fare una funzione.
class ReverseBinary:
        # in python si indenta di 4 spazi 
        # in python è peccato mischiare tab e spazi, alcune cose rischi che 
        # non funzionino
	def convert(self, number):
                # io non sono in grado di leggerla
		return int(bin(int(number))[2:][::-1], 2)
