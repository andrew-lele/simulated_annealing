#Andrew Le
#import random integer generator
from random import randint
import numpy as np
#used for differentiation
from ad import adnumber

#LOCAL SEARCH
def hill_Climb(code, xmin, ymin, xmax, ymax):
	print("... execute hill_Climb ... ")
	
	#get intial values - num_restarts is constant
	NUM_RESTARTS = 1000
	x_theta = adnumber( randint(xmin, xmax) )
	y_theta = adnumber( randint(ymin, ymax) )
	x_theta,y_theta = my_func(x_theta.x_theta, y_theta.y_theta)
	ALPHA = 1

	for i in range(0, NUM_RESTARTS):
		theta_x = theta_x - ALPHA
		theta_y = theta_y - ALPHA


#read in input_file and execute function
def main(args):

	#initalize given parameters
	# i_file_name = str(sys.argv[1])
	xmin = int(sys.argv[2])
	ymin = int(sys.argv[3])
	xmax = int(sys.argv[4])
	ymax = int(sys.argv[5])

	# i_file_name = str(i_file_name)
	code = ''
	# with open(i_file_name, 'r') as i_file:
	# 	code = i_file.read()
	# exec(code)
	print(code)
	
	my_func(1,2)
	print("===============================")
	result = hill_Climb(code, xmin, ymin, xmax, ymax)



#import sys package and start the search
if __name__ == '__main__':
	import sys

	#Open file and read in the code from the file 
	i_file_name = str(sys.argv[1])
	i_file_name = str(i_file_name)

	with open(i_file_name, 'r') as i_file:
		code = i_file.read()
	exec(code)

	main(sys.argv[1:])
