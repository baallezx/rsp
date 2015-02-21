def create_graph(contents):
	"""
	if you are given a -1 then it does not point to anything.
	"""
	d = {}
	for i in xrange(len(contents)):
		d[i] = int(contents[i])
	return d

def _cycle(graph, key, stack, stacks):
	# print graph, key, stack
	if ( key , graph[key] ) in stack: # you have found a cycle
		stacks.append(stack)
		return # True
	elif graph[key] == -1: # dead end
		return None # False
	else:
		stack.append( ( key , graph[key] ) )
		_cycle( graph, graph[key], stack, stacks )
		# print stack

def find_cycles(graph):
	"""
	find all the cycles in a Directed Acyclic Graph.
	"""
	stacks = []
	for k,v in graph.items():
		stack = []
		_cycle(graph, k, stack, stacks)
	results = []
	for i in stacks:
		i.sort()
		if i not in results:
			results.append(i)
		#print i
	print len(results)

if __name__ == "__main__":
	import sys
	l = sys.argv[1:]
	r = open(l[0],'r').read().split('\n')
	r.remove('')
	# print r
	N = r[0]
	graph = create_graph(r[1:])
	# print graph
	find_cycles(graph)
