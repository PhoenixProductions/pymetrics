import ply.lex as lex
import ply.yacc as yacc
import os

class Parser:
 tokens = ()
 precedence = ()
 yparser = None
 fields = []
 values = []

 def __init__(self, **kw):
  self.debug = kw.get('debug',1)
  self.names = { }
  try:
   modname = os.path.split(os.path.splitext(__file__)[0])[1] + "_" + self.__class__.__name__
  except:
   modname = "parser"+"_"+self.__class__.__name__

  self.debugfile = modname + ".dbg"
  self.tabmodule = modname + "_" + "parsetab"
  lex.lex(module=self, debug=self.debug)
  self.yparser = yacc.yacc(module=self,
            debug=self.debug,
            debugfile=self.debugfile,
            tabmodule=self.tabmodule)

 def parse(self,data,debug=0):
  self.yparser.error = 0
  self.fields = []
  self.values = []
  p = self.yparser.parse(data,debug=debug)
  if self.yparser.error: 
   return None
  return p
  
 def run(self):
  while 1:
   try:
    s = raw_input('>')
   except EOFError:
    break
   if not s: continue
   print "< {}".format(self.parse(s))




