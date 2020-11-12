# generic_ABC_example
# 
A reworked version of the *ABC_example* to use the *generic_component.py* for all three
(A,B,C) components. As with the *ABC_example* this example is fully self contained here.
The inputs are located in the *_input* directory and the codes are in *_exec*.  As such it
depends only on the IPS framework and does not require the IPS wrappers repo.  All aspects
of the workflow are specified in the simulation configuration file, all of the components
are generic in that sense.

basic_init.py - Demonstrates copying an input file to a new name and initializing a state
file from a component input file

basic_driver.py - It only initializes and executes the components in a loop in the order
that they appear in the [PORTS] list in the simulation config file.

A_comp - Is fairly busy.  It demonstrates copying files to new names both before and after
the "physics code" runs, and running helper codes both before and after the "physics code"
runs.  The helper codes don't actually do anything though.  It also redirects stdio of the
"physics code" to a named log file.

B_Comp - Is as simple as it gets.  It reads one input file, two state files and writes one
output/state file.

C\_comp - Demonstrates redirecting stdio of the "physics code" to real stdio, which is
equivalent to eliminating the LOGFILE_NAME variable from the config file

## generic_component.py
## 
*generic_component.py* is an IPS component wrapper for the case that the only thing needed
is the staging of input and state files to the work directory, execution of the physics
code, updating of state files and archiving of the output files.  It does no processing of
the input and state files nor processing of the output files or state files which have
been modified by the physics code, except possible copying of input or output files to
more convenient names. In other words it  is useful if the user has in hand, or other
components produce, input files readable by the physics code, and the code output files
can be used as is. It also supports running helper codes before and/or after running the
physics code. The component is generic in that it can, without modification, wrap any
physics code for use with IPS.  It could  also be used as a starting template for a more
general component.  The specification of  all aspects of the component to be implemented
is in the simulation configuration file.  For more details see the docstring in
*generic_component.py* which is found in the *_exec_* directory.


## basic_init.py
## 
*basic_init.py* collects a complete set of initial state files and stages them to the 
/work/state/ directory. It is expanded from the simpler version presently in the
*ABC_simulation* which itself is simplified and adapted from *generic_ps_init.py*, but
eliminating reference to many features specific to plasma physics.  The immediate
application is to simple, example simulations which do not make use of the SWIM Plasma
State system. The SWIM Plasma State need not be used at all, but can be. This version has
more capability than the original *basic_init.py* in that it supports file copying and
running of helper codes.   For more details see the docstring in *basic_init.py* which is
found in the *_exec_* directory.

