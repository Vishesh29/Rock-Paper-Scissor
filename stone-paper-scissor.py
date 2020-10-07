#A short fun program in python that will let you play Stone Paper Scissor with it when you are bored:)

from random import randint
player=input('rock(r),paper(p),scissor(s)')
print('player:',player)

choice=randint(1,3)
if choice==1:
	computer='r'
elif choice==2:
	computer='p'
else:
	computer='s'

print('vs computer:',computer)

if player==computer:
	print('draw')
elif (player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
	print('You won!!!!')
else:
	print('computer won')

input("press enter to exit")