import os
import datetime

class Logger:
    Levels = {"INFO":1, "WARNING":2, "ERROR":3}
    
    def __init__(self, file_path, log_level):
        self.file_path = file_path
        self.log_level = str(log_level).upper()
        self.lev_num = 0
    
        # Checking File Presence 
        if os.path.exists(self.file_path) == True:
            pass
        else:
            raise FileNotFoundError("File Not Found")

        # Checking Log Value
        try:
            self.lev_num = self.Levels[self.log_level]
        except KeyError: raise Exception("Invalid Log Value")
        
    def log(self, message, message_level):
        message_level = str(message_level).upper()
        message_level_num = 0
        # Checking Message Level Value
        try:
            message_level_num = self.Levels[message_level]
        except KeyError: raise Exception("Inavlid Message Log Value")
        
        # Boundary Parameters for level value
        if message_level_num >= self.lev_num:
            with open(self.file_path, "a") as log_mode:
                log_mode.write(f"\nMessage Logged : '{message}' at [{datetime.datetime.now()}]\nLog Level of Message: {message_level}\n")
            
    def read_logs(self):
        # Reads Logs line by line and make a list and displays it 
        with open(self.file_path,"r") as read_log_mode:
            Lines = read_log_mode.readlines()
        return Lines

    def clear_logs(self):
        # Clears the file 
        with open(self.file_path,"w") as clear_mode:
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

        
    