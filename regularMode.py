import os, datetime

def isExists():
    """
    check if file is already exists
    :return: if not exist exit the program
    """
    if not os.path.exists(os.path.abspath('logs/processList.out')):
        print 'processList.out is not exists.\n'
        exit()

def findDiff(fileOne,fileTWo,someString):
    """
    check for difference between the two files, if killed or new process has come up
    :param fileOne: the first file
    :param fileTWo: the second file
    :param someString: killed or new
    :return: print on the screen the killed or new process
    """
    status = open('logs/Status_Log.txt','a+')
    for line in fileOne:
        list1 = line.split(' ')
        flag = False
        for anotherLine in fileTWo:
            list2 = anotherLine.split(' ')
            if list1[len(list1) - 1] == list2[len(list2) - 1]:
                flag = True
                break
        if flag == False:
            status.write(someString)
            status.write(line)
            print someString, line

    status.close()

def nearest(items, pivot):
    """
    :param items: list of type datetime
    :param pivot: the one pivot we are referring to
    :return: return the nearest item in items to the pivot
    """
    return min(items, key=lambda x: abs(x - pivot))

def whoIsOlder(items):
    """
    :param items: takes a list of items and find the older file
    :return: the index of the older file in items
    """
    newItems = list()
    for i in items:
       newItems.append(datetime.datetime.strptime(i,'%Y-%m-%d %H:%M:%S'))

    sample = nearest(newItems,datetime.datetime.strptime('1900-01-01 00:00:00','%Y-%m-%d %H:%M:%S'))
    if items[0] == sample:
        return 0
    else:
        return 1


def takeSample(sample):
    """
    :param sample: the user datetime input
    :return: parsed data from the file into a list
    """
    processList = open('logs/processList.out', 'r')
    dates = list()
    for line in processList:
        splLine = line.split(' ')
        if splLine[0] == 'Time:':
            dates.append(datetime.datetime.strptime(line[6:-8], '%Y-%m-%d %H:%M:%S'))
    processList.close()

    dd = nearest(dates,datetime.datetime.strptime(sample,'%Y-%m-%d %H:%M:%S'))
    closestDate = 'Time: ' + str(dd)
    out = list()
    processList = open('logs/processList.out', 'r')
    flag = False
    for line in processList:
        if flag:
            if line == '\n':
                break
            out.append(line)
        if line[:-8] == closestDate:
            flag = True

    return out

def ui(numOfDate):
    """
    :param numOfDate:some string 'first' or 'second'
    :return: the date and time from the user
    """
    flag1 = True
    flag2 = True
    while flag1 or flag2:
        flag1 = True
        flag2 = True
        print 'Please Enter '+ numOfDate +' Date:'
        date = raw_input('Enter DD/MM/YY: ')
        time = raw_input('Enter HH:MM:SS: ')
        try:
            d = datetime.datetime.strptime(date, '%d/%m/%y')
            flag1 = False
        except:
            print 'Date is not inserted correctly!'
        try:
            t = datetime.datetime.strptime(time, '%H:%M:%S')
            flag2 = False
        except:
            print 'Time is not inserted correctly!'

    d = str(d)
    date = d.split(' ')
    date = date[0]
    t = str(t)
    time = t.split(' ')
    time = time[1]
    return date + ' ' + time


isExists()
firstSample = ui('First')
print '\n'
secondSample = ui('Second')
print '\n'
items = [firstSample,secondSample]
oneOrZero = whoIsOlder(items)
if oneOrZero == 0:
    fileOne = takeSample(firstSample)
    fileTwo = takeSample(secondSample)
else:
    fileOne = takeSample(secondSample)
    fileTwo = takeSample(firstSample)

findDiff(fileOne,fileTwo,'New: ')
findDiff(fileTwo,fileTwo,'Killed: ')