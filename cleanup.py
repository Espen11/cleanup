#!/usr/bin/env python 

import os, time, sys
from optparse import OptionParser

##################################################

def find_files(path,days):
	now = time.time()
	file_list = []
	tot_size = 0
	for root, sub_folders, files in os.walk(path):
		for file in files:
			f = os.path.join(root,file)
			if os.stat(f).st_mtime < now - days * 86400:
				tot_size = tot_size + os.path.getsize(f)
				file_list.append(f)

	print ''
	print 'Found %i files to delete' % (len(file_list))
	print 'Totaling %iGB in size' % (tot_size/1024/1024/1024)

	return file_list

def delete_files(file_list):
	ans = raw_input('\nType y to continue: ')
	if ans == 'y':
		for file in file_list:
			if os.path.isfile(file):
				os.remove(file)
	else:
		print 'Exiting'
		return

##################################################

if __name__ == '__main__':
	usage = "Usage: %prog [options]"
	parser = OptionParser(usage=usage)
	parser.add_option('-p', '--path', dest='path', help='dir to clean', metavar='path')
	parser.add_option('-d', '--days', dest='days', help='delete files older that x days', metavar='days')

	(options, args) = parser.parse_args()


	if options.path:
		if options.days:
			files = find_files(options.path,int(options.days))
			delete_files(files)
		else:
			files = find_files(options.path,7)
			delete_files(files)

