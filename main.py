from syllable import Syllable
import hangul
from phonology import Phonology
from kparser import Parser

#c = Syllable('ㄴ','ㅏ')
c2 = Syllable('난')
h = hangul.Hangul()

#print(c2.getimf())
#print(h.getinitials())
parser = Parser()
teststr ="넋 모르다"
p = Phonology(teststr)
print('Actual Realization:\t' + parser.tostring(p.pronounce()))
print('IPA Transcription:\t' + parser.toipa(p.pronounce()))