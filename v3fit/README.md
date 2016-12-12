# IPS-V3FIT Example

Example use cases for the ips-v3fit components. This contains two example cases.
* ips.v3post.config Is work flow where VMEC generates a wout file that is used by v3fit.
* ips.v3fit.config  Just runs a reconstruction in the ips framework.

## List of Files
* ips.v3post.config V3POST work flow configuration file.
* ips.v3fir.config V3FIT work flow configuration file.
* platform.conf Configuration file for the local machine.
* input.test.vmec VMEC namelist input file.
* input.test.v3fit V3FIT namelist input file.
* intpol.dot Interferometry/Polarimetry diagnostics discription.
* sxrem.dot Soft X-ray diagnostics discription.
* thomson.dot Thomson scattering diagnostics discription.


## Requirements
* vmec or parvmec and v3fit
* The IPS vmec component.
* The IPS vmec_init component.
* The IPS v3fit component.
* The IPS v3fit_init component.
* The IPS v3post_driver driver.
* The IPS v3fit_driver driver.

## Running Locally

To run this example work flow on a local machine, the user needs to provide a
platform config file or configure the provided platform.conf file.

### Platform Configuration File

To configure the platform configuration file, change the

* IPS_PATH
* HOST
* USER
* HOME
* CORES_PER_NODE
* SOCKETS_PER_NODE

values to the equivalents for your local machine. Alternatively, the user can 
also subsitute the provided platform file with the one provided by the IPS 
framework in the share directory.

The ips-3fit components require definitions for the following variables.

* IPS_VMEC_COMP_PATH Path to the ips-vmec scripts.
* VMEC_INSTALL_PATH = Path to the install location of VMEC.
* VMEC_INSTALL_NAME = Name of the VMEC binary.
* V3FIT_INSTALL_PATH = Path to the install location of VMEC.
* V3FIT_INSTALL_NAME = Name of the VMEC binary.

### Running

To run v3post example workflow, copy the files to a run directory and run the 
command

ips.py --config=ips.v3post.config --platform=platform.conf

To run v3fit example workflow, copy the files to a run directory and run the 
command

ips.py --config=ips.v3fit.config --platform=platform.conf
