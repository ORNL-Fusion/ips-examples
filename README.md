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

4. After running, successful output looks like ...

  ```
  cat log.stdOut
  ...
  Starting IPS
  Created <class 'hello_driver.hello_driver'>
  Created <class 'hello_worker.hello_worker'>
  Created <class 'runspaceInitComponent.runspaceInitComponent'>
  [('nid01590', 24)] 24 2 24 True
  Checklist config file "/global/project/projectdirs/atom/users/greendl1/runs/ips-examples/hello-world/checklist.conf" could not be found, continuing without.
  runspaceInitComponent.init() called
  CREATE_RUNSPACE = DONE
  RUN_SETUP = DONE
  RUN = DONE
  runspaceInitComponent.step() called
  hello_driver: beginning step call
  Hello from hello_worker
  runspaceInitComponent.finalize() called
  HelloDriver: finished worker call
  ```

5. Look at the web portal for details on your IPS job 
