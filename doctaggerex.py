import os
import sys
import re

# The user supplies the directory in the command line where docs are held
directory = sys.argv[1] #Why do we use "1" here?
# 1 is an index. sys.argv holds all the stuff you typed in the console
# so index 0 is just going to be the original command
# if you typed "./script.py arg1 arg2"
# then sys.argv[0] would be "./script.py" which is not very useful for you
# yes only the first argument is used if you specify this way

# shell automatically replaces relative links with full ones
# "C:\My Documents"
# Specify keywords in command line

# ./doc_tagger.py directory bim bam bop
# sys.argv[2:] will be ["bim", "bam", "bop"]
# first time, keyword will be "bim"
# so in the keywords dict, keywords["bim"] = re.compile..etc
keywords = {}
for keyword in sys.argv[2:]: # Why "2:" ?
	keywords[keyword] = re.compile(r'\b' + keyword +r'\b', re.IGNORECASE)
# first time around keyword is "bim", seconf time "bam" etc...
title_search = re.compile(r'(title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# Find and iterate throguh all files in the directory
for file_name in (os.listdir(directory)):
	if file_name.endswith('.txt'):
		file_name_path = os.path.join(directory, file_name)
        # if you have a directory named "C:\stuff"
        # and a file name inside of it called "junk.txt"
        # then joining them gives you "C:\stuff\junk.txt"
		with open(file_name_path, 'r') as f:
			full_text = f.read()

		title = re.search(title_search, full_text)
		if title:
			title = title.group('title')
		if author:
			author = author.group('author')
		translator = re.search(translator_search, full_text)
		if translator:
			translator = translator.group('translator')
		illustrator = re.search(illustrator_search, full_text)
		if illustrator:
			illustrator = illustrator.group('illustrator')

		print '***' * 25
		print "Here's the info for {}:".format(file_name)
		print "Title: {}".format(title)
		print "Author(s): {}".format(author)
		print "Translator(s): {}".format(translator)
		print "Illustrator(s): {}".format(illustrator)

		print "\n\n\n"
		print "Keyword Report:"

		for keyword in keywords:
			print "'{0}:{1}".format(
				keyword, 
				len(re.findall(keywords[keyword], fulltext))
				)
			print "\n"
			break