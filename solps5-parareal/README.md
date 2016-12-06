# Running SOLPS_parareal on Edison within the AToM Environment:

## Running SOLPS standalone

```
tcsh
cd /global/project/projectdirs/atom/users/$USER
mkdir runs
cd runs
cp -r /global/project/projectdirs/atom/users/$USER/ips-examples/solps5-parareal/F_Run .
cd F_Run/Frun_files_DIIID
source ../ips-examples/solps-5-parareal/env.solps.edison.sh
b2run b2mn < input.dat
```

Directories needed in some repository:
SOLPS_bin/F_Run, SOLPS_bin/G_Run, SOLPS_bin/PR_Conv, SOLPS_bin/PR_Corr
(current samples in /global/scratch2/sd/samaddar/IPS_SOLPS/SOLPS_bin)
To start running a test case using IPS:
Files needed in directory where you want to run the simulation (Example:
…../my_solps_ORNL/src/Braams/b2/runs/…../ IPS_SOLPS/RUN_EXAMPLE)
pbs script ("parareal_SOLPS2.pbs”)
 & “SOLPS_parareal2.conf”
Current samples in: /global/scratch2/sd/samaddar/IPS_SOLPS/RUN_EXAMPLE
Stuff to modify for each run:
STEP 1:
In run directory: …../my_solps_ORNL/src/Braams/b2/runs/…../
IPS_SOLPS/RUN_EXAMPLE/
In pbs script ("parareal_SOLPS2.pbs”)
1) Update “IPS Root” path.
2) Update path for “*.conf file” (SOLPS_parareal2.conf) .
STEP 2:
In run directory: …../my_solps_ORNL/src/Braams/b2/runs/…../
IPS_SOLPS/RUN_EXAMPLE/
In SOLPS_parareal2.conf, modify:
1) Update path for IPS_ROOT (path for IPS trunk)
2) Update path for SIM_ROOT (path for simulation run) 
3) Update values of MAX_SLICE & NT_SLICE. Currently set at 32, which means
the parallelization is over 32 time slices. No need to change for testing
purposes.
4) Under [COARSE_SOLPS] :
a. Update path for INPUT_DIR (path for directory … SOLPS_bin /G_Run)
b. Update path for CORRECTION_BIN (path for file
…SOLPS_bin/Pr_Corr/SOLPS_Pr_Corr_V2.sh)
c. Update path for EXECUTABLE (path for file
…SOLPS_bin/G_Run/SOLPS_start_RedGrid_DIIID.sh )
5) Under [FINE_SOLPS] :
a. Update path for INPUT_DIR (path for directory … SOLPS_bin /F_Run)
b. Update path for CORRECTION_BIN (path for file
…SOLPS_bin/Pr_Corr/SOLPS_Pr_Corr_V2.sh)
c. Update path for EXECUTABLE (path for file
…SOLPS_bin/F_Run/SOLPS_start_DIIID.sh )
6) Under [CONVERGE_SOLPS]:
a. Update path for INPUT_DIR (path for directory … SOLPS_bin /F_Run)
b. Update path for CONV_BIN (path for file … SOLPS_bin
/PR_Conv/conv_solps)
STEP 3:
1) In SOLPS_bin/F_Run/: Update paths in SOLPS2_V2.sh &
SOLPS_start_DIIID.sh
2) In SOLPS_bin/G_Run: /: Update paths in SOLPS2_RedGrid_V2.sh &
SOLPS_start_RedGrid_DIIID.sh
3) In SOLPS_bin/PR_Corr/: update path for corr_solps in SOLPS_Pr_Corr_V2.sh
 (not necessary after first time or unless any of the codes are updated)
Note: source code for corr_solps in SOLPS_bin/PR_Corr/src_code_PR_corr 
4) In SOLPS_bin/PR_Conv/ : Nothing to do unless you change the source code
for conv_solps in …/ SOLPS_bin/PR_Conv/src_code_PR_conv/
STEP4: Copy IPS python scripts for SOLPS from
/global/scratch2/sd/samaddar/IPS_SOLPS/scripts_IPS to $IPS_ROOT/bin (not
necessary after first time).
Once all steps 1,2, 3 & 4 are covered, submit pbs script from RUN_EXAMPLE:
qsub parareal_SOLPS2.pbs
Good luck!
Post production:
Parareal produces separate b2time.nc files for SOLPS runs across individual time
slices . The fine calculations generate these files in the format b2time_fine.*k.*pe.nc,
where k=parareal iteration, pe=processor. To combine all the *.nc files into a single
file named b2time.nc, corresponding to a particular iteration, k, one can use the
script: plot_solps_pr.sh
Simple instructions to use the script are given at the beginning of the file. In this
example, simulations across 32 processors are combined at iteration k=4. Before
running script, please make sure the path for ‘nccat’ is correct.
To start a fresh case with new b2fstati, b2mn.dat, etc: Above steps (except step 4)
PLUS
1) Update file contents in SOLPS_bin/F_Run/ & SOLPS_bin/G_Run. Make sure
you have the correct b2yt.dat for the desired grid sizes in
G_Run/base_from_96_36to48_36 & G_Run/base_from_48_36to96_36. 
Notes:
i) The run directory “IPS_SOLPS/RUN_EXAMPLE” should typically have a path
like …/my_solps/src/Braams/b2/runs/…/IPS_SOLPS/RUN_EXAMPLE
because of the way SOLPS is run (or the way I know how to run SOLPS).
Question/comments: Please send me an email at dsamaddar@alaska.edu or
Debasmita.Samaddar@ccfe.ac.uk 
