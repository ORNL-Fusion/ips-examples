If you already have the IPS with the structure created in 1) then skip to 2) to run.

1) To download, create a directory where your IPS installation will live, e.g.
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

2) To set the environment, cd to the IPS top level directory (e.g. /IPS/, unless you are 
already there).  Export IPS_DIR environment variable and source env.ips.
```
export IPS_DIR=${PWD}
source ips-wrappers/env.ips
```

3) To run, cd into the example directory and run
```
cd ips-examples/ABC_example
ips.py --simulation=ips.config --platform=platform.conf
````

Hello_world is (almost) the simplest possible IPS run, exercising two components DRIVER, 
hello_driver.py, and WORKER, hello_worker.py.  We say "almost" because it would actually 
be possible to have an IPS simulation with only a driver and no components.  Hello world 
does not use any STATE files or use any physics components.  There is one external connection, 
to an environment file (env.ips) that is sourced from $IPS_DIR/ips-examples/env.ips in the 
present setup.

To clean all the run files and start with just the input deck run 
```
./cleanIpsRun.sh
```



