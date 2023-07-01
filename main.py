from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

# file1 = drive.CreateFile({'title': 'Hello.txt'})  
# file1.SetContentString('Hello World!') 
# file1.Upload()


file_list = drive.ListFile({'q': "'1lDdFhvdE57NFfrSi6JYaYmJdGjl0s-zd' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  file1.GetContentFile(file1['title'])
# file2 = drive.CreateFile()
# file2.SetContentFile('client_secrets.json')
# file2.Upload()
# title: Study class 11, id: 1lDdFhvdE57NFfrSi6JYaYmJdGjl0s-zd
# file3 = drive.CreateFile({'id': "1lDdFhvdE57NFfrSi6JYaYmJdGjl0s-zd"})
# print('Downloading file %s from Google Drive' % file3['title']) # 'hello.png'
# file3.GetContentFile('main.webm')
input()