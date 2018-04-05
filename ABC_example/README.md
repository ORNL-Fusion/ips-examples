Here we assume you are installing to a directory `mydir`

```
export IPS_ROOT=mydir
cd $IPS_ROOT
git clone https://github.com/HPC-SimTools/IPS-framework.git
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```

Then source and run ...
```
source ips-wrappers/env.ips.osx
cd ips-examples/ABC_example
ips.py --simulation=ABC_simulation.config --platform=platform.conf
```

