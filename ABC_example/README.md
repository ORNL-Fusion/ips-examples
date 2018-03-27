I ran this with the following series of commands as a clean install

```
git clone https://github.com/HPC-SimTools/IPS-framework.git
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```

Edit `ips-wrappers/env.ips.osx` to point to these clones ...

```
export IPS_PATH=$HOME/code/ips-testing/IPS-Framework
export IPS_WRAPPER_PATH=$HOME/code/ips-testing/ips-wrappers
export IPS_EXAMPLES_PATH=$HOME/code/ips-testing/ips-examples
```

Then source and run ...
```
source ips-wrappers/env.ips.osx
cd ips-examples/ABC_example
ips.py --simulation=ABC_simulation.config --platform=platform.conf
```

