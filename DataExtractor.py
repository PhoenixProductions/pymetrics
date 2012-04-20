import time
import os
import datetime

class DataExtractor:
  def __init__(self, **kw):
    self.debug = kw.get('debug',0)
    
  def run(self): 
    print('õ Starting extraction')
        
if __name__ == '__main__':
    de = DataExtractor()
    de.run()
