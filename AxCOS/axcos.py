import string
import random
print('Welcome to AxCOS standalone.')
initcmd = input('$ ')
while True:
  if initcmd == 'cos ver':
    print('V:3.5')
  elif initcmd == 'cos ver -cli':
    print('CLI3.5')
  elif initcmd == 'cos op':
    print("Operational:100%")
  elif initcmd == 'generate xeno':
    randomLetter2 = random.choice(string.ascii_letters)
    randomLetter3 = random.choice(string.ascii_letters)
    randomLetter4 = random.choice(string.ascii_letters)
    randomLetter44 = random.choice(string.ascii_letters)
    r33codex = randomLetter44.upper()
    number = random.randint(1, 9)
    number2 = random.randint(1, 9)
    number3 = random.randint(1, 9)
    number4 = random.randint(1,8)
    number5 = random.randint(1,3)
    print(randomLetter2+randomLetter3+randomLetter4+r33codex+'XENO'+str(number)+str(number2)+str(number3)+str(number4)+str(number5))
    break
    
    