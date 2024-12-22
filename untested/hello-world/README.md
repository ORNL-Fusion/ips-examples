# Install the IPS
Skip this if you've already installed the IPS. 

1. Clone the examples repo
```
git clone https://github.com/ORNL-Fusion/ips-examples.git
cd ips-examples
```
2. Export the `IPS_EXAMPLES_PATH` environment variable
```
export IPS_EXAMPLES_PATH=${PWD}
```

# Run the example

1. Run the hello-world example
```
cd hello-world
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




