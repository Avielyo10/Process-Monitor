import os
def watchwer(fileName):
    while True:
      if not os.path.exists(os.path.abspath(fileName)):
          open(fileName,'w+')
          statLog = open('Status_Log.txt','w')
          statLog.write('SomeOne Is Trying To Delete Or Transfer Your Files')
          print 'SomeOne Is Trying To Delete Or Transfer Your Files'
          print ''
          os.chmod(fileName,0600)
          statLog.close()


