import random

class SleepQueue:
    
    '''
    INSTANCE VARIABLES:\n
        sleepQueue : a dictionary of the form\n\t\t\t {blockNum: list of PIDs of processes waiting for this block }
        revSleepQueue : a dictionary of the form {pid : blockNum} for fast removal 
    '''
    
    def __init__(self):
    
        '''
        Constructor :  Initializes the Sleep Queue
        '''
    
        self.sleepQueue = {}
        self.revSleepQueue = {}
    
    
    def add(self, blockNum, pid):
    
        '''
        Adds the pid of the process waiting for blockNum to get free in the Sleep Queue.\n
        Give blockNum -1 to add pid of a process waiting for any Block Number to get free in the Sleep Queue.
        '''
    
        if blockNum in self.sleepQueue:
            self.sleepQueue[blockNum].append(pid)
        else:
            self.sleepQueue[blockNum] = [pid]

        self.revSleepQueue[pid] = blockNum
        print("Process",pid,": Added to the sleep queue")


    def printSQ(self):
    
        '''
        Prints the contents of the Sleep Queue.
        '''
    
        print("-----SLEEP QUEUE-----")
    
        for blockNo in self.sleepQueue:
            st = "["
            for pid in self.sleepQueue[blockNo]:
                st += str(pid) + ", "
            st += "]"
            print(blockNo, ":", st)


    def getPidsWaitingForBuffer(self,buffer): 
        
        '''
        Returns pids waiting for a specific buffer
        '''
        
        return self.sleepQueue.pop(buffer,-2)

    def getPidsWaitingForAnyBuffer(self):

        '''
        Returns pids waiting for any buffer
        '''

        return self.sleepQueue.pop(-1,-2)