import sys, re, traceback
from llef.llef import get_stressed_phones

def get_stressed_phones_for_htk(word):
	try:
		stressed_phones = get_stressed_phones(word)
	except (ValueError, TypeError):
		return '','',''

	lexiconword=word
	if lexiconword.startswith("'"): lexiconword=lexiconword[1:]
        if '/' in lexiconword: return '','',''
        if '\\' in lexiconword: return '','',''

        if 'tsh' in stressed_phones:
                #print 'Ignored because of unsupported phone: %s' % lexiconword
                return '','','';

        phones = ' '.join(stressed_phones).encode('UTF-8')
        phones = phones.replace('1','X')
        phones = phones.replace('X','')
        phones = phones.replace('i','I')
        phones = phones.replace('o','O')

	return lexiconword, word, phones

