#! /usr/bin/env python

"""
generic_X_dot_code.py 3/10/2018 (Batchelor)
A simple "physics" code which in a real application would typically be
a massively parallel code, and which likely was written as a stand-alone
with no thought of coupling to other codes.  The philosopy of the IPS is
to not require any modification of the "physics" code's usual I/O.

What it does is to calculate X_dot for the 2D system of ODEs:
X_dot = a_lin*X + b_nonlin*X*Y
Y_dot = c_lin*Y + d_nonlin*X*Y
Writes X_dot into file "X_code.out"

This code reads two input files "X_dot_code.in" and "integrator.out"
X_dot_code.in contains parameters of the ODE a_lin and b_nonlin, a surrogate for
all the namelists and input input files a serious code might need.
integrator.out contains X and Y, the evolving solution of the ODE which is the state
data needed to calculate X_dot.

The prefix "generic" refers to the fact that this code just reads raw input files with no
translation in and out of any common data format state file such as Plasma State.  This 
distinguishes it from the ABC_simulation which endeavors to mimic a situation using a 
common data format state file.

"""
import time
import utils.simple_assignment_file_edit as edit

print('generic_X_dot_code Running ')

# Get static data from input file
data_dict = edit.input_file_to_variable_dict('X_dot_code.in')
a_lin = float(data_dict['a_lin'])
b_nonlin = float(data_dict['b_nonlin'])

# Get state data from integrator.out file
data_dict = edit.input_file_to_variable_dict('integrator.out')
X = float(data_dict['X'])
Y = float(data_dict['Y'])

# Do big calculation

X_dot = a_lin * X + b_nonlin * X * Y
time.sleep(2)  # Wait a few seconds to pretend to be doing something.

# Write data to output file
variable_dict = {'X_dot': X_dot}
edit.variable_dict_to_output_file(variable_dict, 'X_dot_code.out')

# That's all folks
