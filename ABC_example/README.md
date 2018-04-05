
```
export IPS_DIR=${PWD}
git clone https://github.com/HPC-SimTools/IPS-framework.git ips-framework
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```

Then source and run ...
```
source ips-wrappers/env.ips.osx
cd ips-examples/ABC_example
ips.py --simulation=ABC_simulation.config --platform=platform.conf
```

