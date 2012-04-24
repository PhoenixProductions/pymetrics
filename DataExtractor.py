import time
import os
import datetime
import shutil
import argparse
import fileinput

class DataExtractor:
  
  
  def __init__(self, file, out):
    self.datafile = file
    self.analysisdir = os.path.expanduser(out)
      
  def run(self): 
    
    print(': Starting extraction')
    if (self.datafile ==''):
      print('No file specified')
      return
    workingfilename ="{}_working".format(self.datafile)
    print("{}".format(self.datafile))
    print(": copying to working file to {}".format(workingfilename) )
    archive_data_filename = "{}_{}.log".format(self.datafile,datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    print(": archiving to{}".format(archive_data_filename))
    os.rename(self.datafile,archive_data_filename)
    try:
      shutil.copyfile(archive_data_filename, workingfilename)
    #except (Error):
    #  print("! copying over self!")
    #  return
    except (IOError):
      print("Unable to write working file")
      return
    #format of data file is
    # timestamp action/item count unit
    for line in fileinput.input(files=workingfilename):
      dataline = line.strip()  
      #print(dataline)
      components = dataline.split(' ')
      #str_timestamp = "{} {}".format(components[0], components[1])
      str_action = components[2]
      #num_count = components[3]
      #str_unit = components[4]
      #check if an "action" file exists in the analysis dir
      with open('{}/{}.log'.format(self.analysisdir, str_action),'a') as f:
        f.write("{}\n".format(dataline))
        f.close()
    #finished extracting the data file
    #delete it    
    os.remove(workingfilename)
      
    
        
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Params")
  parser.add_argument('datafile', nargs='?', help='DataFile to be processed')
  parser.add_argument('out',nargs='?',default='~/Dropbox/metrics/analysis',help='Location for analysis files')
  args = parser.parse_args()
  if args.datafile == None:
    parser.print_help()
  else:  
   de = DataExtractor(args.datafile, args.out)
   de.run()
