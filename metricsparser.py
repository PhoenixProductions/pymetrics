import ply.lex as lex
import ply.yacc as yacc
import datetime as dt
import time
import os
##import Parser

class MetricsParser():
 def __init__(self, **kw):
  self.debug = kw.get('debug',0)
  self.names = { }
  self.write = 1
  
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
  self.write = 1;
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
    #   print("< {}".format(self.parse(s)))
        result = self.parse(s)
        if result == None:
           print("Didn't understand that!")
        else:
            pass                    
                         
 tokens = (
  'WORD', 'AT', 'NUMBER', 'CMD'
 )

# t_FLOAT   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'

 t_NUMBER = r'\d+'
 t_WORD = r'[a-zA-Z_]+'
 t_AT = r'@'
 t_CMD = r'![a-zA-Z]+'
 def t_newline(self,t):
  r'\n+'

 def t_error(self,t):
   t.lexer.skip(1)

 def p_command(self,p):
  """ command : unit
              | unit timestamp 
  """
  
  if len(p) == 1:
      pass
  elif len(p) == 2:
     self.values['timestamp'] = dt.datetime.now()
     p[0] = "{}".format(p[1])
  else:
    p[0] = "{} {}".format(p[1],p[2])

  if self.write == 1:
      with open('data','a') as f:
        line = "{} {} {} {}\n".format(self.values['timestamp'],self.values['item'],self.values['count'],self.values['unit'])
        f.write(line)
        f.close()
      #print("{}".format(p[0]))
    
      
 def p_timestamp(self,p):
    """ timestamp : AT NUMBER
    """
    #print("time  i.e. at ? {}".format(len(p)))
#   Calculate the timestamp from the implied format
    lp = len(p)
    if lp == 3:
        # at time
        timev = time.strptime(p[2],"%H%M")
        #print("{}".format(timev))
        td = dt.datetime.combine(dt.datetime.now(), dt.time(timev[3],timev[4]))
        p[0] = "@ {}".format(td)
        
        self.values['timestamp'] = td
        
    
 def p_unit(self,p):
  """unit  : CMD
           | simpleunit
           | unitwithcategory
  """
  if len(p) == 2:
        self.write = 0
        p[0] = 'Command'
        print('Command Detected')
        if p[1] == '!l':
            with open('data','r') as f:
                for line in f:
                    print("{}".format(line))
                f.close()
      
  else:
          p[0] = p[1]

 def p_simpleunit(self,p):
  """simpleunit : WORD
                | WORD NUMBER
  """
  self.values['item'] = p[1]
  if len(p) == 3:
    self.values['count'] = p[2]
    p[0] = "{} {}".format(p[1],p[2])
  else:
    self.values['count'] = 1
    p[0] = "{} {}".format(1,p[1])

 def p_unitwithcategory(self,p):
  """unitwithcategory : WORD WORD
                      | WORD NUMBER WORD
  """
  #print("Matched unit with category {}".format(len(p)))
  self.values['item'] = p[1]
  if len(p) == 3:
      self.values['count'] = 1
      self.values['unit'] = p[2]
      p[0] = "{} {}".format(p[1],p[2])
  if len(p) == 4:
      self.values['count'] = p[2]
      self.values['unit'] = p[3]
      p[0] = "{} {} {}".format(p[1],p[2],p[3])
  else:
      pass
#      p[0] = "{}".format(p[1])
      
 def p_error(self,p):
  if p:
      pass
      #print("parse error {}".format(p.value))
  else:
      pass
      #print ("error at EOF")


if __name__ == '__main__':
    p = MetricsParser()
    p.run()
