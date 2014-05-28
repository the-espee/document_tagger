import re
from pg_sample_texts import DIV_COMM, MAG_CART
 
documents = [DIV_COMM, MAG_CART]
 
 #?P<title> creates a named capturing group

 # Why the [] expression?
 # Why is (.*) in parenthesis? When do we use parenthesis and brackets?

title_search = re.compile(r'(title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
 

for i, doc in enumerate(documents):
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  translator = re.search(translator_search, doc)
  illustrator = re.search(illustrator_search, doc)
  if author: 
    author = author.group('author')
  if translator:
    translator = translator.group('translator')
  if illustrator:
    illustrator = illustrator.group('illustrator')
  print "***" * 25
  print "Here's the info for doc {}:".format(i)
  print "Title:  {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator)
  print "\n"