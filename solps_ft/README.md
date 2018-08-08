# Install the IPS
Skip this if you've already installed the IPS. 

1. Create an IPS directory and clone the IPS-framework, wrappers, and examples repos.
```
mkdir IPS
cd IPS
git clone https://github.com/HPC-SimTools/IPS-framework.git ips-framework
git clone https://github.com/ORNL-Fusion/ips-wrappers.git
git clone https://github.com/ORNL-Fusion/ips-examples.git
```
2. Export the `IPS_DIR` environment variable
```
export IPS_DIR=${PWD}
```
3. Add this to your `.bashrc` or otherwise so it's there next time you open a shell (Note: Adapt for `csh` or otherwise).
```
echo 'export IPS_DIR='${PWD} >> ~/.bashrc 
```

# Run the example

1. Source the IPS environemnt
```
cd $IPS_DIR
source ips-wrappers/env.ips
```
2. Run the hello-world example
```
cd ips-examples/hello-world
ips.py --simulation=ips.config --platform=platform.conf
```
To clean all the run files and start with just the input deck run 
```
./cleanIpsRun.sh
``````
## Notes on the hello-world example
Hello_world is (almost) the simplest possible IPS run, exercising two components DRIVER, 
hello_driver.py, and WORKER, hello_worker.py.  We say "almost" because it would actually 
be possible to have an IPS simulation with only a driver and no components.  Hello world 
does not use any STATE files or use any physics components.  There is one external connection, 
to an environment file (env.ips) that is sourced from $IPS_DIR/ips-examples/env.ips in the 
present setup.




