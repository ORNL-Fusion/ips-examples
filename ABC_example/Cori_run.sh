#!/bin/bash -l
#SBATCH --account=atom
#SBATCH --partition debug
#SBATCH --nodes=1
#SBATCH --time=00:02:00
#SBATCH --output=log.slurm.stdOut
#SBATCH --constraint=haswell

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior

source $IPS_DIR/ips-wrappers/env.ips
which ips.py
ips.py --config=ABC_simulation.config --platform=conf.ips.cori --log=log.framework 2>>log.stdErr 1>>log.stdOut
egrep -i 'error' log.* > log.errors
./setPermissions.sh
