#!/bin/bash -l
#SBATCH --account=atom
#SBATCH --partition regular
#SBATCH --nodes=2
#SBATCH --time=3:00:00
#SBATCH --output=log.slurm.stdOut

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior

# Production
#source /project/projectdirs/atom/atom-install-edison/ips-wrappers/env.ips.edison 
# Devel
#source /project/projectdirs/atom/atom-install-edison/ips-wrappers-devel/env.ips.edison 
# Greendl1
#source /project/projectdirs/atom/users/greendl1/code/ips-wrappers/env.ips.edison 
# tyounkin
source /project/projectdirs/atom/users/tyounkin/ips-examples/ftridyn_ea_task_pool/env.ips.edison

export OMPI_ROOT=/project/projectdirs/atom/users/elwasif/ompi/install_4.0
export PATH=$OMPI_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$OMPI_ROOT/lib64:$LD_LIBRARY_PATH
export MANPATH=$OMPI_ROOT/share/man:$MANPATH

#orte-dvm --daemonize --report-uri ./dvm_uri
unset ORTE_HNP_DVM_URI
orte-dvm  --debug-daemons --report-uri ./dvm_uri.$$ &
sleep 5
export ORTE_HNP_DVM_URI=$(cat ./dvm_uri.$$)
echo  $ORTE_HNP_DVM_URI
sleep 5
mpirun -np 5 hostname
sleep 5
which mpirun
#$IPS_PATH/bin/ips.py --config=ips.config --platform=edison_ompi.conf --log=log.framework 2>>log.stdErr 1>>log.stdOut
$IPS_PATH/bin/ips.py --config=ips.config --platform=edison_ompi.conf --log=log.framework 2>>log.stdErr 1>>log.stdOut
egrep -i 'error' log.* > log.errors
./setPermissions.sh

