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
