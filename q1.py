import sys

openfile = open("message1.txt").read()
file = open("q1.txt","w")

key = input('enter a number: ')

result =" "
for i in openfile:
   i.lower()
   if(ord(i) >= ord('a') and ord(i)<= ord('z')):
      char =chr(97 + (ord(i) + key -97)%26)
      file.write(char)
   else:
    file.write(i)

file.close()
