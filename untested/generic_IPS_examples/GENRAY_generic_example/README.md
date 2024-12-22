# Notes on the GENRAY\_generic\_example

This is a simple example that runs the GENRAY code within the IPS from provided input
files.  GENRAY requires an input namelist file with generic name "genray.dat", and an
input equilibrium EQDSK file.  The example uses the basic\_driver.py and
generic\_component.py instead of a GENRAY specific component.  The input files are
contained in the \_input/genray\_input/ directory.  The names of the namelist and EQDSK
files are specified in the config file.  The input namelist file can have any name and is
copied to the generic name "genray.dat" in the component.  The name of the EQDSK file
appears in the namelist file and the actual filename in the input directory must match
that. This particular example is a single ray ECH case from the GENRAY regresion test
suite: CANONICAL\_2004\_ITER\_TEST\_one\_ray

The full path to the GENRAY executable appears in the env.COMPX\_codes file in
/ips-wrappers/. It presently points to the AToM collection of code binaries on NERSC Cori:

/global/common/software/atom/cori/binaries/genray/m77_CompX/

## There are presently two basic examples here:

1. GENRAY\_basic_example\_EC

This example is a single ray ECH case from the GENRAY regresion test suite:
CANONICAL\_2004\_ITER\_TEST\_one\_ray.  To run it on Cori:

sbatch Cori\_run\_EC

2. GENRAY\_basic\_example\_LH

This example is for inside launch lower hybrid on DIII-D.  To run it on Cori:

sbatch Cori_run_LH
