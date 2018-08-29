# Installing IPS
For instructions on installing the IPS see README.md one level up at

https://github.com/ORNL-Fusion/ips-examples 


# Notes on the GENRAY_basic_example
This is a simple example that runs the GENRAY code within the IPS from provided input 
files.  GENRAY requires an input namelist file with generic name "genray.dat", and an
input equilibrium EQDSK file.  The example uses the basic_driver.py and 
GENRAY_basic_component.py components, contained in the _exec/ directory.  The input files
are contained in the _input/genray_input/ directory.  The names of the namelist and EQDSK 
files are specified in the config file.  The input namelist file can have any name and is 
copied to the generic name "genray.dat" in the component.  The name of the EQDSK file 
appears in the namelist file and the actual filename in the input directory must match that.
This particular example is a single ray ECH case from the GENRAY regresion test suite:
CANONICAL_2004_ITER_TEST_one_ray

The full path to the GENRAY executable appears in the config file.  It presently points
to the latest version maintained by Bob Harvey and Yuri Petrov and is subject to change.

# Thre are presently two basic examples here

1. GENRAY_basic_example_EC
_
This example is a single ray ECH case from the GENRAY regresion test suite:
CANONICAL_2004_ITER_TEST_one_ray.  To run it on Edison:

sbatch Edison_run_EC

2. GENRAY_basic_example_LH

This example is for inside launch lower hybrid on DIII-D.  To run it on Edison:

sbatch Edison_run_EC
