#Andrew Le
#import random integer generator
from random import randint
import numpy as np
#used for differentiation
from ad import adnumber

#LOCAL SEARCH
def hill_Climb(fxn, xmin, ymin, xmax, ymax):
	print("... execute hill_Climb ... ")
	print("fxn: " ,fxn)
	# get intial values - num_restarts is constant, using derivatives
	NUM_RESTARTS = 1000

	x = randint(xmin, xmax) 
	y = randint(ymin, ymax) 
	# x_theta = adnumber( randint(xmin, xmax) )
	# y_theta = adnumber( randint(ymin, ymax) )
	theta = my_func(x, y)
	theta_new = theta + 1
	ALPHA = 2

	for i in range(0, NUM_RESTARTS):
		thetas = [my_func(x + ALPHA, y), my_func(x, y + ALPHA), my_func(x - ALPHA, y),my_func(x, y - ALPHA)  ]
		direction = max(thetas)
		# theta1 = my_func(x + ALPHA, y) 
		# theta2 = my_func(x, y + ALPHA) 
		# theta3 = my_func(x - ALPHA, y) 
		# theta4 = my_func(x, y - ALPHA) 

		# theta_new = max(theta4, theta3, theta2, theta1, theta)
		# while theta != theta_new:
		# 	theta_x = theta_x - ALPHA*
		# 	theta_y = theta_y - ALPHA

	#ugly brute force method
	# NUM_RESTARTS = 1000

	# for i in range(0, NUM_RESTARTS):
	# 	x = randint(xmin, xmax) 
	# 	y = randint(ymin, ymax) 
	# 	theta = my_func(x, y)
	# 	ALPHA = 1
	# 	theta_new = theta + 1
	# 	print("---begin ascent---")
	# 	while theta_new != theta:
	# 		theta1 = my_func(x + ALPHA, y) 
	# 		theta2 = my_func(x, y + ALPHA) 
	# 		theta3 = my_func(x - ALPHA, y) 
	# 		theta4 = my_func(x, y - ALPHA) 

	# 		theta_new = max(theta4, theta3, theta2, theta1, theta)




#read in input_file and execute function
def main(args, code):

	#initalize given parameters
	xmin = int(sys.argv[2])
	ymin = int(sys.argv[3])
	xmax = int(sys.argv[4])
	ymax = int(sys.argv[5])
	print("===============================")
	code = code.split('\n')
	result = hill_Climb(code[1][8:], xmin, ymin, xmax, ymax)



#import sys package and start the search
if __name__ == '__main__':
	import sys

	#Open file and read in the code from the file 
	i_file_name = str(sys.argv[1])
	i_file_name = str(i_file_name)

	with open(i_file_name, 'r') as i_file:
		code = i_file.read()
	exec(code)

	main(sys.argv[1:], code)
