grid = []
for i in range(0,9):
	grid.append([])
for i in range (0,9):
	for j in range(0,9):
		grid[i].append(j)
		grid[i][j] = 0

for i in range(0,9):
	for j in range(0,9):
		print ('Enter value of row: ',i+1, ' column: ',j+1)
		grid[i][j] = int(input())

def print_grid(grid):
	for i in range(9):
		if i % 3 == 0 and i != 0:
			print("-----------------------")
		for j in range(9):
			if j % 3 == 0 and j != 0:
				print(" | ", end="")

			if j == 8:
				print(grid[i][j])
			else:
				print(str(grid[i][j]) + " ", end="")


def possible(y,x,n) :

	for i in range(0,9) :
		if grid[y][i] == n:
			return False
	for i in range(0,9) :
		if grid[i][x] == n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3) :
		for j in range(0,3) :
			if grid[y0+i][x0+j] == n:
				return False
	return True

def solve() :
	#global grid
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0 :
				for n in range(1,10) :
					if possible(y,x,n) :
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	print_grid(grid)
	input("More?")

print_grid(grid)
solve()
