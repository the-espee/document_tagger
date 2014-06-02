import re
from pg_sample_texts import DIV_COMM, MAG_CART
 
documents = [DIV_COMM, MAG_CART]
 
 #?P<title> creates a named capturing group -- What are named groups?

 # Why the [] expression?
 # Why is (.*) in parenthesis? When do we use parenthesis and brackets? 
 # Why does my code work without the parenthesis in the named group?

title_search = re.compile(r'(title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
 

for document_number, document in enumerate(documents):
  title = re.search(title_search, document).group('title')
  author = re.search(author_search, document)
  translator = re.search(translator_search, document)
  illustrator = re.search(illustrator_search, document)
  if author: 
    author = author.group('author')
  if translator:
    translator = translator.group('translator')
  if illustrator:
    illustrator = illustrator.group('illustrator')

  print "***" * 25
  print "Here's the info for doc {}:".format(document_number)
  print "Title:  {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator)
  print "\n"