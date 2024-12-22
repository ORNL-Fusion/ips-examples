# Brief description
A GENRAY stand alone example that runs GENRAY in the IPS, and that communicates through
the Plasma State.  The case is inside lower hybrid launch in DIII-D.

It uses a new multifrequency version of the rf_genray.py component
that supports both ECH and lower hybrid.  As such it replaces the old rf_genray_EC.py, 
rf_genray_LH.py and rf_genray_EC_p.py components.  

Nota Bene:  There are fortran executables in the GENRAY wrappers directory (/ips-wrappers/ips-genray)
that must be built after cloning.  Also as of now the config file points to a GENRAY executables
in a CompX user area.

