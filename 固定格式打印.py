tableData = [['apples','orange','cherries'],
			['Alice','Bobss','Carols'],
			['dogs','cats','moose']]

def printTbale(table):
	colWidths = [0] * len(table)
	for i in range(len(table)):
		for j in range(len(table[i])):
			
			if len(table[i][j]) > colWidths[i]:
				colWidths[i] = len(table[i][j])
					
	for i in range(len(table)):
		a = ''
		for j in range(len(table[i])):
			a += table[j][i].rjust(colWidths[j]) + ' '
		print(a)

printTbale(tableData)