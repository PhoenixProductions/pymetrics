from parser import Parser

class MetricsParser(Parser):
 tokens = (
  'WORD', 'AT', 'NUMBER', 'FLOAT', 'COLON'
 )

 t_FLOAT   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
 t_NUMBER = r'\d+' 
 t_COLON = r':'

 def t_WORD(self,t):
  r'\W+'
  print 'matched word'
 
 def t_newline(self,t):
  r'\n+'

 def t_error(self,t):
  t.lexer.skip(1)

 def p_command(self,p):
  '''command : 
             | action'''
  print "Command " 
  print p[0]
 
 def p_action(self,p):
  '''action : WORD'''
  l = len(p)
  if l == 1:
   print 'simply unit'
  elif l == 2:
   print 'quantified unit'
  else:
   print 'unknown command'

 
# def p_time(p):
#  '''time : NUMBER COLON NUMBER'''
#  print "time"
#  print p

 def p_error(self,p):
  if p:
   print "parse error %s", p.value
  else:
   print "error at EOF"
if __name__ == '__main__':
 p = MetricsParser()
 p.run()
