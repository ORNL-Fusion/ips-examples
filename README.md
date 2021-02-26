# Info for the dbb_ex_new_ips branch
## Install the IPS
Skip this if you've already installed the new version of the IPS.

1. At NERSC Cori there is an installation of the new IPS framework at

   /global/common/software/atom/cori/ips-framework-new/bin
   
   So there is no need to install the new IPS for running on Cori.  For information on installing the your own copy of new IPS version at NERSC see documentation at:
   
   https://ips-framework.readthedocs.io/en/latest/user_guides/nersc_conda.html

2. For information on installing the new IPS version on a local machine see documentation at:
https://ips-framework.readthedocs.io/en/latest/getting_started/getting_started.html

## Clone your own copies of the wrappers and examples repositories
```
mkdir IPS
cd IPS
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```
Checkout the dbb_ex_new_ips and dbb_wr_new_ips branches.  These branches have the modifications needed for the examples using the new IPS package.

```
git checkout dbb_ex_new_ips
git checkout dbb_wr_new_ips
```

## Run examples

1. Source the IPS environemnt
   The environment presently in the /global/common/software/atom/cori//global/common/software/atom/cori/ installation is presently not compatible
   with the new ips package.  So for now you need your own local copys of the wrappers and examples. You will also need to export
   the path to your wrappers and examples in your .bashrc file e.g.
   
```
export LOCAL_WRAPPER_PATH=\<path to your ips-wrappers\>
export LOCAL_EXAMPLES_PATH=\<path to your ips-examples\>
```   

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
