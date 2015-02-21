
# NON-RECURSIVE
def return_format(width,text_input):
	if width > 0: # XXX: maybe width should be checked to make sure you dont have a string that is greater than the width.
		text_tokens = text_input.split(' ')
		curr_width = 0
		for i in text_tokens:
			if '\n' in i:
				pass
			curr_width += len(i) + 1
			if curr_width <= width:
				print i,
#				curr_width += 1 # for the space
#--			elif curr_width == width:
#				print i,'\n',
#				curr_width = 0
			else:
				print '\n',i,
				curr_width = len(i)
	else:
		# NOTE: can not calculate column must be at lest length 1.
		raise Exception

# RECURSIVE
def r_return_format(width, curr_width, text_input):
	if len(text_input) == 0:
		return
	curr_width += len(text_input)
	text = text_input.pop(0)
	if curr_width < width:
		print text,
		r_return_format( width, curr_width, text_input )
	elif curr_width == width:
		print text,'\n',
		curr_width = 0
		r_return_format( width, curr_width, text_input )
	else:
		print '\n',text,
		curr_width = 0
		r_return_format( width, curr_width, text_input )

# TODO: since all of these files will do the exact same thing just make one module that can do this for all and then pass to a method that will do all the proper formatting for that specific file.
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
	print '-'*width
	return_format( width , s )
	print '-'*width
#	r_return_format(width, 0, lines)
