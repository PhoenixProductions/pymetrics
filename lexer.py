import ply.lex as lex
import ply.yacc as yacc

#This has to handle the grammar for adding
#<item>
#<item> <count>
#<item> <count> at <time>
#<item> at <time>
class Lexer:

 tokens= (
  'ITEM',
  'NUMBER',
  'AT'
 )


 t_ITEM = r'[a-zA-Z]+\w'
 t_AT = r'\wAT\w'

 def t_NUMBER(self,t):
  r'\d+'
  t.value = float(t.value)
  return t
 
 def t_error(self,t):
   print "Illegal character %s" % t.value[0]
   t.lexer.skip(1)


 def build(self,**kwargs):
  self.lexer = lex.lex(module=self, **kwargs)

 def test(self,data):
  self.lexer.input(data)
  while True:
   tok = self.lexer.token()
   if not tok: break
   print tok
  
m = Lexer()
m.build()
m.test("something at 1000")
