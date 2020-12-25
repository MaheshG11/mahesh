'''i=0
while i<10:
    print(i**2)
    i=i+1'''
'''
FACTORIAL
'''
'''
product=1
n=int(input("give input"))
for i in range(1,n+1):
    product = product*i
print(product)'''


'''
NESTED LOOPS
'''
'''
for i in range(5) :
    for j in range (5) :
        print (i, end='')
    print() '''

#for i in range(5) :
#    for j in range (5) :
#        print ("*", end='  ')
#    print()

'''
n=int(input())
for i in range(1,n+1):
     for j in range(1,i+1):
         print('*', end= '  ')
     print()
'''

'''
BREAK  AND CONTINUE
'''

'''for i in range(10):
    if i%2 ==0 :
        continue #loop skipping statement - loop below it gets skippeed
                 # and starts from above
    if i==7 :
        break #loop exiting statement - it will exit the current loop
              # which is for in this condn
'''

'''n = int(input('enter a number'))
for i in range(2,n) :
     if n%i== 0 :
         break

if n%i==0 :
    print ("number is not prime")
else :
    print ("number is prime")
'''

'''for i in range (0,5,1) :
    for j in range(0,i+1,1):
        print(2**j, end=' ')
    print()
'''
#strip() - it removes starting and ending white spaces
#split() - it splits the string in a group of characters
#len() - number of words after split
#eval() - evaluates



