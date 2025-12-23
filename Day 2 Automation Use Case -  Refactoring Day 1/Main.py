import os
import datetime

class Logger:
    _LEVELS = {"INFO":1, "WARNING":2, "ERROR":3}
    
    def __init__(self, file_path, _log_level ):
        self._file_path = file_path
        self._level_num = 0         # Order matters as setter sets level num before itself if below property call 
        self.log_level = _log_level #triggers Python’s descriptor protocol.
    
        # Checking File Presence 
        if os.path.exists(self._file_path) == True:
            pass
        else:
            raise FileNotFoundError("File Not Found")

    @property # Property Getter - No Args Taken
    def log_level(self):
        return self._log_level

    @log_level.setter #Setter - Take one value and acts on it
    def log_level(self, value):
        if not isinstance(value, str):
            raise TypeError("Entered Level is Not Accepted !!")
        self._log_level = str(value).upper()  
    
        # Checking Log Value
        try:
            self._level_num = self._LEVELS[self._log_level]
        except KeyError: raise ValueError(f"Invalid Log Value : {self._log_level}")

    @staticmethod
    def _format_entry(message,level):
        return(
                f"\nMessage Logged : '{message}' at [{datetime.datetime.now()}]\n"
               f"Log Level of Message: {level}\n"
        )

    def log(self, message, message_level):
        if not isinstance(message_level, str):
            raise TypeError("Message Level is not of Accepted Type")
        message_level = str(message_level).upper()
        message_level_num = 0

        # Checking Message Level Value
        if message_level in self._LEVELS.keys():
            message_level_num = self._LEVELS[message_level]
        else: 
            raise ValueError("Invalid Value")
        
        # Boundary Parameters for level value
        if message_level_num >= self._level_num:
            entry = self._format_entry(message, message_level)
            with open(self._file_path, "a") as log_mode:
                log_mode.write(entry)
            
    def read_logs(self):
        # Reads Logs line by line and make a list and displays it 
        with open(self._file_path,"r") as read_log_mode:
            Lines = read_log_mode.readlines()
        return Lines

    def clear_logs(self):
        # Clears the file 
        with open(self._file_path,"w") as clear_mode:
            clear_mode.seek(0)
            clear_mode.truncate()


        

Logger_Test_Obj = Logger(r"C:\Users\ramaa\OneDrive\Documents\Python Mini Projects\Automation-Orchestrator-v1-\Day 1 Automation Use Case - Configurable File Logger Service\TestFile.txt", "INFO")

Logger_Test_Obj.clear_logs()

Logger_Test_Obj.log("Automation started", "INFO")
Logger_Test_Obj.log("API rate limit nearing", "WARNING")
Logger_Test_Obj.log("API authentication failed", "ERROR")

X = Logger_Test_Obj.read_logs()
for i in X:
    print(i)

        
    