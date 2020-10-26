# Brief description
A TORIC stand alone example that runs TORIC in the IPS, and that communicates through 
the Plasma State.  The example is taken from an ITER simulation done several years ago by 
Francesca Poli in conjunction with TSC.  It uses the rf_ic_toric_abr_mcmd.py.py component
to wrap TORIC. The plasma data is initialized using the generic_ps_init.py component.
The plasma profiles are provided in an existing plasma state file.  The MHD equilibrium 
eqdsk file is generated from the plasma state file using a Plasma State function ps_wr_geqdsk. 


Nota Bene:  There are fortran executables in the TORIC wrappers directory (/ips-wrappers/ips-toric)
that must be built after cloning.

