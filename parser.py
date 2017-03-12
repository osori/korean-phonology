import syllable

class Parser:
	def __init__(self, string):
		self.string = string
		self.listchars = list(string)
		self.syllables = []

	def tosyllables(self, string):
		for i in range(0, len(string)-1):
			wordFinal = False
			if (self.listchars[i+1] == ' '): wordFinal = True
			if (self.listchars[i] == ' '): break # avoid multiple spacing
			syllables.append(Syllable(self.listchars[i], wordFinal))

	def tostring(self, syllables):
		ret = ''
		for s in syllables:
			ret = ret + s.gethangul()
		return ret
