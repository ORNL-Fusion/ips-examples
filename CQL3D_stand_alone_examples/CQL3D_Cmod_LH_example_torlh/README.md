# Brief description
A CQL3D stand alone example that runs CQL3D in the IPS, and that communicates through the
Plasma State.  It is a rather complicated example that comes from work on iteration of 
TORLH and CQL3D. 

Nota Bene:  There are fortran executables in the CQL3D wrappers directory (/ips-wrappers/ips-cql3d)
that must be built after cloning.  Also as of now the config file points to a CQL3D executable
in a CompX user area.


##  Caveat (temporay I expect)
The input files for this cql3d example are too big to go into github.  Besides which
some of them are binary.  So temporarily I'm moving them to my project area on Edison
/project/projectdirs/atom/users/dbb/cql3d_input.  To run this example you
will need to copy the contents of that directory here.  It's not satisfactory but 
until we find a better solution ...

