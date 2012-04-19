import ply.lex as lex
import ply.yacc as yacc
import datetime as dt
import os
##import Parser

class MetricsParser():
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
  self.values = dict({'item':'','unit':'','count':0,'timestamp':0})
  p = self.yparser.parse(data,debug=debug)
  if self.yparser.error: 
   return None
  return p
  
 def run(self):
  while 1:
   try:
    s = input('>')
   except EOFError:
    break
   if not s: continue
   print("< {}".format(self.parse(s)))
                         
 tokens = (
  'WORD', 'AT', 'NUMBER', 'FLOAT', 'COLON', 'SPACE'
 )

 t_FLOAT   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
 t_NUMBER = r'\d+' 
 t_COLON = r':'
 t_WORD = r'[a-zA-Z_]+'
 t_AT = r'at|AT|aT|At'
 
# def t_WORD(self,t):
#  r'\W+'
 
 def t_newline(self,t):
  r'\n+'

 def t_error(self,t):
  print("Illegal Character '{}' ".format(t.value[0]))
  t.lexer.skip(1)

 def p_command(self,p):
  """ command : unit
              | unit time
  """
  
  if len(p) == 1:
      pass
  elif len(p) == 2:
    self.values['timestamp'] = dt.datetime.now()
  p[0] = "Added item"
  with open('data','a') as f:
    line = "{} {} {} {}\n".format(self.values['timestamp'],self.values['item'],self.values['count'],self.values['unit'])
    f.write(line)
    f.close()
  print(p[0])

 def p_time(self,p):
     """ time : AT NUMBER
     """
     print("time  i.e. at ? {}".format(len(p)))
     self.values['timestamp'] = p[2]
     p[0] = p[2]
           
 def p_unit(self,p):
  """unit  : simpleunit
           | unitwithcategory
  """
 # p[0] = p[1]

 def p_simpleunit(self,p):
  """simpleunit : WORD
                | WORD NUMBER
  """
  print("Simple unit {} i.e. 1 of".format(len(p)))
  self.values['item'] = p[1]
  if len(p) == 3:
    self.values['count'] = p[2]
  else:
    self.values['count'] = 1

 def p_unitwithcategory(self,p):
  """unitwithcategory : WORD WORD
                      | WORD NUMBER WORD
  """
  print("Matched unit with category {}".format(len(p)))
  self.values['item'] = p[1]
  if len(p) == 3:
      self.values['count'] = 1
      self.values['unit'] = p[2]
  if len(p) == 4:
      self.values['count'] = p[2]
      self.values['unit'] = p[3]
   
 def p_error(self,p):
  if p:
      print("parse error {}".format(p.value))
  else:
      print ("error at EOF")


if __name__ == '__main__':
    p = MetricsParser()
    p.run()
