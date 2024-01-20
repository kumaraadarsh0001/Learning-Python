import sys
# stdout assigned to a variable
var = sys.stdout
arr = ['geeks', 'for', 'geeks']
# printing everything in the same line
for i in arr:
	var.write(i)
# printing everything in a new line
for j in arr:
	var.write('\n'+j)