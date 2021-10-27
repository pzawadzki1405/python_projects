name = input('Enter file name:')

try:
    file = open(name)       #tries to open file 'name'
except:
    print('wrond file name')
    quit()                  #quit the program, skip the lines of code below

count = 0
for line in file:
    count=count+1
    print(line.rstrip()[(line.find('[')+1):line.find(']')]) #rstrip skip \n and space
                        #find show position of character in string
                        #character ':' cuts the string

print('this file have ',count,'lines')
