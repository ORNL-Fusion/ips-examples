If you already have the IPS with the structure created in 1) then skip to 2) to run.

1) Create a directory where your IPS installation will live, e.g.
```
mkdir IPS
```

cd into it and clone the IPS framework and wrappers/examples repos in this directory, e.g.

```
cd IPS
git clone https://github.com/HPC-SimTools/IPS-framework.git ips-framework
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```

2) To run, if you are not already there, then cd to the IPS top level directory e.g. /IPS/,
export, source, cd to the example directory, and run ...
```
export IPS_DIR=${PWD}
source ips-wrappers/env.ips
cd ips-examples/ABC_example
ips.py --simulation=ABC_simulation.config --platform=platform.conf
```

