# Brief description
A CQL3D stand alone example that runs CQL3D in the IPS, and that communicates through the
Plasma State.  It is a rather complicated example that comes from work on iteration of
TORLH and CQL3D.

Nota Bene:  There are fortran executables in the CQL3D wrappers directory (/ips-wrappers/ips-cql3d)
that must be built after cloning.


##  Caveat (temporay I expect)
Some of the IPS examples have input files that are big and/or binary and therefore should 
not go not the github repo.  Also we don't yet have a maintained collection of physics 
executables.  Therefore I'm collecting the inputs and executables for the examples in a
directory in my project area -> /project/projectdirs/atom/users/dbb/IPS_examples_externals
The files for this particular example are in the subdirectory:

/project/projectdirs/atom/users/dbb/IPS_examples_externals/CQL3D_Cmod_LH_example_torlh_ext

It's not very satisfactory but until we find a better solution ...
