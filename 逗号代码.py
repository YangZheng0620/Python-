spam = ['apples','bananas','tofu','cats']

def func(l):
	tempStr = l[0]
	for i in range(len(l)):
		if i == 0:
			tempStr = tempStr
		elif i == len(l) - 1:
			tempStr = tempStr + ' and ' + l[i]
		else:
			tempStr = tempStr + ', ' + l[i]
	return tempStr

print(func(spam))

import copy

grid = [ ['.', '.', '.', '.', '.','.'],
         ['.', '0', '0', '.', '.','.'],
         ['0', '0', '0', '0', '.','.'],
         ['0', '0', '0', '0', '0','.'],
         ['.', '0', '0', '0', '0','0'],
         ['0', '0', '0', '0', '0','.'],
         ['0', '0', '0', '0', '.','.'],
         ['.', '0', '0', '.', '.','.'],
         ['.', '.', '.', '.', '.','.']]

for row in range(len(grid[0])):
	print()
	for col in range(len(grid)): 
		print(grid[col][row],end = '')
