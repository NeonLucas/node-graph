from collections import defaultdict

d = defaultdict(list)


#Weighted BiDirectional Edge
def create_w_biedge(graph, x, y, weight = 1):
	graph[x].append((y, weight))
	graph[y].append((x, weight))


#print all edges in graph in a neat format
def print_edges(graph):
	for i in graph:
		for k in graph[i]:
			print(i, "-->", k, sep = " ")


#initialize graph and set preliminary distance values for the nodes of the graph from start
def initialize_graph(graph, start):
	global distance_set
	distance_set = {}
	for i in graph:
		if i == start:
			distance_set[i] = 0
		else:
			distance_set[i] = 999999999999999999999


#calculates distance to nearest nodes
def calculate_dist(graph, current_choice):
	global distance_set

	tbo = [] # to be opened(distances will be updated)

	for i in graph[current_choice]:
		tbo.append(i)
	
	travelled = distance_set[current_choice]
	
	for i in tbo:
		dist = i[1] + travelled #distance from start = distance travelled + weight of edge

		if dist < distance_set[i[0]]:
			distance_set[i[0]] = dist




#finds shortest distance to every node in a weighted graph
def find_short_dist(graph, start):
	global spt_set
	initialize_graph(graph, start)

	spt_set = [] #shortest path tree set(calculated nodes)

	while len(spt_set) < len(graph):
		
		minimum = 99999999999
		
		for i in distance_set:
			if distance_set[i] < minimum and i not in spt_set:
				minimum = distance_set[i]
				current_choice = i
			else:
				pass

		spt_set.append(current_choice)
		calculate_dist(graph, current_choice)
	
	print(distance_set)

create_w_biedge(d, "A", "B", 8)
create_w_biedge(d, "A", "C", 4)
create_w_biedge(d, "B", "D", 1)
create_w_biedge(d, "C", "D", 7)
create_w_biedge(d, "C", "E", 3)
create_w_biedge(d, "D", "F", 1)
create_w_biedge(d, "E", "F", 2)
create_w_biedge(d, "C", "G", 2)
create_w_biedge(d, "E", "G", 1)
create_w_biedge(d, "G", "K", 5)
create_w_biedge(d, "F", "K", 1)

initialize_graph(d, "A")


find_short_dist(d, "A")

print_edges(d)




# NEED TO DO FURTHER TESTING(done)