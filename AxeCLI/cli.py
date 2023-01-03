import os
print('Welcome to AxeCLI.')
initcmd = input('$ ')
while True:
  if initcmd == 'axe setup':
    filename = input('filename(eg. main.abr): ')
    try:
      os.system(f'python3 -m axe {filename}')
    except:
      print('AxeCLI Render=*/')
  elif initcmd == 'axe -render:first:setup':
    filename = input('filename(eg. main.abr): ')
    os.system(f'python3 -m axe {filename}')
  elif initcmd == 'axe create pip':
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
  elif initcmd == 'axe install pip':
    os.system('python3 get-pip.py')
  elif initcmd == 'axe start':
    os.system('touch define.abr')
    print('File Created: define.abr')
  elif initcmd == 'axe start -n':
    askname = input('Name of File: ')
    os.system(f'touch {askname}.abr')
