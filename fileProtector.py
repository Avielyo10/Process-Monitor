import os
def watchwer(fileName):
    while True:
      if not os.path.exists(os.path.abspath(fileName)):
          print 'SomeOne Is Trying To Delete Or Modify Your Files'
          print ''
          open(fileName,'w+')
          os.chmod(fileName,0600)


