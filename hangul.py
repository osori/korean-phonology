# -*- coding:utf-8 -*-

# ipa-korean
# Hangul Class

import yaml
import codecs

class Hangul:
	def __init__(self):
		f = codecs.open("hangul.yaml", "r", "utf-8")
		self.hanguldata = yaml.safe_load(f)
		f.close()

	def gethanguldata(self):
		return self.hanguldata

	def getinitials(self):
		return self.hanguldata['orthography inventory']['initial']

	def getmedials(self):
		return self.hanguldata['orthography inventory']['medial']

	def getfinals(self):
		return self.hanguldata['orthography inventory']['final']

	def getcharbycp(self, cp, imf):
		return next((k for k, v in self.hanguldata['codepoint'][imf].items() if v == cp), None)

	def getcpbychar(self, char, imf):
		return self.hanguldata['codepoint'][imf][char]

	def getipa(self, char, imf):
		# in the case of null onset(e.g. 안), return an empty string
		if (imf == 'i' and char == 'ㅇ'):
			return ''

		return self.hanguldata['ipa'][char]

	# returns true if a given hangul character is a consonant
	def isconsonant(self, char):
		return True if (char in self.hanguldata['phonemic inventory']['consonants']) else False

	# returns true if a given hangul character is a vowel
	def isvowel(self, char):
		return True if (char in self.hanguldata['phonemic inventory']['vowels']) else False

	def getallophone(self, char, imf):
		if char == '': return char
		if char not in self.hanguldata['allophonic inventory'][imf]: return char
		allophone = self.hanguldata['allophonic inventory'][imf][char]
		return allophone

	def sfnlexception_getallophone(self, char, imf):
		return self.hanguldata['allophonic inventory'][imf]['exceptions'][char]