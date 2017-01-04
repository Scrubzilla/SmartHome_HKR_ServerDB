class Singleton(object):
    instance = None
    printerIsBusy = False
    textToPrint = []            #Used to store all of the text that shall be printed by the logger in the next 30sec period
    textOnHold = []             #A temporary list that holds all of the text that was commanded to be printed while the logger was busy

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    #Adds text to list of prints.
    def add_text_to_log(self, text):
        if(self.printerIsBusy is False):
            self.textToPrint.append(text)
        else:
            self.textOnHold.append(text)

    #Used when the logger have just finished writing to get the requests that was made while the logger was busy to the main list.
    def merge_lists(self):
        self.textToPrint = self.textOnHold
        self.textOnHold.clear()

    #Used to set the loggers status to busy/free
    def set_printer_status(self, status):
        self.printerIsBusy = status

    #Used to get the list of things that shall be printed
    def get_list_to_print(self):
        return self.textToPrint

    # Used to get the length of the list of things that shall be printed
    def get_length_of_printlist(self):
        return len(self.textToPrint)