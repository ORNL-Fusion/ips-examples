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
  RF_IC step
  model_RF_IC_3.step() called
  Executing  ['/project/projectdirs/atom/users/greendl1/code/ips-wrappers/ips-model-rf/model_RF_IC_3', 'ips-state.nc', 'STEP', '10.000']
  RM: get_allocation() returned %s (True, ['nid00026'], [('nid00026', ['0:0'])], 1, 24, True)
  build_launch_cmd( 1 /project/projectdirs/atom/users/greendl1/code/ips-wrappers/ips-model-rf/model_RF_IC_3 ('ips-state.nc', 'ips-eqdsk.geq', 'ips-cql.dat', 'ips-dql.nc', 'STEP', '10.000') 1 24 nid00026 True True )
  in wait task
  
   model_RF_IC
   cur_state_file = ips-state.nc
   cur_eqdsk_file = ips-eqdsk.geq
   cur_cql_file = ips-cql.dat
   cur_dql_file = ips-dql.nc
   mode = STEP
   time_stamp = 10.000
    ps_init_tag: Plasma State v2.041 f90 module initialization.
  
   model_RF_IC: STEP
   power_ic(           1 ) =    20000000.0000000
   SUM(ps%picrf_totals(:, 0)) =    1000000.00000000
   SUM(ps%picrf_totals(:,           1 )) =    500000.000000000
   SUM(ps%picrf_totals(:,           2 )) =    500000.000000000
   SUM(ps%picth(:)) =   1000000.000000000
    *ps_update_file_write: normal exit,            0  update elements written.
   model_RF_IC_2: Stored Partial RF Plasma State
  ```

3. Visualize your IPS job on the portal 

  ![IPS portal image 1](https://github.com/ORNL-Fusion/ips-examples/blob/master/sequential-model-simulation/images/portal1.png)
  
  Click on your job
  
  ![IPS portal image 2](https://github.com/ORNL-Fusion/ips-examples/blob/master/sequential-model-simulation/images/portal2.png)
  
  Click on "View Data With Web Graphics"
  
  ![IPS portal image 3](https://github.com/ORNL-Fusion/ips-examples/blob/master/sequential-model-simulation/images/portal3.png)

4. Restart from the 10th step
  Edit the following sections in the `ips.config` file from 
  ```
  SIMULATION_MODE = NORMAL
  ```
  to
  ```
  SIMULATION_MODE = RESTART
  ```
  and (near the very bottom of `ips.config`) change
  ```
  [TIME_LOOP]
    MODE = REGULAR
    START = 10.
    FINISH = 20.
    NSTEP = 10
  ```
  to
  ```
    [TIME_LOOP]
    MODE = REGULAR
    START = $RESTART_TIME
    FINISH = 20.
    NSTEP = 10
  ```
