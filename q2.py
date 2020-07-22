def key(Input):
   num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   al ='abcdefghijklmnopqrstuvwxyz'

   for i in Input :
     if i in al :
         index = al.find(i)
   
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
name =raw_input("enter file's name: ")
Input = open("{0}".format(name)).read()
key = key(Input)
print("key :{0}".format(key))
