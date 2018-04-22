import os, datetime
def isExists():
    if not os.path.exists(os.path.abspath('logs/processList.out')):
        print 'processList.out is not exists.'
        exit()
def findDiff(fileOne,fileTWo,someString):
    for line in fileOne:
        list1 = line.split(' ')
        flag = False
        for anotherLine in fileTWo:
            list2 = anotherLine.split(' ')
            if list1[len(list1) - 1] == list2[len(list2) - 1]:
                flag = True
                break
            if flag == False:
                print someString, line

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

def takeSample(sample):
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
fileOne = takeSample(firstSample)
fileTwo = takeSample(secondSample)
