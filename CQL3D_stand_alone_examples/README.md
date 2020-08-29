# CQL3D Stand Alone IPS Examples

These examples exercise the CQL3D Fokker-Planck code within the IPS simulation system.  They
are set up to run without modification on the Cori computer at NERSC.  The user only needs
to export an environment variable pointing to the IPS installation. e.g.

```export ATOM=/global/common/software/atom/cori```

CQL3D_basic_example and CQL3D_basic_example_pegasus run CQL3D using a set of input files located 
in *_inputs/cql3d_input*
directory.  The component python wrapper is a stripped down version called CQL3D_basic_component.py
which simply stages the input files to the cql3d work directory, launches the CQL3D code,
and stages the output files to the simulation_results directory.  It does not couple to the
Plasma State system or process the input or output files.  The CQL3D_basic_component could
be useful as is when the user has the cql3d input files and makes direct use of the output
files.

The other examples use the full fp_cql3d_general.py wrapper component, which does make use of the Plasma
State system.  It obtains plasma profile data from a plasma state file, updates
a template cql3d input file with current plasma data, runs cql3d with the updated input file,
then processes the cql3d output file to update the plasma state file with the new Fokker-Planck data.
This is the standard CQL3D IPS component that has been used extensively in coupled multi-physics
simulations.

### Details

By default these examples use the IPS framework and component wrappers in the AToM installation
on Cori -> */global/common/software/atom/cori*. So to run the examples the user need only have a
copy of the example directory in their area.  This can be obtained either by copying from the
AToM installation or by cloning the examples from github

```
git clone https://github.com/ORNL-Fusion/ips-examples.git
```

A more advanced user who may be developing or modifying components will need their own copy
of the wrappers to work with and may want to start a separate github branch.  Again this
can be obtained by copying from the installation or cloning from github.


```
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
```

To switch from using the installed wrappers to using a private, local copy it is necessary
to define an environment variable pointing to the users local wrapper directory, e.g.

```export LOCAL_WRAPPER_PATH=<my wrapper directory>```

Also the batch scripts of the examples must source an environment file *use_local_wrappers*.
This only involves uncommenting one line in the slurm batch script.

```
# Uncomment next line to use the local wrappers (e.g for development)
#source $LOCAL_WRAPPER_PATH/use_local_wrappers
```

#### FYI

Although the user should not need to know this:  To access the CQL3D binary the slurm batch
script sources an environment file *env.COMPX_codes*.  The AToM copy of the fortran binary for 
CQL3D resides in */global/common/software/atom/cori/binaries/cql3d/m77_CompX*.



