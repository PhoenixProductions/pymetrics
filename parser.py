import ply.lex as lex
import ply.yacc as yacc
import os

class Parser:
 tokens = ()
 precedence = ()

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
  yacc.yacc(module=self,
            debug=self.debug,
            debugfile=self.debugfile,
            tabmodule=self.tabmodule)

 def run(self):
  while 1:
   try:
    s = raw_input('>')
   except EOFError:
    break
   if not s: continue
   yacc.parse(s)



