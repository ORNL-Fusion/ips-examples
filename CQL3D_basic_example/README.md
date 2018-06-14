# Installing IPS
For instructions on installing the IPS see README.md one level up at

https://github.com/ORNL-Fusion/ips-examples 


# Notes on the CQL3D_basic_example
This is a simple example that runs the CQL3D code on NERSC Edison within the IPS from 
provided input files.  

For this example CQL3D requires three input files: cqlinput, rayech, and an
input equilibrium eqdsk file.  The input files are contained in the _input/CQL3D_input/ 
directory. The input files correspond to an ECH regression test case D3D_96143_one_ray/edison_test

The example uses the basic_driver.py and CQL3D_basic_component.py components, 
which are contained in the _exec/ directory. The full path to the CQL3D executable appears 
in the config file.  It presently points to the latest version on NERSC Edison maintained 
by Bob Harvey and Yuri Petrov and is subject to change.

