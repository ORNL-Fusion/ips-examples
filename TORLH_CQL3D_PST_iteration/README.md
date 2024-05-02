# TORLH_CQL3D_PST_iteration IPS Example

This README is adapted from
README - TORLH/CQL3D IPS Iterative Solver
AUTHOR - SAM FRANK - frank@psfc.mit.edu
DATE   - 07/2021

This example exercises the TORLH/CQL3D Iterative solver
utilizing the ATOM IPS wrappers. Currently the solver is set up for the toy
problem Princeton Small Torus or "PST". This case can be fully converged at low
resolutions making it ideal for debugging the IPS driven TORLH CQL3D iterations.
This case needs 504 processors to run the TORLH field solve optimally. This
means on cori you should run this case using following slurm parameters:

NODES = 16
CONSTRAINT = HASWELL

The example is set up to run without modification on the Cori computer at NERSC.  The user
only needs to export an environment variable pointing to the IPS installation. e.g.

```export ATOM=/global/common/software/atom/cori```

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


Executables needed for this case are:

TORLH - Ptoric.e (TORLH executable file) and imchzz (Im[Chi_zz]
These are located in the AToM physics binary collection /global/common/software/atom/cori/binaries/
Specifically in /global/common/software/atom/cori/binaries/torlh/SFRANK_7_20_2021. The Executables
are accessed by sourcing env.TORLH_binary in the simulation config file


CQL3D - xcql3d_mpi_intel.cori (CQL3D executable) and cql3d_mapin 
These are located in /global/common/software/atom/cori/binaries/cql3d/m77_CompX and are also
accessed by sourcing env.COMPX_codes in the batch script.

Additionally  -geqxpl is needed (for making equigs metric coefficients file)  located at
/project/projectdirs/atom/atom-install-edison/binaries/geqxpl/default/

Input files used in this case, located in the /_inputs/ directory here are the following:

_inputs/generic_ps_file_init_inputs/
	-Cmod_torlh.sconfig (RF source data not really used but important for
			    any future coupling of TORLH/CQL3D model to other
			    models)
	-g files or eqdsk files for given shot
_inputs/model_EPA_mdescr_input/
	-model_EPA_mdescr_input.nml (plasma profiles for plasma state model)
_inputs/torlh_input/
	-machine.inp (TORLH input file template)
	-equigs_gen.ind (geqxpl inputs)
	-Chizz_interp.inp (dummy input needed for imchzz table interpolation)
_inputs/cql3d_input
	-cqlinput_template (CQL3D input file template)
	-grfont.dat (font data for CQL3D outputs)
	-ImChizz.inp_template (template for nonmax imchzz formulation exec)


