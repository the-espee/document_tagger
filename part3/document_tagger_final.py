import sys
import os
import re

title_pattern = re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + 
                          r'((\n(\ )+)(\S*(\ )?)*)*)', 
                          re.IGNORECASE)
author_pattern = re.compile(r'(author:)(?P<author>.*)', 
    re.IGNORECASE)
translator_pattern = re.compile(r'(translator:)(?P<translator>.*)', 
    re.IGNORECASE)
illustrator_pattern = re.compile(r'(illustrator:)(?P<illustrator>.*)', 
    re.IGNORECASE)
 
meta_search_dict = dict(author=author_pattern, #Why am I putting these in the dictionary? Do these come
 					title=title_pattern, # from the above search criteria? I thought dictionaries had curly brackets and key value pairs were done with a colon?
 					translator=translator_pattern,
 					illustrator=illustrator_pattern)

def meta_search(meta_search_dict, text):
 	"""Returns results of search for metadata from text"""
 	results = {}
 	for keyword in meta_search_dict:
 		result = re.search(meta_search_dict[keyword], text)
 		if result:
 			results[keyword] = results.group(k)
 		else:
 			results[k] = None
 	return results

def file_opener(fl_path):
 	"""Given a full path to a file, opens that file and returns it's contents"""
 	with open(fl_path, 'r') as f:
 		return f.read()

def file_path_maker (directory, fl_name):
 	return os.path.join(directory, fl_name)

def keyword_pattern_maker(keywords):
 	"""Returns dictionary of keyword regular expression patterns"""
 	result = {keyword: re.compile(r'\b' + keyword + r'\b') for keyword in keywords}
 	return result

def keyword_counter(pattern, text):
 	"""Returns the number of matches for a keyword in a given text"""
 	matches = re.findall(pattern, text)
 	return len(matches)

def doc_tag_reporter(directory, keywords):
 	"""
 	Iterates over a directory of Project Gutenberg documents and gives
 	info on title, suthor, illustrator, and count of user supplied keywords
 	"""
 	for fl in os.listdir(directory):
 		if fl.endswith('.txt'):
 			fl_path = file_path_maker(directory, fl)
 			text = file_opener(fl_path)
 			meta_searches = meta_search(meta_search_dict, text)
 			keyword_searches = keyword_pattern_maker(keywords)
 			print "Here's the info for {}:".format(fl)
 			for k in meta_searches:
 				print "\"{0}\": {1}".format(k.capitalize(), meta_searches[k])
 				print "\n****KEYWORD REPORT\n\n"
 				for kw in keyword_searches:
 					print "\"{0}: {1}".format(kewyord, keyword_counter,keyword_searches[keyword], text)
 					print '\n\n'
 					print "***" * 25

def main():
	directory = sys.argv[1]
	keywords = [i for i in sys.argv[2:]]
	doc_tag_reporter(directory, keywords)

if __name__ == '__main__':  #What is a main function and what does it do?
	main()
 