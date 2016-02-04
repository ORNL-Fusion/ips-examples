# ips-examples

##How to run "ips-hello-world" on edison.nersc.gov

1. Request access to the ATOM project (both on github & at NERSC).
2. Setup your run directory
  
  ```
  cd /project/projectdirs/atom
  mkdir www/$USER
  cd users
  mkdir $USER
  cd $USER
  module load git
  git clone https://github.com/ORNL-Fusion/ips-examples.git
  ```
  
3. Run the example
  
  ```
  cd ips-examples/hello-world
  sbatch batchscript.ips.edison
  squeue -u $USER
  ```

4. After running

  ```
  cat log.stdOut
  ```

5. Look at the web portal for details on your IPS job 
