def return_format(width,text_input):
	if width > 0:
		text_tokens = text_input.split(' ')
		curr_width = 0
		for i in text_tokens:
			if '\n' in i:
				pass
			curr_width += len(i) + 1
			if curr_width <= width:
				print i,
			else:
				print '\n',i,
				curr_width = len(i)
	else:
		# NOTE: can not calculate column must be at lest length 1.
		print "width is to small for this file!!!"
		raise Exception

if __name__ == "__main__":
	import sys
	l = sys.argv[1:]
	# TODO: add checker for the correct conditions
	r = open(l[0],'r').readlines()
	width = int(r[0].replace('\n',''))
	lines = r[1:]
	print 'lines = ',lines
	s = ""
	for i in lines:
		s += i
	# print '-'*width
	return_format( width , s )
	# print '-'*width
