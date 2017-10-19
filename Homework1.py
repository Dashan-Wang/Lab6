#Problem 1
for i in range(6):
    print("*",end='')
    for n in range(i):
        print(" ",end='')
    print('*')

#Problem 2
def is_prime():
    for i in range(1,101):
        a=0
        if i==1:
            a=1
        else:
            for n in range(2,i):
                if i%n==0:
                    a=1
        if a==0:
            print(i,' ')
is_prime()

#Problem 3
num=int(input("Enter a pocket number:"))
if num<0 or num>36:
   print("It's wrong!")
elif num==0:
    print(num,"is green.")
elif num>=29 or (num>=11 and num<=18) :
    if num%2==1:
        print("The color is black.")
    else:
        print("The color is red.")
else:
    if num%2==1:
        print("The color is red.")
    else:
         print("The color is black.")

#Problem 4
num=int(input("Enter a number of seconds:"))
if num<0:
    print("Wrong!")
day=num//86400
hour=(num-day*86400)//3600
minute=(num-day*86400-hour*3600)//60
num=num-day*86400-hour*3600-minute*60
print("%s days;%s hours;%s minutes: %s seconds"%(day,hour,minute,num))

#Problem 5
for i in range(8):
    if i==7:
        print("****")
    elif i in [0,1,4,5]:
        print(" **")
    else:
        print("*  *")
    
    




    
