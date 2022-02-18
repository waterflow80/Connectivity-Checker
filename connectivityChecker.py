from tkinter import * #for GUI
import os #for system commands
import time #for sleep

class ConnectionTester:
    def __init__(self):
        window = Tk()
        window.title("Connection Tester")
        # window.iconbitmap("/home/haroune/programs/Icon_tools_and_star.png")
        #window.geometry("400x400")



        
        #Title 
        Label(window, text="Test Domain Connectivity", bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=1,column=1,sticky=N)
        Label(window, text=None).grid(row=2, column=1)
        Label(window, text=None).grid(row=3, column=1)
        Label(window, text="Processing Time ", bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=7,column=1, sticky=W)
        Label(window, text=None).grid(row=5, column=1)
        Label(window, text=None).grid(row=6, column=1)
        Label(window, text="Domain Name", bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=4,column=1, sticky=W)
        Label(window, text=None).grid(row=8, column=1)
        Label(window, text=None).grid(row=9, column=1)
        Label(window, text="Connectivity State", bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=10,column=1, sticky=W)
        Label(window, text=None).grid(row=10, column=1)
        Label(window, text=None).grid(row=11, column=1)
        Label(window, text="N° Packets Sent", bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=12,column=1, sticky=W)
        Label(window, text=None).grid(row=13, column=1)
        Label(window, text="N° Packets Received", bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=14,column=1, sticky=W)
        
        
        #Domain Name
      
        # Label(window, text="-----------------------").grid(row=1,column=1,sticky=N)
        
        
        #Variables to store input
        self.domainName = StringVar()
        self.result = StringVar(window, value="Connectivity")
        self.clearButtonState = StringVar(window, value="Clear")
        self.submiButtonState = StringVar(window, value="Check Connectivity")
        self.processingTime = IntVar()
        self.processingTime.set(5)
        self.nbPacketsSent = StringVar(window, value="")
        self.nbPacketsReceived = StringVar(window, value="")
        

        
        #Input
        Entry(window, textvariable=self.domainName,bg="light gray",
              justify=CENTER).grid(row=4, column=2, padx = (0,5))
        
        Entry(window, textvariable=self.processingTime,bg="light gray",
              justify=CENTER).grid(row=7, column=2, padx = (0,5))
        
        #Result Output
        # Entry(window, textvariable=self.nbPacketsSent,bg="light gray",
        #       justify=CENTER).grid(row=12, column=2, padx = (0,5))
        
        Label(window, textvariable=self.nbPacketsSent, bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=12,column=2, sticky=N)
        Label(window, textvariable=self.nbPacketsReceived, bg="light gray", bd=1, relief="sunken",font=("Helvetica",22)).grid(row=14,column=2, sticky=N)
        # Entry(window, textvariable=self.nbPacketsReceived,bg="light gray",
        #       justify=CENTER).grid(row=14, column=2, padx = (0,5))
        
        Label(window, textvariable=self.result, bg="light gray",bd=1,
              font="Helvetica 12 bold", justify=CENTER).grid(row=10, column=2, sticky=N)
        
        #Actions
        #Submit
        Button(window, textvariable=self.submiButtonState,
               command=self.checkConnectivity,
               font="Helvetica 14").grid(row=17,column=2, padx= (100,5), pady=5)
        #clear
        Button(window, textvariable=self.clearButtonState,
               command=self.clear,
               font="Helvetica 14").grid(row=18,column=2, padx= (100,5), pady=5)
        
        #Bind the Enter Key to Call the event
        window.bind('<Return>',self.checkConnectivityEnter)
    
        
        window.mainloop()
        
        
    def clear(self):
        self.nbPacketsReceived.set("")
        self.nbPacketsSent.set("")
        self.domainName.set("") 
        
    def checkConnectivity(self):
        timeToWait = self.processingTime.get() #The time given for the system to execute the command and get a result
        
        waitCommand = "-w " + str(timeToWait) + " " #Specify the time taken pinging before exiting the terminal
        
        dommainName = self.domainName.get() #The domain name enterd by the user
            
        cmd = "ping " + waitCommand + dommainName #Adding the domain name to the ping command
            
        path_of_the_ping_result_file = "/your_path/ping/ping.txt/ping/ping.txt"
            
        redirectResult = "> " + path_of_the_ping_result_file #To put the result in a text file so we can parse it later
            
        fullCommand = cmd + redirectResult #Full command to be executed
        
        emptying_file_command = "echo " " " + redirectResult #Setting the file to empty ''
            
        os.system(fullCommand) #Executing the ping command with the domain name
            
        nb_packets_received = "" #Stores the number of packets received
            
        lineList = "" #Stores the words of the line containing the packets information
            
        with open(path_of_the_ping_result_file, "r") as f:
            allLines = f.readlines() #Saving the content of the file
            for line in allLines:
                if "transmitted" in line:
                    lineList = line.split()
                    break; 
            for iter in range(len(lineList)):
                if str(lineList[iter]) == 'received,':
                    nb_packets_received = lineList[iter - 1]
                    break    
        if (nb_packets_received > '0'):
            self.result.set("WELL CONNECTED :)")
        else:
            self.result.set("NOT CONNECTED :(")    
    
    
    '''
    Executes the operation when Enter Keyword is pressed
    '''
    def checkConnectivityEnter(self,event):
        timeToWait = self.processingTime.get() #The time given for the system to execute the command and get a result
        
        waitCommand = "-w " + str(timeToWait) + " " #Specify the time taken pinging before exiting the terminal
        
        dommainName = self.domainName.get() #The domain name enterd by the user
            
        cmd = "ping " + waitCommand + dommainName #Adding the domain name to the ping command
            
        path_of_the_ping_result_file = "/your_path/ping/ping.txt"
            
        redirectResult = "> " + path_of_the_ping_result_file #To put the result in a text file so we can parse it later
            
        fullCommand = cmd + redirectResult #Full command to be executed
        
        emptying_file_command = "echo " " " + redirectResult #Setting the file to empty ''
            
        os.system(fullCommand) #Executing the ping command with the domain name
            
        nb_packets_received = "0" #Stores the number of packets received
        
        nb_packets_sent = "0"
            
        lineList = "" #Stores the words of the line containing the packets information
            
        with open(path_of_the_ping_result_file, "r") as f:
            allLines = f.readlines() #Saving the content of the file
            for line in allLines:
                if "transmitted" in line:
                    lineList = line.split()
                    break;
            for iter in range(len(lineList)):
                if str(lineList[iter]) == 'transmitted,':
                    nb_packets_sent = lineList[iter - 2]
                if str(lineList[iter]) == 'received,':
                    nb_packets_received = lineList[iter - 1]
                    break   
        if (nb_packets_received > '0'):
            self.nbPacketsReceived.set(nb_packets_received)
            self.nbPacketsSent.set(nb_packets_sent)
            self.result.set("WELL CONNECTED")
        else:
            self.nbPacketsReceived.set(nb_packets_received)
            self.nbPacketsSent.set(nb_packets_sent)
            self.result.set("NOT CONNECTED")    
    
        
            
        
ConnectionTester()
