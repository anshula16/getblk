import os, signal, random
from Buffer import Buffer

def brelse(buffer, bufferHead, lock, sleepQueue):

    '''
    Implementation of BRELSE algorithm.
    Buffer is released after kernel on behalf of the process finishes using it.
    '''

    lock.acquire()
    
    blockNo = buffer.getBlockNum();
    
    if buffer==None:
        print("\nUnexpected behaviour")
        return

    if bufferHead.checkValidBit(blockNo):
        print("Adding at the end")
        bufferHead.addToFreeList(buffer, False)
    else:
        print("Adding at the front")
        bufferHead.addToFreeList(buffer, True)

    bufferHead.clearLockedBit(buffer.getBlockNum())
    print("Process",os.getpid(),": Unlocked buffer ",buffer.getBlockNum(),"            Lock status:",buffer.getLockedStatus())
    bufferHead.printFreeList()
    
    wakeAllProcessWaitingForBuffer(sleepQueue,buffer)
    wakeAllProcessWaitingForAnyBuffer(sleepQueue)
    
    lock.release()



def wakeAllProcessWaitingForBuffer(sleepQueue,buffer):
    #-2 is returned when no such entry for buffer in sleepQueue
    list=sleepQueue.getPidsWaitingForBuffer(buffer.getBlockNum())
    if(list==-2):
        return
    for pid in list:
        os.kill(pid,signal.SIGINT)


def wakeAllProcessWaitingForAnyBuffer(sleepQueue):
    #-2 is returned when no such entry for buffer in sleepQueue
    list=sleepQueue.getPidsWaitingForAnyBuffer()
    if(list==-2):
        return
    for pid in list:
        os.kill(pid,signal.SIGHUP)

