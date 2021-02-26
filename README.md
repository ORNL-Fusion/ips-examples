# Info for the dbb_ex_new_ips branch
## Install the IPS
Skip this if you've already installed the new version of the IPS.

1. At NERSC Cori there is an installation of the new IPS framework at

   /global/common/software/atom/cori/ips-framework-new/bin
   
   So there is no need to install the new IPS for running on Cori.

For information on installing the your own copy of new IPS version at NERSC see documentation at:
https://ips-framework.readthedocs.io/en/latest/user_guides/nersc_conda.html

2. For information on installing the new IPS version on a local machine see documentation at:
https://ips-framework.readthedocs.io/en/latest/getting_started/getting_started.html

## Run examples

1. Source the IPS environemnt


2. Run the ABC example
  * Locally
```
cd ips-examples/ABC_example
ips.py --simulation=ABC_simulation.config --platform=platform.conf
```
  * On a batch system (e.g., Cori at NERSC)
```
cd ips-examples/ABC_example
sbatch Cori_run
```
To clean all the run files and start with just the input deck run
```
./cleanIpsRun.sh
```
