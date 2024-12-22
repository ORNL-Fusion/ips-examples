# Process SOLPS-ITER Data
This IPS workflow processes SOLPS-ITER data as a first step in the PSI integrated simulation.

Within this workflow, SOLPS data and geometries are processed for:
1. Creating geometries and background plasma profiles for GITR.
2. Producing target plasma profiles for use in hPIC.
3. Making an ion species list for use in F-TRIDYN simulations.
4. Creating a reference coordinate system (R-R_sep) in the plasma state. 

To run this example on Cori, copy the solps-iter_data directory to scratch:
```cp -r solps-iter_data $SCRATCH```

Go to the solps-iter_data folder on scratch
```cd $SCRATCH/solps-iter_data```

Then use the batchscript to submit the job
```sbatch batchscript.ips.cori```

Job status can be checked
```squeue -u your_username```

Output files can be found in the work/plasma_state folder
