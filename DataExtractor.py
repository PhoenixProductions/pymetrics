import configparser
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
    self.archive = archive
      
  def run(self): 
    if not os.path.exists(self.analysisdir):
        print(": Analysis directory {} doesn't exist".format(self.analysisdir))
        return
    print(': Starting extraction')
    if (self.datafile ==''):
      print('No file specified')
      return
    workingfilename ="{}_working".format(self.datafile)
    archive_data_filename = "archive_{}.log".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
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
        
        str_outputfile = '{}.log'.format(os.path.join(self.analysisdir, str_action))
        print("Writing data to {}".format(str_outputfile))
        try:
            with open(str_outputfile,'a') as f:
                f.write("{}\n".format(dataline))
                f.close()
        except IOError as e:
            print("unable to write to log file")
            self.archive = False #skip the archiving step.
        #finished extracting the data file
        #delete it    
    print("{}".format(self.archive))    
    if self.archive:
        print(": archiving to{}".format(archive_data_filename))
        os.rename(self.datafile,archive_data_filename)
        os.remove(workingfilename)

    
        
if __name__ == '__main__':
    #load configuration 1st
    config = configparser.ConfigParser()
    config.read('config')
    
    parser = argparse.ArgumentParser(description="Params")
    #parser.add_argument('-n','--noarchive',nargs='?',default=config['DEFAULT']['ArchiveDataLog'],help='Skip archiving data', const=False)
    parser.add_argument('datafile', nargs='?', help='DataFile to be processed')
    parser.add_argument('-o', '--out',nargs='?',default=config['DEFAULT']['AnalysisLogs'],help='Location for analysis files')
    print("{}".format(config['DEFAULT']['ArchiveDataLog']))    
    args = parser.parse_args()
    if args.datafile == None:
        parser.print_help()
    else:  
        de = DataExtractor(args.datafile, args.out, config['DEFAULT']['ArchiveDataLog'])
        de.run()
