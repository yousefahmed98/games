from __future__ import print_function
import subprocess as sp
arr1=["|","A","|","B","|","C",'|']
arr2=["|","D","|","E","|","F",'|']
arr3=["|","G","|","H","|","I",'|']
arr4=["","","","","","","","",""]
arr5=["","","","","","","","",""]
def draw():
  print("-------")
  print(*arr1, sep='')
  print("-------")
  print(*arr2, sep='')
  print("-------")
  print(*arr3, sep='')
  print("-------")
draw()
k=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
while k !=9:
  x=y=z=count=counter=0
  if k%2==0:
    player1=str(input("player1, please enter the position:"))
    while player1!="A" and player1!="B" and player1!="C" and player1!="D" and player1!="E" and player1!="F" and player1!="G" and player1!="H" and player1!="I" : 
      print("you should enter alphabet from A to I")
      player1=str(input("player1, please enter your new Position:"))
      if  player1=="A" or player1=="B" or player1=="C" or player1=="D" or player1=="E" or player1=="F" or player1=="G" or player1=="H" or player1=="I" : 
        break
    
    while count<9 :
       if arr4[count]==player1:
         player1=str(input("player1 enter another position:"))
       count+=1
    arr4[count9]=player1
    count9+=1
    num1=int(input("player,enter number"))
    while counter<9 :
       if arr5[counter]==num1:
         num1=int(input("player1,enter another number:"))
       counter+=1
    arr5[count10]=num1
    count10+=1
    if num1>9:
      print("you should use numbers from 1 to 9")
      num1=int(input("player1,enter number:"))      
    while num1%2==0:
      print("you should use odd numbers")
      num1=int(input("player1,enter number:"))
      if num1%2!=0:
        break
    if player1=="A":
      x=1
    if player1=="B":
      x=3
    if player1=="C":
      x=5
    if player1=="D":
      y=1
    if player1=="E":
      y=3
    if player1=="F":
      y=5
    if player1=="G":
      z=1
    if player1=="H":
      z=3
    if player1=="I":
      z=5
    if x==1 or x==3 or x==5:
      arr1[x]=num1
      count1=count1+1
      if x==1:
        count4+=1
        count6+=1
      if x==5:
        count5+=1
        count8+=1
      if x==3:
        count7+=1
    if y==1 or y==3 or y==5:
      arr2[y]=num1
      count2=count2+1
      if y==3:
        count5+=1
        count4+=1
        count7+=1
      if y==1:
        count6+=1
      if y==5:
        count8+=1
    if z==1 or z==3 or z==5:
      arr3[z]=num1
      count3=count3+1
      if z==5:
        count4+=1
        count8+=1
      if z==1:
        count5+=1
        count6+=1
      if z==3:
        count7+=1  
    draw()
    tmp = sp.call('cls',shell=True)
    if count1==3:
      if arr1[1]+arr1[3]+arr1[5]==15:
        print("Player1 is winner")
        break
    if count2==3:
      if arr2[1]+arr2[3]+arr2[5]==15:
        print("Player1 is winner")
        break
    if count3==3:
      if arr3[1]+arr3[3]+arr3[5]==15:
        print("Player1 is winner")
        break
    if count4==3:
      if arr1[1]+arr2[3]+arr3[5]==15:
        print("Player1 is winner")
        break
    if count5==3:
      if arr1[5]+arr2[3]+arr3[1]==15:
        print("Player1 is winner")
        break
    if count6==3:
      if arr1[1]+arr2[1]+arr3[1]==15:
        print("Player1 is winner")
        break
    if count7==3:
      if arr1[3]+arr2[3]+arr3[3]==15:
        print("Player1 is winner")
        break
    if count8==3:
      if arr1[5]+arr2[5]+arr3[5]==15:
        print("Player1 is winner")
        break
      
    
  else:
    draw()
    player2=str(input("player2,Enter position:"))
    while player2!="A" and player2!="B" and player2!="C" and player2!="D" and player2!="E" and player2!="F" and player2!="G" and player2!="H" and player2!="I" :
            print( "you should enter alphabet from A to I")
            player2=str(input("player2,enter position:"))
            if  player2=="A" or player2=="B" or player2=="C" or player2=="D" or player2=="E" or player2=="F" or player2=="G" or player2=="H" or player2=="I" : 
              break
    while count<9 :
       if arr4[count]==player2:
         player2=str(input("player2, enter another position:"))
       count+=1
    arr4[count9]=player2
    count9+=1
    num2=int(input("player2,Enter number:"))
    while counter<9 :
       if arr5[counter]==num2:
         num2=int(input("player2,enter another number:"))
       counter+=1
    arr5[count10]=num2
    count10+=1
    if num2>8:
      print("you should use numbers from 0 to 8 ")
      num2=int(input("player2, enter number:"))
        
    while num2 %2!=0:
      print("you should use even numbers")
      num2=int(input("player2, enter number:"))
      if num2%2==0:
        break
      
    if player2=="A":
      x=1
    if player2=="B":
      x=3
    if player2=="C":
      x=5
    if player2=="D":
      y=1
    if player2=="E":
      y=3
    if player2=="F":
      y=5
    if player2=="G":
      z=1
    if player2=="H":
      z=3
    if player2=="I":
      z=5
    if x==1 or x==3 or x==5:
      arr1[x]=num2
      count1+=1
      if x==1:
        count4+=1
        count6+=1
      if x==5:
        count5+=1
        count8+=1
      if x==3:
        count7+=1  
    if y==1 or y==3 or y==5:
      arr2[y]=num2
      count2+=1
      if y==3:
        count4+=1
        count5+=1
        count7+=1 
      if y==1:
        count6+=1
      if y==5:
        count8+=1
    if z==1 or z==3 or z==5:
      arr3[z]=num2
      count3+=1
      if z==5:
        count4+=1
        count8+=1
      if z==1:
        count5+=1
        count6+=1
      if z==3:
        count7+=1 
    draw()
    tmp = sp.call('cls',shell=True)
    if count1==3:
      if arr1[1]+arr1[3]+arr1[5]==15:
        print("Player2 is winner")
        break
    if count2==3:
      if arr2[1]+arr2[3]+arr2[5]==15:
        print("Player2 is winner")
        break
    if count3==3:
      if arr3[1]+arr3[3]+arr3[5]==15:
        print("Player2 is winner")
        break
    if count4==3:
      if arr1[1]+arr2[3]+arr3[5]==15:
        print("Player2 is winner")
        break
    if count5==3:
      if arr1[5]+arr2[3]+arr3[1]==15:
        print("Player2 is winner")
        break
    if count6==3:
      if arr1[1]+arr2[1]+arr3[1]==15:
        print("Player2 is winner")
        break
    if count7==3:
      if arr1[3]+arr2[3]+arr3[3]==15:
        print("Player2 is winner")
        break
    if count8==3:
      if arr1[5]+arr2[5]+arr3[5]==15:
        print("Player2 is winner")
        break
  k=k+1  
print("END GAME")
    
           
      
