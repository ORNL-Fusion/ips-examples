# ips-examples

How to run ips-hello-world on edison.nersc.gov

1. Request access to the ATOM project.
2. Setup your run directory
```
cd /project/projectdirs/atom/users
mkdir $USER
cd $USER
module load git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```
3. Run the example
```
cd ips-hello-world
sbatch batchscript.ips.edison
```
