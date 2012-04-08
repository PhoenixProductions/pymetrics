from datetime import *
from buzhug import Base
import re
#using http://buzhug.sourceforge.net/

 
def create_db():
 print "Creating entries db"
 try:
  entries = Base('entries.db').create(('name',str),('value',float),('timestamp',datetime))
  categories = Base('categories.db').create(('name',str))
  entry_cats = Base('entry_categories.db').create(('entry',entries),('category',categories))
 except(IOError):
  print ""  

def parse_input(input):
 entries = Base('entries.db').open()

 print 'parsing ' + input

 #search for <name> at <time>
 re_at_time = re.compile('(.+) at ([0-9:]+)', re.IGNORECASE)
 m = re_at_time.match(input)
 if (m):
  print 'Matched ? at ?'
  print m.group(1)
  print m.group(2)
  ts = new datetime.today()
  entries.insert(name=input,timestamp=ts)

 else:
  entries.insert(name=input,timestamp=datetime.now())

def ask_for_metric():
 while True:
  response = raw_input('>')
  if response in ('!q','!quit'):
   print 'quitting'
   return
  if response in('!l','!list'):
   show_items()
  else: 
   parse_input(response) 

def show_items():
 entries = Base('entries.db').open()
 ar_entries = entries.select()
 for entry in ar_entries:
  print entry.name  +":"+ entry.timestamp.strftime("%A %d. %b %Y %H:%M")

# check if we have a metrics database first
create_db()	
entries = Base('entries.db').open()
categories = Base('categories.db').open()
entry_cats = Base('entry_categories.db').open()

ask_for_metric()

