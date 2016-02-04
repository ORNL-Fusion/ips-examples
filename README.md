# ips-examples  on edison.nersc.gov

##ips-hello-world

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

5. Look at the web portal for details on your IPS job [http://swim.gat.com:5050/](http://swim.gat.com:5050/)

  ![IPS Portal Image](https://github.com/ORNL-Fusion/ips-examples/blob/master/hello-world/portal-image.png)
  
## ips-sequential-model-simulation (with restart)
Here "sequential" refers to each component being run sequentially, as opposed to concurrently, which will be dealt with in the next example.

1. Run the example for 10 time steps
  
  ```
  cd ips-examples/sequential-model-simulation
  sbatch batchscript.ips.edison
  squeue -u $USER
  ```

2. After running, successful completion looks like ...

  ```
  cat log.stdOut
  ...
  ```

3. Visualize your IPS job on the portal 

  ![IPS portal image 1](https://github.com/ORNL-Fusion/ips-examples/blob/master/sequential-model-simulation/images/portal1.png)
  
  Click on your job
  
  ![IPS portal image 2](https://github.com/ORNL-Fusion/ips-examples/blob/master/sequential-model-simulation/images/portal2.png)
  
  Click on "View with web graphics"
  
  ![IPS portal image 3](https://github.com/ORNL-Fusion/ips-examples/blob/master/sequential-model-simulation/images/portal3.png)
