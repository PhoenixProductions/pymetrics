import time
import os
import datetime

class DataExtractor:
  def __init__(self, **kw):
    self.debug = kw.get('debug',0)
    
  def run(self): 
    print('� Starting extraction')
        
if __name__ == '__main__':
    de = DataExtractor()
    de.run()
