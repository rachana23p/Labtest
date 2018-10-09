import sys
count=0
a=sys.argv[1]
file = open("test1.txt",'r')

for line in file:
	lines=line.split(' ')
	#print(lines)
	for i in range(0,len(lines)):
		if a in lines[i]:
			print("match found")
			count=count+1	
		else:
			print("not found")
print(count)
sys.exit()



