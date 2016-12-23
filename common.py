#!/usr/bin/env python

def _tx_string(s):
	#solve the UnicodeEncodeError
	#'ascii' codec can't encode character u'\xa0'
	#usage: _tx_string(u'\xa0abc')
	if s is not None and isinstance(s, unicode):
		s = s.encode('utf-8')
	return s
