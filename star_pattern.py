row = int (input ("Enter number of rows "))
for i in range ( row , 0 ,-1 ) :
      print (' * ' * (i))


==============
row = int (input ("Enter number of rows "))
for i in range ( 1, row+1 ) :
      print (' * ' * (i))

===============
row = int (input ("Enter number of rows "))
for i in range (0,row) :
   for j in range(0,row-i-1):
     print(end=" ")
   for j in range(0,i+1):
      print('*',end="")
   print()

=======================
row = int (input ("Enter number of rows "))
for i in range (1,row+1) :
   for j in range(1,i+1):
       print(j,end="")
   print()

============================
row = int (input ("Enter number of rows "))
for i in range (1,row+1) :
   for j in range(1,i+1):
       print(i,end="")
   print()   
