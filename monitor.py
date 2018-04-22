from fileProtector import watcher
import psutil, sys, time, os, threading, datetime, tempfile

flag = True
while flag:
    interval = raw_input('Please Enter The Time Interval You Want In Seconds: \n')
    try:
        int(interval)
    except ValueError:
         print('Time can be an integer only!')
    else:
        flag = False

    # creating the files needed
    if not os.path.exists(os.path.abspath('logs')):
        os.mkdir('logs')
    a=open("logs/processList.out",'w+')
    b=open("logs/Status_Log.txt",'w+')
    a.close()
    b.close()

    #define watcher Thread
    class myWatch(threading.Thread):
        def __init__(self,fileName):
            self.fileName = fileName
            threading.Thread.__init__(self)
        def run(self):
            threading.Lock().acquire()
            watcher(self.fileName)
            threading.Lock().release()

    processWatch = myWatch('logs/processList.out')
    statWatch = myWatch('logs/Status_Log.txt')
    processWatch.start()
    statWatch.start()

    # enter the processes data to a file
    processList = open('logs/processList.out', 'w+')
    processList.write('Time: ')
    processList.write(str(datetime.datetime.now()))
    processList.write('\n')
    sys.stdout = processList
    psutil.test()
    sys.stdout = sys.__stdout__
    os.chmod('logs/processList.out', 0600)
    os.chmod('logs/Status_Log.txt', 0600)

    current = list()
    processList = open('logs/processList.out', 'r')
    for line in processList:
        current.append(line)
    processList.close()
    current = current[1:]

    while True:
       # updating files
        prev = list()
        processList = current
        for process in processList:
            prev.append(process)

        # wait before updating the current situation
        time.sleep(float(interval))

        # updating the current situation
        del current [:]
        temp = tempfile.TemporaryFile()
        processList = open('logs/processList.out', 'a+')
        processList.write('\nTime: ')
        processList.write(str(datetime.datetime.now()))
        processList.write('\n')
        sys.stdout = processList
        psutil.test()
        sys.stdout = temp
        psutil.test()
        processList.close()
        sys.stdout = sys.__stdout__

        temp.seek(0)
        for line in temp:
            current.append(line)
        temp.close()

        # looking for changes made
        secretFile = prev
        processList = current
        statusLog = open('logs/Status_Log.txt','a+')

        #case 1: new process
        for process in processList:
            list1 = process.split(' ')
            flag = False
            for prePrs in secretFile:
                list2 = prePrs.split(' ')
                if list1[len(list1) - 1] == list2[len(list2) - 1]:
                    flag = True
                    break
            if flag == False:
                statusLog.write('New: ')
                statusLog.write(process)
                print 'New: ', process

        statusLog.close()

        statusLog = open('logs/Status_Log.txt', 'a+')

        # case 2: killed process
        for prePrs in secretFile:
            list1 = prePrs.split(' ')
            flag = False
            for process in processList:
                list2 = process.split(' ')
                if list1[len(list1) - 1] == list2[len(list2) - 1]:
                    flag = True
                    break
            if flag == False:
                statusLog.write('Killed: ')
                statusLog.write(prePrs)
                print 'Killed: ', prePrs

        statusLog.close()












