nl=[]
#this is wrong, range will generate numbers from and until
#if you do range(1,5), it will print 1,2,3,4
for x in range(2000, 3200):
   if (x%7==0) and (x%5!=0):
       nl.append(str(x))

print (','.join(nl))
