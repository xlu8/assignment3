def key(Input):
   num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   alpha="abcdefghijklmnopqrstuvwxyz"

   for i in Input :
     if i in alpha :
         index = alpha.find(i)
         num[index] +=1
   
   max1 = 0
   index1 =0
   for j in range(26):
      if (max1 < num[j]):
          max1 = num[j]
          index1 = j 

   key = index1 -4
   if(key<0):
       key+=26

   return key

def get_text(Input,key):
  result =""
  for i in range(len(Input)):
    a = Input[i]
    if(a.isupper()):
        a=a.lower()
    if(a.isalpha()):
       if(ord(a) - key <0):
           result +=chr((ord(a) - key +26 -97) %26 +97)
       else:
           result +=chr((ord(a) -key -97) %26 +97)
    else:
       result +=a
  return result

name =raw_input("enter file's name: ")
Input = open("{0}".format(name)).read()
key = key(Input)
print("key :{0} \n".format(key))
print("recovered text: \n {0}".format (get_text(Input,key)))
