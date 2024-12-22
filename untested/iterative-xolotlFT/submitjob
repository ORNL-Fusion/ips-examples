#!/bin/bash -l
#SBATCH --account=m1709
#SBATCH --partition debug
#SBATCH -C haswell
#SBATCH --nodes=2
#SBATCH --time=00:30:00
#SBATCH --output=log.slurm.stdOut

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior

#clean current directory:
if [ -f cleanIpsRun.sh ]; then
   echo "clean up directory"
   ./cleanIpsRun.sh
else
   echo "WARNING: not cleaning up submission directory"
fi

conda activate ftx

module load PrgEnv-intel/6.0.5 intel/19.0.3.199
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/gcc/11.2.0/snos/lib64

export OMP_PLACES=threads
export OMP_PROC_BIND=spread

ips.py --config=ips.ftx.config --platform=conf.ips.cori --log=log.framework 2>>log.stdErr 1>>log.stdOut

egrep -i 'error' log.* > log.errors
./setPermissions.sh
