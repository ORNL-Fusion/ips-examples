# Install the IPS
Skip this if you've already installed the IPS. 

1. Clone and examples repo.
```
git clone https://github.com/ORNL-Fusion/ips-examples.git
```

# Run the example

1. Source the IPS environment for the (self contained) ABC example 
```
cd ips-examples/ABC_example
source env.ABC_example
```

2. Run the ABC example
  * Locally
```
cd ips-examples/ABC_example
ips.py --simulation=ABC_simulation.config --platform=platform.conf
```
  * On a batch system (e.g., Cori at NERSC)
```
cd $IPS_DIR/ips-examples/ABC_example
sbatch Cori_run

```
To clean all the run files and start with just the input deck run 
```
./cleanIpsRun.sh
```

## Notes on the ABC example
The ABC simulation is a somewhat more realistic example of IPS usage than hello-world.  
But it is completely 
written in python and has no dependencies other than IPS.  As such it should run about 
anywhere, at least it runs on Macs and at NERSC.  The input and output files are all 
human readable text.  It largely has the structure of a real simulation in that it 
has three components that interact. The “simulation” solves a coupled set of 2 ODEs by 
bonehead step-by-step integration.
 
x' = Ax+Bxy

y' = Cy+Dxy

There are 3 “physics”:  codes X_dot_code.py, Y_dot_code.py, and integrator.py. Component
wrapper scripts drive these “physics” codes:  A_component.py, B_component.py, and 
C_component.py.  In addition there are simulation initializer and driver components: 
basic_init.py and basic_driver.py.  The basic_init.py and basic_driver.py components are 
very generic and might well be usable directly in other simple workflows.

The code is in the _exec directory and all of the input data is in the  _input directory.  
Each code has a template input file and produces one output file.  The STATE files consist
output files from the A and B components and a common state.dat file.  It also will send 
the eventlog html file to a www directory.  So it pretty much has the structure of a real 
simulation.

Typically a real simulation would be run as a batch job, submitted via a batch script.  In 
trying to make this as much like a real simulation running as a batch job, a batch script 
for Cori and a shell script for Mac are provided.  The exporting of IPS_DIR and 
sourcing of ips.env are included in these scripts so these two steps described above can 
be omitted.  The command lines to run from the /ips-examples/ABC_example/ directory are 
on Cori
```
sbatch Cori_run
```
and on Mac,
```
./Mac_run 
```
This example also demonstrates simulation restart which is invoked with the Cori_restart
and Mac_restart scripts. 


