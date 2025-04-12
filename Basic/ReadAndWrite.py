'''

file = open('ReadAndWrite.txt', 'r')
for lines in file.readlines():
  print(lines)
file.close()

'''


file = open('ReadAndWrite2.txt', 'a')
file.write('\nThis is the new text')
file.close()
