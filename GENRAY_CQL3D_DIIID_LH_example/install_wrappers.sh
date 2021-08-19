#!/bin/bash
# This will install a series of wrappers into your current conda environment

# To create a new environment look at https://ips-framework.readthedocs.io/en/latest/user_guides/nersc_conda.html
#
# Or run the following:
# > module load python/3.7-anaconda-2019.10
# > conda create -n my_ips_env --clone base
# > source activate my_ips_env
#
#
# After which the run_slurm script should be updated to use this new environment with
# > source activate my_ips_env

# These wrapper binary components will only build on cori with `module load cray-netcdf`
module load cray-netcdf

# Assume that ips-examples exist at same level as ips-wrapper
IPS_WRAPPER_PATH=$PWD/../../ips-wrappers

cd $IPS_WRAPPER_PATH/utilities
python -m pip install .

cd $IPS_WRAPPER_PATH/initializers/ips_initializers/generic_ps_init
make
make DESTDIR=$CONDA_PREFIX install
cd $IPS_WRAPPER_PATH/initializers
python -m pip install .

cd $IPS_WRAPPER_PATH/generic-drivers
python -m pip install .

cd $IPS_WRAPPER_PATH/ips-model-epa
make
make DESTDIR=$CONDA_PREFIX install
python -m pip install .

cd $IPS_WRAPPER_PATH/ips-genray
make
make DESTDIR=$CONDA_PREFIX install
python -m pip install .

cd $IPS_WRAPPER_PATH/ips-cql3d
make
make DESTDIR=$CONDA_PREFIX install
python -m pip install .

cd $IPS_WRAPPER_PATH/ips-model-rf
make
make DESTDIR=$CONDA_PREFIX install

cd $IPS_WRAPPER_PATH/ips-monitor
python -m pip install .
