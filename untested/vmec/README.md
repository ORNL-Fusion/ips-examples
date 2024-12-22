# IPS-VMEC Example

Example use case for the ips-vmec components.

## List of Files
* ips.vmec.config Work flow configuration file for running on a local machine.
* platform.conf Configuration file for the local machine.
* input.test.vmec

## Requirements
* vmec or parvmec
* The IPS vmec component.
* The IPS vmec_init component.
* The IPS vmec_driver driver.

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

The ips-vmec components require definitions for the following variables.

* IPS_VMEC_COMP_PATH Path to the ips-vmec scripts.
* VMEC_INSTALL_PATH = Path to the install location of VMEC.
* VMEC_INSTALL_NAME = Name of the VMEC binary.

### Running

To run this example workflow, copy the files to a run directory and run the 
command

ips.py --config=ips.vmec.config --platform=platform.conf
