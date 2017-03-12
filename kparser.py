from syllable import Syllable

DEFAULT = object()

class Parser:
	def __init__(self):
		self.string = ''
		self.listchars = list()
		self.syllables = []

	def tosyllables(self, string):
		self.string = string;
		self.listchars = list (string)
		print (len(self.string))
		for i in range(0, len(self.string)):
			wordFinal = False
			if (i != len(self.string)-1 and self.listchars[i+1] == ' '): wordFinal = True
			if (len(self.string) == 1): 
				wordFinal = True
				print("Only one-letter")
			if (self.listchars[i] != ' '): # avoid spacing
				self.syllables.append(Syllable(self.listchars[i], wordFinal))

		return self.syllables

	def tostring(self, syllables):
		self.syllables = syllables
		ret = ''
		for s in self.syllables:
			ret = ret + s.gethangul()
			if(s.iswordfinal):
				ret = ret + ' '
		return ret

	def toipa(self, syllables):
		self.syllables = syllables
		ipa = ''
		for c in self.syllables:
			ipa = ipa + c.getipa()
			if (c.iswordfinal):
				ipa = ipa + ' '
		return ipa