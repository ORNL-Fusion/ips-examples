# Notes on the CQL3D\_generic_example
# 
This is a simple example that runs the CQL3D code on NERSC Cori within the IPS from
provided input files.  It is the same as the CQL3D\_basic\_example but here it serves to
demonstrate use of the generic\_component.py

For this example CQL3D requires three input files: cqlinput, rayech, and an input
equilibrium eqdsk file.  The input files are contained in the \_input/CQL3D_input/
directory. The input files correspond to an ECH regression test case
D3D\_96143\_one\_ray/edison\_test

The example uses the basic\_driver.py and the generic\_component.py instead of a CQL3D
specific component. The full path to the CQL3D executable appears in the env.COMPX\_codes
file in /ips-wrappers/. It presently points to the AToM collection of code binaries on
NERSC Cori:

/global/common/software/atom/cori/binaries/cql3d/m77_CompX/
