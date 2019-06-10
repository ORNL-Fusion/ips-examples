#! /usr/bin/env python

"""
integrator.py 3/10/2018 (Batchelor)
A simple "physics" code which in a real application would typically be a massively 
parallel code, and which likely was written as a stand-alone with no thought of coupling 
to other codes.  The philosopy of the IPS is to not require any modification of the 
"physics" code's usual I/O.  

This code reads one input file "integrator.in" which is a surrogate for all the namelists and input
input files a serious code might need.  What it actually does is to calculate Y_dot for the 2D
system of ODEs:
X_dot = a_lin*X + b_nonlin*X*Y
Y_dot = c_lin*Y + d_nonlin*X*Y
Writes Y_dot into file "integrator.out"
"""
import sys
import os
import subprocess
import utils.simple_assignment_file_edit as edit

print('integrator Running')

# Get data from input file

data_dict = edit.input_file_to_variable_dict('integrator.in')
delta_t = float(data_dict['delta_t'])
X_in = float(data_dict['X'])
Y_in = float(data_dict['Y'])
X_dot = float(data_dict['X_dot'])
Y_dot = float(data_dict['Y_dot'])
print('delta_t = ', delta_t, ' X_in = ', X_in, ' Y_in = ', Y_in, ' X_dot = ', X_dot, ' Y_dot = ', Y_dot)

# Do big calculation

X = X_in + X_dot*delta_t
Y = Y_in + Y_dot*delta_t

# Write data to output file
variable_dict = {'X' : X, 'Y' : Y}
edit.variable_dict_to_output_file(variable_dict, 'integrator.out')

print(' X = ', X, ' Y = ', Y)

# That's all folks