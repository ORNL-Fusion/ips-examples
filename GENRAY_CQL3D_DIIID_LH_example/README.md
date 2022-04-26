# GENRAY_CQL3D_DIIID_LH_example
An example that couples the ray tracing code GENRAY with the CQL3D Fokker-Planck
code. Thermal profile data communicated through the Plasma State system.  The case is 
inside lower hybrid launch in DIII-D. It uses a new multifrequency version of the 
rf_genray.py component that supports both ECH and lower hybrid.  As such it replaces 
the old rf_genray_EC.py, rf_genray_LH.py and rf_genray_EC_p.py components.

Nota Bene:  There are fortran executables in the IPS wrappers directory that must be built
after cloning, i.e. those in ips-genray, ips-cql3d, and ips-model-epa.


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

Although the user should not need to know this:  To access the GENRAY and CQL3D binaries 
the slurm batch script sources an environment file *env.COMPX_codes*.  The AToM copy of 
the fortran binaries reside in:

GENRAY ->  */global/common/software/atom/cori/binaries/genray/m77_CompX*.

CQL3D ->  */global/common/software/atom/cori/binaries/cql3d/m77_CompX*.

The input files for this example are located on Cori in a collection of input data for 
IPS examples:


```
/global/common/software/atom/cori/examples_input_data