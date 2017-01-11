import datetime
import os
import time

from threading import Thread
from smarthome_server import LogHolder

class LogPrinter(Thread):
    def run(self):
        print("Initializing printer...")
        myLogger = LogHolder.Singleton.get()
        todaysDate = datetime.date.today()      #Check the days date each time it's printing (in case of sudden date-switching)

        while True:
            if (todaysDate == datetime.date.today()):       #Checks if it's still the same date as it was 15seconds ago
                print("FROM LOGGER: Still the same date.")  #If it is, it proceeds as normal
            else:
                todaysDate = datetime.date.today()          #If it's not, change the date to the new date & look for old logs
                print("FROM LOGGER: Proceeding with clearing old logs...")
                self.clean_old_logs()

            filepath = "./logs/" + str(todaysDate) + ".txt" #Set the filepath to the correct folder + todays date

            if(myLogger.get_length_of_printlist() > 0):     #Look if there are anything to log, if not do nothing else, start logging
                if (os.path.exists(filepath) is True):      #If the file already exists, add the text from the LogHandler to it.
                    myLogger.set_printer_status(True)       #Set the loggers status to busy.
                    with open(filepath, mode='a', encoding='utf-8') as myfile:
                        myfile.write('\n'.join(myLogger.get_list_to_print()))
                        myfile.write('\n')
                        print("Printed.")
                else:                                       #If the file does not exist, create a new file with the text from the LogHandler in it..
                    myLogger.set_printer_status(True)       #Set the loggers status to busy.
                    with open(filepath, mode='w', encoding='utf-8') as myfile:
                        myfile.write('\n'.join(myLogger.get_list_to_print()))
                        myfile.write('\n')
                        print("Printed.")

                myLogger.merge_lists()                      #When finished with this iteration, merge the lists
                myLogger.set_printer_status(False)          #Set the logger to status free

            time.sleep(15)                                  #Sleep for x seconds until the next time to log

    def clean_old_logs(self):
        deletedFilesCount = 0

        for dirpath, dirnames, filenames in os.walk("./logs/"):     #Look iterative through the folders/files on this path
            for file in filenames:
                curpath = os.path.join(dirpath, file)
                file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))  #The date that the file was created

                if datetime.datetime.now() - file_modified > datetime.timedelta(days=7):    #Checks if the file is now older than 7 days
                    os.remove(curpath)      #If it is, remove it
                    deletedFilesCount += 1
        #print("Deleted " + str(deletedFilesCount) + " files.")
