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
  """ command : unit
              | unit time
  """
  if len(p) == 1:
   p[0] = "INSERT INTO units {} VALUES {}".format(self.fields,self.values)
  elif len(p) == 2:
   self.fields.append('timestamp')
   self.values.append('now')
  
   p[0] = "INSERT INTO units {} VALUES {}".format(self.fields,self.values)


 def p_time(self,p):
  """ time : AT NUMBER 
  """
  print "Matched time"
  self.fields.append('timestamp')
  self.values.append(p[2])
  
 def p_unit(self,p):
  """unit  : simpleunit
           | unitwithcategory
  """
 # p[0] = p[1]

 def p_simpleunit(self,p):
  """simpleunit : WORD
                | WORD NUMBER
  """
  print "Simple unit {} i.e. 1 of".format(len(p))
  self.fields.append('item')
  self.values.append(p[1])
  if len(p) == 3:
   self.fields.append('count')
   self.values.append(p[2])
  else:
   self.fields.append('count')
   self.values.append(1)

 def p_unitwithcategory(self,p):
  """unitwithcategory : WORD WORD
                      | WORD NUMBER WORD
  """
  print "Matched unit with category {}".format(len(p))
  self.fields.append('item')  
  self.values.append(p[1])
  if len(p) == 3:
   self.fields.append('count')
   self.values.append(p[2])
   self.fields.append('unit')
   self.values.append(1)
  if len(p) == 4:
   self.fields.append('count')
   self.values.append(p[2])
   self.fields.append('unit')
   self.values.append(p[3])
   
 def p_error(self,p):
  if p:
   print "parse error %s" % p.value
  else:
   print "error at EOF"
if __name__ == '__main__':
 p = MetricsParser()
 p.run()
