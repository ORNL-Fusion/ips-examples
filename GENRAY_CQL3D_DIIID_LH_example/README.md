# Brief description
A GENRAY stand alone example that runs GENRAY in the IPS, and that communicates through
the Plasma State.  The case is inside lower hybrid launch in DIII-D.

It uses a new multifrequency version of the rf_genray.py component
that supports both ECH and lower hybrid.  As such it replaces the old rf_genray_EC.py,
rf_genray_LH.py and rf_genray_EC_p.py components.

Nota Bene:  There are fortran executables in the GENRAY wrappers directory (/ips-wrappers/ips-genray)
that must be built after cloning.  Also as of now the config file points to a GENRAY executables
in a CompX user area.

# GENRAY_CQL3D_DIIID_LH_example
An example that couples the ray tracing code GENRAY with the CQL3D Fokker-Planck
code. Thermal profile data communicated through the Plasma State system.  The case is 
inside lower hybrid launch in DIII-D. It uses a new multifrequency version of the 
rf_genray.py component that supports both ECH and lower hybrid.  As such it replaces 
the old rf_genray_EC.py, rf_genray_LH.py and rf_genray_EC_p.py components.

Nota Bene:  There are fortran executables in the IPS wrappers directory that must be built
after cloning, i.e. those in ips-genray, ips-cql3d, and ips-model-epa.


##  Caveat (temporay I expect)
Some of the IPS examples have input files that are big and/or binary and therefore should
not go not the github repo.  Also we don't yet have a maintained collection of physics
executables.  Therefore I'm collecting the inputs and executables for the examples in a
directory in my project area -> /project/projectdirs/atom/users/dbb/IPS_examples_externals
The files for this particular example are in the subdirectory:

/project/projectdirs/atom/users/dbb/IPS_examples_externals/TORLH_CQL3D_KSTAR_example_ext

It's not very satisfactory but until we find a better solution ...
