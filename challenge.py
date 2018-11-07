
def printStars(m, n):
	for i in range(0,m):
		print '*' * n;


def order(list):
	list.sort()
	for i in range(len(list)):
		print list[i]

def sum(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	print sum


printStars(3,5)
order(["Tatianna", "Danielle", "Robinson"])
sum(7)