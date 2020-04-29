#!/bin/bash -l
#SBATCH --account=m1709
#SBATCH --partition debug
#SBATCH --nodes=1
#SBATCH --time=00:30:00
#SBATCH --output=log.slurm.stdOut
#SBATCH --constraint=haswell

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior

source /project/projectdirs/m1709/psi-install-cori/env/bin/activate
source /project/projectdirs/m1709/psi-install-cori/ips-examples/fy18_fusion_theory_milestone/env/env.ips3.cori

python3 $IPS_DIR/bin/ips.py --simulation=ips.config --platform=conf.ips.cori --log=log.framework 2>>log.stdErr 1>>log.stdOut

egrep -i 'error' log.* > log.errors

./setPermissions.sh
