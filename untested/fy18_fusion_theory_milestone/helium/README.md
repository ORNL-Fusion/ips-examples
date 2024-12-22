# FY18 Fusion Theory Milestone
This IPS workflow is the plasma-surface interaction integrated workflow.
Helium and D-T simulations are both part of these examples.

This workflow is currently underconstruction.
## Step 1 - Run SOLPS for the given case
As part one of the integrated workflow, SOLPS is used to simulate the scrape-off layer plasma.
Jeremy Lore (lorejd@ornl.gov) is the point of contact for such simulations as part of the Plasma-Surface Interactiosn SciDAC.
Four files which are a part of the input/output of SOLPS are utilized in this integrated simulation:
1. mesh.extra.iter - this is a mesh file used to prescribe the material boundary of the simulation away from the magnetically connected target.
2. b2fgmtry - describes the B2 mesh which containts the plasma solution.
3. b2fstate - stores the B2 solution.
4. some_file.equ - magnetic equilibrium file mapping magnetic flux used as input to the SOLPS simulation.

These files should be placed in a location which can be pointed to using the SOLPS_DATA_PATH environment variable (set in the proper environment file.

Things to set in the IPS config file should also go here? Relevant settings?

## Step 2 - Process SOLPS data for downstream components
Within this workflow, SOLPS data and geometries are processed for:
1. Creating geometries and background plasma profiles for GITR.
2. Producing target plasma profiles for use in hPIC.
3. Making an ion species list for use in F-TRIDYN simulations.
4. Creating a reference coordinate system (R-R_sep) in the plasma state.

Specific instructions on how to process SOLPS data ahead of time which is needed for hPIC setup/execution.

## Step 3 - Run hPIC for the given case
As part one of the integrated workflow, hPIC is used to simulate the ion energy-angle distributions of the background plasma species at the divertor target.
Davide Curreli (dcurreli@illinois.edu) is the point of contact for such simulations as part of the Plasma-Surface Interactiosn SciDAC.
Output data from hPIC which is utilized in this integrated simulation include three files per plasma ion species per location:
1. some_file_IEAD.dat - this is a 2D histogram (in energy and angle) of the ion distribution function at the target.
2. some_file_AngleCenters.dat - describes the angle dimension of the 2D histogram.
3. some_file_EnergyCenters.dat - describes the energy dimension of the 2D histogram.

These files should be placed in a location which can be pointed to using the HPIC_DATA_PATH environment variable (set in the proper environment file.

Things to set in the IPS config file should also go here? Relevant settings?
## Step 4 Configure IPS Config File
Configuration of the IPS Config File (ips.config) will determine how exactly the simulation is run.
### SOLPS
Although execution of SOLPS is currently external to the integrated simulation, the processing and utilization of this data can be determined by several input parameters in the config file.
Which fields and what do they do?
### F-TRIDYN
Which fields and what do they do?
### hPIC
### GITR

## Step 5 Run the workflow
1. From the helium or DT example folder, source the anaconda environment and environment file
```source $CODE_PATH/env/bin/activate```
```source ../env/env.ips3.cori```

2. Run the workflow
```python3 $IPS_DIR/bin/ips.py --simulation=ips.config --platform=conf.ips.cori```

# Notes

On Cori the batchscript to submit the job
```sbatch batchscript.ips.cori```

Job status can be checked
```squeue -u your_username```

Output files can be found in the work/plasma_state folder
