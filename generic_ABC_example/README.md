# generic_component.py

A simple IPS component wrapper for the case that the only thing needed is the staging
of input and state files to the work directory, execution of the physics code, and updating 
of state files and archiving of the output files.  It does no processing of the input and
state files nor processing of the output files and state files which have been modified by
the physics code.  In other words it is useful if the user has in hand, or other components
produce, input files readable by the physics code, and the code output files can be used 
as is.  The component is generic in that it can, without modification, wrap any physics 
code for use with IPS.  It could also be used as a starting template for a more general 
component.  The specification of all aspects of the component to be implemented occurs in 
the simulation configuration file.


# generic_ABC_example
 
 
A reworked version of the ABC_example to use this generic_component.py for all three (A,B,C)
components. As with the ABC_example this example fully self contained here.  The inputs are
located in the *_input* directory and the codes are in *_exec*.  As such it depends only 
on the IPS framework and does not require the IPS wrappers repo.