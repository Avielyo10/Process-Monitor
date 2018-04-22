import os
def watcher(fileName):
    while True:
      if not os.path.exists(os.path.abspath('logs')):
          os.mkdir('logs')
      if not os.path.exists(os.path.abspath(fileName)):
          open(fileName,'w+')
          statLog = open('logs/Status_Log.txt','w')
          statLog.write('SomeOne Is Trying To Delete Or Transfer Your Files')
          print 'SomeOne Is Trying To Delete Or Transfer Your Files'
          print ''
          os.chmod(fileName,0600)


