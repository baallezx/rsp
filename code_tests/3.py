def create_graph(contents):
	"""
	if you are given a -1 then it does not point to anything.
	"""
	d = {}
	for i in xrange(len(contents)):
		d[i] = int(contents[i])
	return d

def _cycle(graph, key, stack, stacks):
	# TODO: add condition where if the value is a -1 to return False
	print graph, key, stack
	if ( key , graph[key] ) in stack:
		return # True
	elif graph[key] == -1:
		return None # False
	else:
		stack.append( ( key , graph[key] ) )
		_cycle( graph, graph[key], stack, stacks )
		print stack
		stacks.append(stack)

def find_cycles(graph):
	"""
	find all the cycles in a Directed Acyclic Graph.
	"""
	cycles = 0
	stacks = []
	for k,v in graph.items():
		stack = []
		# results = _cycle(graph, k, stack, stacks)
		_cycle(graph, k, stack, stacks)
#		if isinstance(results,list):
#			stacks.append( results.sort() )
#		if results == True:
#			cycles += 1
	print '-'*89
	results = []
	for i in stacks:
		i.sort()
		if i not in results:
			results.append(i)
		print i
	print len(results)
	return cycles

if __name__ == "__main__":
	import sys
	l = sys.argv[1:]
	r = open(l[0],'r').read().split('\n') #TODO: need to make sure that file contents are not corrupt.
	r.remove('')
	print r
	N = r[0]
	graph = create_graph(r[1:])
	print graph
	print find_cycles(graph)
