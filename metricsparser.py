from parser import Parser

class MetricsParser(Parser):
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
  print "Illegal Character '%s'" % t.value[0]
  t.lexer.skip(1)

 def p_command(self,p):
  """ command : action
              | action time
  """
  lp = len(p)


 def p_time(self,p):
  """ time : AT NUMBER 
  """
  print "Matched time"
  
 def p_action(self,p):
  """action  : simpleaction
             | actionwithcategory
  """
  print "Matched action {}".format(len(p))

 def p_simpleaction(self,p):
  """simpleaction : WORD
  """
  print "Simple action {}".format(len(p))

 def p_actionwithcategory(self,p):
  """actionwithcategory : WORD WORD
  """
  print "Matched actionwith category {}".format(len(p))

 
 def p_error(self,p):
  if p:
   print "parse error %s" % p.value
  else:
   print "error at EOF"
if __name__ == '__main__':
 p = MetricsParser()
 p.run()
