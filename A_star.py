#creation of grid
def create_grid(x,y):

	grid = []
	for i in range(1, y+1):
		row = []
		for k in range(1, x+1):
			row.append([k,i])# co ordinate of each cell ps. parent cell gets added in the main program
		grid.append(row)
	return grid


def create_wall(x,y,grid):

	grid[y-1][x-1] = "X"


def display_coords(grid):

	for i in grid:
		print(i)


def display_grid(grid, path = [], start = None, end = None):

	out = []
	for i in grid:
		row = []
		for k in i:
			if k == "X":
				row.append("X")
			elif k == start:
				row.append("S")
			elif k == end:
				row.append("E")
			elif k in path:
				row.append("0")
			else:
				row.append(" ")
		out.append(row)
	for i in out:
		print(i)


def calc_walkdist(node1, node2, pg):

	if abs(node1[0] - node2[0])+abs(node1[1] - node2[1]) == 2:
		g_cell = pg + 12
	else:
		g_cell = pg + 10

	return g_cell


def calc_heuristic(node, goal_node):

	h = abs(node[0] - goal_node[0]) + abs(node[1] - goal_node[1])
	return h


def op_pop_min(ls): # to find and pop out the node with min f in open list

	mini = 9999999999999999999999999999999
	for i in ls:
		if i[2] < mini:
			mini = i[2]
			out = ls.index(i)
	return ls.pop(out)


def wallcheck(node, grid): #checks if a wall exists at certain index (works)

	x_max_in = len(grid[0]) - 1 # index
	y_max_in = len(grid) - 1 # index

	x_in = node[0] - 1
	y_in = node[1] - 1

	if x_in < 0 or x_in > x_max_in or y_in < 0 or y_in > y_max_in:
		return False
	else:
		if g[y_in][x_in] == "X":
			return False
		else:
			return True

def read_cl_list(lis, end):
	global path
	parent = end

	while parent != "START":
		for i in cl_list:
			if i[0] == parent:
				parent = i[1]
				path.append(parent)
				break


def calculate(opened, grid, end): # write the end case tmrw
	global op_list, cl_list, finish_check

	diag_search = [[-1,-1], [1,-1], [-1,1], [1,1]]
	line_search = [[0,-1], [1,0], [0,1], [-1,0]]

	open_node = opened[0]
	
	for i in diag_search + line_search:

		node = [open_node[0] + i[0], open_node[1] + i[1]]

		if node == end: # what happens when u reach the end node
			cl_list.append([node, open_node])
			cl_list.append(opened)
		
			finish_check = True
			return

		if wallcheck(node, grid): # if it is not a well it passes in
			node_g = calc_walkdist(open_node, node, opened[3])
			node_h = calc_heuristic(node, end)
			node_f = node_g + node_h 

			add_check = True
			
			for i in op_list + cl_list: # If at any point found out that a better path already exists to current node it breaks
				if node == i[0] and node_f > i[2]:
					add_check = False
					break
				else:
					pass

			if add_check:
				op_list.append([node, open_node, node_f, node_g])
			else:
				pass

		else:
			pass

	cl_list.append(opened)


def a_star(start, end, grid):
	global op_list, cl_list, finish_check

	op_list = [] # contains all the nodes to be calculated, their parents, f value and g value
	cl_list = [] # contains all the nodes that are already calculated, their parents , f values and g values(cuz too lazy to remove)
	finish_check = False

	op_list.append([start, "START", 0, 0]) # node, parent node, f, g

	while len(op_list) != 0:
		opened = op_pop_min(op_list)

		calculate(opened, g, end)

		if finish_check:
			read_cl_list(cl_list, end)
			break

path = []
g = create_grid(7,5)
create_wall(2,1,g)
create_wall(2,2,g)
create_wall(1,3,g)
create_wall(3,3,g)
create_wall(3,4,g)
create_wall(4,5,g)
create_wall(5,1,g)
create_wall(5,3,g)
create_wall(6,2,g)
create_wall(6,4,g)
create_wall(7,3,g)


#display_coords(g)
#display_grid(g, [], [1,1], [5,8])
#calculate([[4,1], "START", 0, 30], g, [5,8])
a_star([1,1], [7,5], g)
print(path)
display_grid(g, path, [1,1], [7,5])
