import psutil, sys, time

print('\t\t####### Process Monitor #######')
flag = True
while flag:
    interval = raw_input('Please Enter The Time Interval You Want In Seconds: \n')
    try:
        int(interval)
    except ValueError:
         print('Time can be an integer only!')
    else:
        flag = False

    """
    creating the processList & Status_Log output
    :return:
    two log files
    """
    # creating the files needed
    a=open("processList.out",'w+')
    b=open("Status_Log.txt",'w+')
    a.close()
    b.close()

    # enter the processes data to a file
    processList = open('processList.out', 'w')
    org = sys.stdout
    sys.stdout = processList
    psutil.test()
    processList.close()
    sys.stdout = org

    while True:
       # updating files
        prev = list()
        processList = open('processList.out', 'r')
        for process in processList:
            prev.append(process)

        # wait before updating the current situation
        time.sleep(float(interval))

        # updating the current situation
        processList = open('processList.out', 'w')
        org = sys.stdout
        sys.stdout = processList
        psutil.test()
        processList.close()
        sys.stdout = org

        # looking for changes made
        processList = open('processList.out', 'r')
        secretFile = prev
        statusLog = open('Status_Log.txt','a')

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

        processList.close()
        statusLog.close()

        processList = open('processList.out', 'r')
        statusLog = open('Status_Log.txt', 'a')

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

        processList.close()
        statusLog.close()












