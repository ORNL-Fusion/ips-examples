# Brief description
A GENRAY stand alone example that runs GENRAY in the IPS, and that communicates through 
the Plasma State.  It uses an update of the long existing rf_genray_EC_p.py component.  
This rf_genray_EC_p.py is an electron cyclotron specific genray component that permits 
programming of multiple launcher powers and aiming angles from the simulation config file.
The example is taken from an ITER simulation done several years ago by Francesca Poli in 
conjunction with TSC.

Nota Bene:  There are fortran executables in the GENRAY wrappers directory (/ips-wrappers/ips-genray)
that must be built after cloning.  Also as of now the config file points to a GENRAY executables
in a CompX user area.
