# Installing IPS
For instructions on installing the IPS see README.md one level up at

https://github.com/ORNL-Fusion/ips-examples 


# Notes on the CQL3D_basic_example
This is a simple example that runs the CQL3D code within the IPS from provided input 
files.  CQL3D requires an input namelist file with generic name "CQL3D.dat", and an
input equilibrium EQDSK file.  The example uses the basic_driver.py and 
CQL3D_basic_component.py components, contained in the _exec/ directory.  The input files
are contained in the _input/CQL3D_input/ directory.  The names of the namelist and EQDSK 
files are specified in the config file.  The input namelist file can have any name and is 
copied to the generic name "CQL3D.dat" in the component.  The name of the EQDSK file 
appears in the namelist file and the actual filename in the input directory must match that.

The full path to the CQL3D executable appears in the config file.  It presently points
to the latest version maintained by Bob Harvey and Yuri Petrov and is subject to change.