import sys
count=0
a=sys.argv[1]
file = open("test1.txt",'r')

for line in file:
	if a in line:
		print("match found")
		count=count+1	
	else:
		print("not found")
print(count)
sys.exit()


