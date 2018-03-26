#Andrew Le


#read in input_file and execute function

def main(args):
	i_file_name = str(sys.argv[1])
	i_file_name = str(i_file_name)
	code = ''
	try:
		i_file = open(i_file_name, 'r')
		code = i_file.read()
		
	except:
		print('input_error %s')
		sys.exit(2)
	exec(code)



if __name__ == '__main__':
	import sys
	main(sys.argv[1:])
