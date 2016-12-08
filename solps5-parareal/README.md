# Running SOLPS_parareal on Edison within the AToM Environment:
```
cd solps5-parareal
sbatch batchscript.ips.edison
```
##User notes


## Running SOLPS standalone
```
tcsh
cd /global/project/projectdirs/atom/users/$USER
mkdir runs
cd runs
cp -r /global/project/projectdirs/atom/users/$USER/ips-examples/solps5-parareal/F_Run .
cd F_Run/Frun_files_DIIID
source ../../../ips-examples/solps5-parareal/env.solps.edison.sh
../../../ips-examples/solps5-parareal/correctTimestamps5.sh
b2run b2mn < input.dat
```
