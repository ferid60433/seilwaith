import sys, re, traceback
from llef.llef import get_stressed_phones
import get_stressed_phones_for_htk

seen = set()
f = sys.stdin

for word in f.read().decode('UTF-8').strip().split('\n'):

	if re.search(ur'\d', word): continue
	if word.lower() in seen: continue
	seen.add(word.lower())

	lexiconword, word, phones = get_stressed_phones_for_htk.get_stressed_phones_for_htk(word)
	if (len(lexiconword)>0):
		print ("{0:30}{1:30}{2:30}".format(lexiconword.upper().encode('UTF-8'), '[' + word.upper().encode('UTF-8') + ']', phones))
