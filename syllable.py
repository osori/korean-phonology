# Korean
# Syllable class

from hangul import Hangul

DEFAULT = object()
h = Hangul()

# Syllable consists of an initial, a medial, an optional final.
class Syllable:

#	def __init__(self, initial, medial, final=DEFAULT):
#		self.setimf(initial, medial, final) #initial medial final

	def __init__(self, syllable, wordfinal=True):
		if (syllable == ''): return
		self.i = self.divide(syllable)[0]
		self.m = self.divide(syllable)[1]
		self.f = self.divide(syllable)[2]
		self.setimf(self.i, self.m, self.f)
		self.iswordfinal = wordfinal

	def __str__(self):
		return h.getcpbychar(i, 'initial') * 588 + h.getcpbychar(m, 'medial') * 21 + h.getcpbychar(f, 'final')


	def setimf(self, initial, medial, final=DEFAULT):
		# Validate
		if (initial not in h.getinitials() 
			or medial not in h.getmedials() ):
			print("initial: " + initial + ' medial: ' + medial)
			raise ValueError()

		if final is DEFAULT:
			self.imf = [initial, medial, '']
		else:
			self.imf = [initial, medial, final]

	def getimf(self):
		# returns the list of initial, medial, and final
		return self.imf

	def getlen(self):
		# returns the number of characters in the syllable
		return 2 if len(self.imf) == 2 else 3

	def divide(self, syllable):
		cp = ord(syllable) - 44032
		init = h.getcharbycp (cp // 588, 'initial')
		med = h.getcharbycp (cp % 588 // 28, 'medial')
		fin = h.getcharbycp (cp % 588 % 28, 'final')
		return [init, med, fin]

	def alterimf(self, lstsyllable, imfnum, alterchar):
		lstsyllable[imfnum] = alterchar
		return lstsyllable

	def i(self):
		return self.getimf()[0]

	def m(self):
		return self.getimf()[1]

	def f(self):
		return self.getimf()[2]

	def seti(self, init):
		self.i = init;

	def setm(self, med):
		self.m = med;

	def setf(self, fin):
		self.f = fin;

	def gethangul(self):
		return chr(44032+(h.getcpbychar(self.i, 'initial') * 588 + h.getcpbychar(self.m, 'medial') * 28 + h.getcpbychar(self.f, 'final')))

	def getipa(self):
		return h.getipa(self.i, 'i') + h.getipa(self.m, 'm') + (h.getipa(self.f, 'f') if self.f != '' else '')


