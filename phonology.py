# ipa-korean
# Phonology class

from syllable import Syllable
import hangul
import kparser

h=hangul.Hangul()
parser = kparser.Parser()

class Phonology:

	def __init__(self, string):
		# self.parse=kparser.Parser()
		self.string =string
		print('Original String:\t' + string)
		self.syllables = parser.tosyllables(string)
		pass

#잎이 -> 이피
	def pronounce(self):
		psyllables = self.resyllabify(self.syllables)
		psyllables = self.final_neutralize(psyllables)
		return psyllables

	# Must precede Syllable Final Neutralization Rule
	# e.g. 눈이 -> 누니
	def resyllabify(self, syllables):
		for i in range(0, len(syllables)):
			s1 = syllables[i]
			try:
				s2 = syllables[i+1]
			except IndexError:
				s2 = Syllable('')

			if (s1.f != '' and s2.i == 'ㅇ'):
				s2.seti(s1.f)
				s1.setf('')

		return syllables

	# Syllable Final Neutralization Rule
 	# e.g. 앞 aph -> 압 ap
	def final_neutralize(self,syllables):
		ret = ''
		for i in range(0, len(syllables)):
			s1 = syllables[i]
			try:
				s2 = syllables[i+1]
			except IndexError:
				s2 = Syllable('')

			if (s1.iswordfinal or h.isconsonant(s2.i)):

				#TODO: ‘밟-’은 자음 앞에서 [밥]으로 발음하고, ‘넓-’은 다음과 같은 경우에 [넙]으로 발음한다. 
				### EXCEPTION CHECK
				if (s1.f == 'ㄼ' and h.isconsonant(s2.i)):
					allophone = h.sfnlexception_getallophone(s1.f, 'final')
				else:
					allophone = h.getallophone(s1.f, 'final')
				s1.setf(allophone)

	def h_aspirationalize(self, syllables):
		

		return syllables


#
#	def toipa(self, string):
#		ipa = ''
#		for c in string:
#			if (Syllable(c).)
#			ipa = ipa + Syllable(c).getipa()
#		return ipa