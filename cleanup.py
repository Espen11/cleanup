#!/usr/bin/env python 

import os, time, sys
from optparse import OptionParser

def clean(path):
#	path = '/var/nfs-backup'
	now = time.time()
	for f in os.listdir(path):
		f = os.path.join(path,f)
		if os.stat(f).st_mtime < now - 7 * 86400:
			print f
			continue
	#		if os.path.isfile(f):
	#			os.remove(os.path.join(path, f))



if __name__ == '__main__':
	usage = "Usage: %prog [options]"
	parser = OptionParser(usage=usage)
	parser.add_option('-p', '--path', dest='path', help='dir to clean', metavar='path')

	(options, args) = parser.parse_args()

	if options.deploy:
		clean(options.path)

