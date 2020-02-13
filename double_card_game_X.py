import random
import string
import time
import sys, select
from multiprocessing import Process
def f2():
     time.sleep(4)
     sys.exit(0)
def f1():
     choice=select.select([sys.stdin],10)
     if(choice==ss):
          print('right answer')
     else:
          print('wrong answer')
def play():
     print()
play()    
alfa=[]
#start = "\033[1m"
#end = "\033[0;0m"
#print(start,'[1mSYMBOL MATCH GAME',end)
print('SYMBOL MATCH GAME')
size=int(input('enter size of cards'))
alfa=list(string.ascii_letters)
card1=[0]*size
card2=[0]*size
pos1=random.randint(0,size-1)
pos2=random.randint(0,size-1)
ss=random.choice(alfa)
alfa.remove(ss)
card1[pos1]=ss
card2[pos2]=ss
i=0
while(i<size):
     if(i!=pos1):
          card1[i]=random.choice(alfa)
          alfa.remove(card1[i])
     if(i!=pos2):
          card2[i]=random.choice(alfa)
          alfa.remove(card2[i])
     i=i+1
print(card1)
print(card2)     


choice=input('enter answer')
if(choice==ss):
     print('right answer')
else:
     print('wrong answer')

time.sleep(3)
sys.exit(0)
     


