#!/usr/bin/python
# Import modules for CGI handling
import cgi,cgitb
import csv
from csv import writer
# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('user')
last_name = form.getvalue('pass')

count=0

password1 = form.getvalue('use')
password2 = form.getvalue('pas')

if(password1 != None and password2 != None):
  count=1

print ("Content-Type: text/html\n\n")
print ("<html>")
print ("<head>")
print ("</head>")
print ("<body>")

if(count == 1):
 if password1 == 'eri' and password2 == '12345678':
   print("<h1>Duplicate Username and password</h1>")
 if password1 == 'eri' and password2 != '12345678':
   print("<h1>Duplicate Username</h1>")
 if password1 != 'eri' and password2 == '12345678':
   print("<h1>Duplicate Password</h1>")
 if password1 != 'eri' and password2 != '12345678':
   print("<h1>Successfully created a New Account</h1>")
   List=[password1,password2]
   for x in range(len(List)):
    print List[x],
   with open('Database.csv') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(List)
    csvfile.close()

else:
 found=0
 with open('Database.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  for row in spamreader:
    if row[0] == first_name and last_name == row[1]:
      found=1

    
 if(found==1):
   print("<h1>Successfully Logged in</h1> </br> <h2>Please click the below button to see the past Projects</h2> </br> <button onclick=show('Project','Home','Courses','Aboutme','CV','signup')>Past Projects</button> " )  
 else:
   print("<h1>Incorrect Login/Signup</h1>")
	
print ("</body>")
print ("</html>")