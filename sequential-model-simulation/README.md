## ips-sequential-model-simulation (with restart)
Here "sequential" refers to each component being run sequentially, as opposed to 
concurrently, which will be dealt with in another example.
This model simulation is intended to look almost like a real simulation, short of 
requiring actual physics codes and input data.  Instead typical simulation-like data is 
generated from simple analytic (physics-less) models for most of the quantities that are 
assembled into time series by the MONITOR component.  It includes time stepping, 
time varying scalars and profiles, and checkpoint/restart. And inportantly it gives a
simple demonstration of coupling of components using the SWIM Plasma State framework.

The PORTS (i.e. components) that exercised are:
Simulation initialization = INIT  generic_ps_init.py
Driver = DRIVER - generic_driver.py
Equilibrium and profile advance = EPA - model_epa_ps_file_init.py
Ion cyclotron heating = RF_IC - model_RF_IC_2_mcmd.py
Neutral beam heating = NB - model_NB_2_mcmd.py
Fusion heating and reaction products = FUS - model_FUS_2_mcmd.py
Simulation time history monitoring = MONITOR -  monitor_comp.py

The driver and monitor components are full components as used in many of the real 
simulations.  In this case the driver is generic_driver.py, which implements a simple 
time stepping workflow using any mixture of eight specific physics components.  The other 
components are simple analytic models, with parameters that can be modified in the component 
input data files.  

The batch script, run_slurm, sources an environment file, env.ips.edison which provides
paths to the IPS framework and to the component scripts and wrapper codes.The environment 
file env.ips.edison is maintained at:

/project/projectdirs/atom/atom-install-edison/ips-wrappers/env.ips.edison

The python components and fortran source files that implement the model 
components reside in the AToM project WRAPPERS directory as defined in 
env.ips.edison, but they have been copied here into the source directory for ease of 
viewing by the user.

N.B. David Green- The wrappers currently points to my dbb_dev branch which has stuff to
be merged into master.

The model (physics-less) components require input data files that describe the models that
are exercised.  These have been placed in this  simulation run directory in _inputs/.

To run the "simulation" submit the batch script from the command line

$ sbatch run_slurm

In order to demonstrate the restart capability there is also a batch script and config
file this will restart from the end of the first simulation (to 10 sec simulation time) 
and run on out to 15 sec.  To do this, from the command line do

$ sbatch restart_slurm
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

   Portal is gone.  Need to write something about the www directory and html.file

4. Restart from the 10th (latest) step
  Edit the following sections in the `ips.config` file from 
  ```
  SIMULATION_MODE = NORMAL
  ```
  to
  ```
  SIMULATION_MODE = RESTART
  ```
  **and** (near the very bottom of `ips.config`) change
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
  and then run with
  ```
  sbatch batchscript.ips.edison
  squeue -u $USER
  ```


This model simulation is intended to look almost like a real simulation, short of 
requiring actual physics codes and input data.  Instead typical simulation-like data is 
generated from simple analytic (physics-less) models for most of the quantities that are 
assembled into time series by the MONITOR component.  It includes time stepping, 
time varying scalars and profiles, and checkpoint/restart.

The PORTS <==> components that exercised are:
Simulation initialization = INIT  minimal_state_init.py
Driver = DRIVER - generic_driver.py
Equilibrium and profile advance = EPA - model_epa_ps_file_init.py
Ion cyclotron heating = RF_IC - model_RF_IC_2_mcmd.py
Neutral beam heating = NB - model_NB_2_mcmd.py
Fusion heating and reaction products = FUS - model_FUS_2_mcmd.py
Simulation time history monitoring = MONITOR -  monitor_comp.py

The driver and monitor components are full components as used in many of the real 
simulations.  In this case the driver is generic_driver.py, which implements a simple 
time stepping workflow using any mixture of eight specific physics components.  The other 
components are simple models, with parameters that can be modified in the component 
input data files.  

The batch script, run_slurm, sources an environment file, env.ips.edison which provides
paths to the IPS framework and to the component scripts and wrapper codes.The environment 
file env.ips.edison is maintained at:

/project/projectdirs/atom/atom-install-edison/ips-wrappers/env.ips.edison

The python components and fortran source files that implement the model 
components reside in the AToM project IPS_CSWIM_WRAPPERS directory as defined in 
env.ips.edison, but they have been copied here into the source directory for ease of 
viewing by the user.

The model (physics-less) components require input data files that describe the models that
are exercised.  These have been placed in this  simulation run directory in _inputs/.

To run the "simulation" submit the batch script from the command line

$ sbatch run_slurm

In order to demonstrate the restart capability there is also a batch script and config
file this will restart from the end of the first simulation (to 10 sec simulation time) 
and run on out to 15 sec.  To do this, from the command line do

$ sbatch restart_slurm
