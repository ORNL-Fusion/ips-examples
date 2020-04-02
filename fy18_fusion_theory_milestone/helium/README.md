# FY18 Fusion Theory Milestone
This IPS workflow is the plasma-surface interaction integrated workflow.
Helium and D-T simulations are both part of these examples.

This workflow is currently underconstruction.
As part one of the integrated workflow, SOLPS is used to simulate the scrape-off layer plasma.
Details about that go here.

Step two is to process SOLPS data for downstream components.
Within this workflow, SOLPS data and geometries are processed for:
1. Creating geometries and background plasma profiles for GITR.
2. Producing target plasma profiles for use in hPIC.
3. Making an ion species list for use in F-TRIDYN simulations.
4. Creating a reference coordinate system (R-R_sep) in the plasma state. 

# Run the workflow
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
