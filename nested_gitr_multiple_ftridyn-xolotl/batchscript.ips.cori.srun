#!/bin/bash -l
#SBATCH --account=atom
#SBATCH --partition debug
#SBATCH -C haswell 
#SBATCH --nodes=8
#SBATCH --time=00:30:00
#SBATCH --output=log.slurm.stdOut

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior

# Production
#source /project/projectdirs/atom/atom-install-cori/ips-wrappers/env.ips.cori 
# Devel
#source /project/projectdirs/atom/atom-install-cori/ips-wrappers-devel/env.ips.cori 
# Greendl1
#source /project/projectdirs/atom/users/greendl1/code/ips-wrappers/env.ips.cori
# tyounkin

source $SLURM_SUBMIT_DIR/env.ips.cori #.python3
source $SLURM_SUBMIT_DIR/env.GITR.cori.AL.sh
#source /project/projectdirs/atom/atom-install-cori/GITR/env.cori.sh
#add this to run any python scripts located in submission directory
export PYTHONPATH=$SLURM_SUBMIT_DIR:$PYTHONPATH

module load python/3.7-anaconda-2019.07
#other modules are now loaded in environment files
#module swap PrgEnv-intel PrgEnv-gnu
#module unload cray-netcdf
#module load cray-hdf5-parallel -- already in environment file    

#export OMP_NUM_THREADS=32
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

$IPS_PATH/bin/ips.py --config=ips.parent.conf --platform=conf.ips.cori --log=log.framework 2>>log.stdErr 1>>log.stdOut

egrep -i 'error' log.* > log.errors
./setPermissions.sh
