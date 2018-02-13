from random import *
import subprocess as sp
from random import randint
import random
def pause():
        p=0
        while(p<20000000):
            p+=1
def draw():
        print(*num, sep='')

i=score1=score2=n=counter=counter2=0
b=10
num=['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9']
alpha=['A','B','C','D','E','F','G','H','I','J']
alpha2=['A','B','C','D','E','F','G','H','I','J']
arr=['','','','','','','','','','','','','','','','','','','','']
l=['*','*',"*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]
while(len(alpha)!=0):
    z=str(random.choice(list(alpha)))
    q=str(random.choice(list(alpha2)))
    arr[i]=z
    arr[b]=q
    alpha.remove(z)
    alpha2.remove(q)
    i+=1
    b+=1
print(*arr, sep='')
pause()
pause()
tmp = sp.call('cls',shell=True)

draw()



while(num!=l ):
    
    if(n%2==0):
        while True:
          input1=(int(input("player 1 enter number  from 0 to 9")))
          input2=(int(input("player 1 enter sec number  from 0 to 9")))
          while num[input1]=="*" or num[input2]=="*":
                 input1=(int(input("player1 enter another num from 0 to 9 ")))
                 input2=(int(input("player1 enter another num from 0 to 9 ")))
                  
          if input1>9 or input2>9:
              print("wrong numbers")
              tmp = sp.call('cls',shell=True)
              draw()
          if input1<=9 and input2<=9:
            break
        
        print(arr[input1])
        print(arr[input2+10])
        if(arr[input1]==arr[input2+10]):
            score1+=1
            num[input1]=num[input2+10]="*"
            
        n+=1
        
        pause()       
        tmp = sp.call('cls',shell=True)
        
        draw()
        
    if(n%2!=0):
        while True:
          input1=(int(input("player 2 enter number  from 0 to 9")))
          input2=(int(input("player 2 enter sec number  from 0 to 9")))
          while num[input1]=="*" or num[input2]=="*":
                 input1=(int(input("player1 enter another num from 0 to 9 ")))
                 input2=(int(input("player1 enter another num from 0 to 9 ")))
                  

          if input1>9 or input2>9:
              print("wrong numbers")
              tmp = sp.call('cls',shell=True)
              draw()
          if input1<=9 and input2<=9:
            break
        print(arr[input1])
        print(arr[input2+10])
        if(arr[input1]==arr[input2+10]):
            score2+=1
            num[input1]=num[input2+10]="*"
        n+=1
        pause()
        tmp = sp.call('cls',shell=True)
        draw()
        
if(score1>score2):
    print("mabrook player 1")
elif(score2>score1):
    print("mabrook player 2")
else:
    print("draw")

