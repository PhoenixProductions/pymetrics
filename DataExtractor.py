import time
import os
import datetime
import shutil
import argparse
import fileinput

class DataExtractor:
  
  
  def __init__(self, file, out, archive=False):
    self.datafile = file
    self.analysisdir = os.path.expanduser(out)
      
  def run(self): 
    
    print(': Starting extraction')
    if (self.datafile ==''):
      print('No file specified')
      return
    workingfilename ="{}_working".format(self.datafile)
    archive_data_filename = "{}_{}.log".format(self.datafile,datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    print("{}".format(self.datafile))
    print(": copying to working file to {}".format(workingfilename) )
    try:
        shutil.copyfile(self.datafile, workingfilename)
    except (Error):
        print("! copying over self!")
        return
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
        
        str_outputfile = '{}/{}.log'.format(self.analysisdir, str_action)
        try:
            with open(str_outputfile,'a+') as f:
                f.write("{}\n".format(dataline))
                f.close()
        except IOError as e:
            with open(str_outputfile,'w') as f:
                f.write("{}\n".format(dataline))
                f.close()
        #finished extracting the data file
        #delete it    

    if archive is True:
        print(": archiving to{}".format(archive_data_filename))
        os.rename(self.datafile,archive_data_filename)
        os.remove(workingfilename)

    
        
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Params")
  parser.add_argument('-n','--noarchive',nargs='?',default=False,help='Skip archiving data', const=False)
  parser.add_argument('datafile', nargs='?', help='DataFile to be processed')
  parser.add_argument('-o', '--out',nargs='?',default='analysis/',help='Location for analysis files')

  args = parser.parse_args()
  if args.datafile == None:
    parser.print_help()
  else:  
   de = DataExtractor(args.datafile, args.out, args.noarchive)
   de.run()
