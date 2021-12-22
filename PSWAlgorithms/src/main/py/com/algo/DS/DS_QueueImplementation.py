'''
Created on Jan 28, 2020

@author: goyalpushkar
'''
#from __builtin__ import True

if __name__ == '__main__':
    pass

from DS_Queue import Queue
import random
 
def main( program ):
    if program.upper() == 'HOT_POTATO':
        mainHotPotato()
    elif program.upper() == 'PRINTER_SIMULATION':
        mainSimulation()
        
def mainHotPotato():
    symbolString = 'P'
    while symbolString.upper() != 'Q':
        symbolString = raw_input("Enter Names as comma seperated values or Q to quit: ")
        numOfPasses = raw_input("Enter Number of passes or Q to quit: ")
        if symbolString.upper() == 'Q' or numOfPasses.upper() == 'Q':
            break
        print("Entered String - " + symbolString + " :Number of Passes - " + numOfPasses)
        print( hot_potato(symbolString, numOfPasses) )
    
def mainSimulation():
    experimentRunTime = 'P'
    while experimentRunTime.upper() != 'Q':
        #num_seconds, page_per_minute, task_size, number_of_students
        experimentRunTime = raw_input("Enter experiment Run Time or Q to quit: ")
        if experimentRunTime.upper() == 'Q':
            break
        pagePerMinute = raw_input("Enter Printer speed in page/minute or Q to quit: ")
        if pagePerMinute.upper() == 'Q':
            break
        numberOfStudents = raw_input("Enter Number of Students or Q to quit: ")
        if numberOfStudents.upper() == 'Q':
            break
        maxTaskSize = raw_input("Enter Max Number of Pages in each task or Q to quit: ")
        if maxTaskSize.upper() == 'Q':
            break
        #print("Entered String - " + symbolString + " :Number of Passes - " + numOfPasses)
        
        for i in range(10):
            ( averageTime, pendingTasks ) = simulation(experimentRunTime, pagePerMinute, numberOfStudents, maxTaskSize)
            print( "Avergae wait %6.2f secs and %3d tasks remaining" % (averageTime, pendingTasks) )
            
 
##############
##Hot Potato##
##############
def hot_potato(nameListP, num):
    
    queueName = Queue()
    nameList = nameListP.split(",")
    for name in nameList:
        queueName.enqueue( name.strip() )
        
    #print( queueName.__str__() )
    while queueName.size() > 1:
        for index in range( int(num) ):
            queueName.enqueue( queueName.dequeue() )
        queueName.dequeue()
        
    return queueName.dequeue()

###################
##Printer Problem##
###################
class Printer:
    
    def __init__(self, ppm):
        self.page_rate = ppm
        #self.current_task = None  #This can be avoided if everything is based on time remaining only
        self.time_remaining = 0
    
    def get_time_remaining(self):
        return self.time_remaining
    
    def is_busy(self):
        if self.time_remaining > 0:  #self.current_task != None:
            return True
        else:
            return False

    def start_task(self, new_task):
        #self.current_task = new_task
        self.time_remaining = ( new_task.get_pages() * 60 ) / self.page_rate
        
    def tick(self):
        if self.time_remaining > 0:  #self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            #if self.time_remaining <= 0:
            #    self.current_task = None

class Task:
    
    def __init__(self, taskCreationtime, maxTaskSize):
        self.timeCr = taskCreationtime
        self.pages = random.randrange(1, int(maxTaskSize) + 1 )

    def get_time(self):
        return self.timeCr
    
    def get_pages(self):
        return self.pages
    
    def wait_time(self, current_time):
        return current_time - self.timeCr

def simulation( num_seconds, page_per_minute, number_of_students, max_task_size ):
    lab_printer = Printer( int(page_per_minute) )
    print_queue = Queue()
    wait_time = []
    
    for current_second in range( int(num_seconds) ):
        if new_print_task(number_of_students):
            newTask= Task( current_second, int(max_task_size) )
            print_queue.enqueue(newTask)
            #print( "Task Creation Time - " + str(newTask.get_time()) + " :Pages - " + str(newTask.get_pages()) )
        
        if ( not lab_printer.is_busy() ) and ( not print_queue.is_empty() ):
            nextTask = print_queue.dequeue()
            wait_time.append( nextTask.wait_time(current_second) )
            lab_printer.start_task(nextTask)
            #print( "Wait Time - " + str(nextTask.wait_time(current_second)) + " :Time Remaining - " + str(lab_printer.get_time_remaining()) )
    
        lab_printer.tick()
        #print( "Time Remaining after Tick- " + str(lab_printer.get_time_remaining()) )
    
    averageWaitTime = sum(wait_time) / len(wait_time)
    
    return ( averageWaitTime, print_queue.size() )    
        
def new_print_task(numOfStudents):
    
    taskCrSeconds = 3600 / int(numOfStudents)
    num = random.randrange(1, taskCrSeconds + 1)
    if num == taskCrSeconds:
        return True
    else:
        return False

#############
## Testing ##
#############
main("PRINTER_SIMULATION")  #PRINTER_SIMULATION #HOT_POTATO