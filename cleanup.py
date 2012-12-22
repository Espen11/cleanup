#!/usr/bin/env python 

import os, time, sys

path = '/var/nfs-backup'
now = time.time()
for f in os.listdir(path):
	f = os.path.join(path,f)
	if os.stat(f).st_mtime < now - 7 * 86400:
		print f
		continue
#		if os.path.isfile(f):
#			os.remove(os.path.join(path, f))

