import ftplib
import os

ftp = ftplib.FTP('129.9.0.102', 'root', 'Test1234.')        # FTP Connection information
ftp.dir()                                                   # Run "dir" command in current folder - cfcard:
print("..............1............................")
# ftp.mkd('newfile3')                                       # Create new directory

# ftp.cwd("logfile")                                          # Change directory
# ftp.dir()                                                   # Run "dir" command in current folder - cfcard:/logfile
# ftp.delete("umut3.cfg")                                     # Delete a file
# ftp.rmd("newfile3")                                         # Delete a folder

upload = open("Device_List.txt", 'rb')                                          # Choose file in local to upload
ftp.storbinary('STOR %s' % os.path.basename("Device_Lis12t.txt"), upload, 1024)   # File upload from PC to device
