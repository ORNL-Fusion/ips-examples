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

Some notes ...

It's presently failing with ...

```
dlg-macpro-2:ABC_example dg6$ ips.py --simulation=ABC_simulation.config --platform=platform.conf
Starting IPS
Created <class 'basic_init.basic_init'>
Created <class 'basic_driver.basic_driver'>
Created <class 'A_component.A_component'>
Created <class 'B_component.B_component'>
Created <class 'C_component.C_component'>
Created <class 'runspaceInitComponent.runspaceInitComponent'>
2018-03-26 13:04:28,301 FRAMEWORK       ERROR    Error in configuration file : NAME = PortalBridge   SCRIPT = /Users/dg6/code/ips-testing/IPS-framework/framework/src/portalBridge.py
2018-03-26 13:04:28,301 FRAMEWORK       ERROR    Error instantiating IPS component PortalBridge From portalBridge
Traceback (most recent call last):
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 711, in _create_component
    module = imp.load_module(script, modFile, pathname, description)
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/portalBridge.py", line 18, in <module>
    from convert_log_function import *
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/convert_log_function.py", line 7, in <module>
    import HTML
ImportError: No module named HTML
2018-03-26 13:04:28,302 FRAMEWORK       ERROR    Problem initializing managers
Traceback (most recent call last):
  File "/Users/dg6/code/ips-testing/IPS-Framework/framework/src/ips.py", line 272, in __init__
    self.ftb)
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 445, in initialize
    self._initialize_fwk_components()
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 531, in _initialize_fwk_components
    self.sim_map[self.fwk_sim_name])
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 711, in _create_component
    module = imp.load_module(script, modFile, pathname, description)
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/portalBridge.py", line 18, in <module>
    from convert_log_function import *
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/convert_log_function.py", line 7, in <module>
    import HTML
ImportError: No module named HTML
Traceback (most recent call last):
  File "/Users/dg6/code/ips-testing/IPS-Framework/framework/src/ips.py", line 1247, in <module>
    sys.exit(main())
  File "/Users/dg6/code/ips-testing/IPS-Framework/framework/src/ips.py", line 1227, in main
    options.cmd_nodes, options.cmd_ppn)
  File "/Users/dg6/code/ips-testing/IPS-Framework/framework/src/ips.py", line 272, in __init__
    self.ftb)
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 445, in initialize
    self._initialize_fwk_components()
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 531, in _initialize_fwk_components
    self.sim_map[self.fwk_sim_name])
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/configurationManager.py", line 711, in _create_component
    module = imp.load_module(script, modFile, pathname, description)
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/portalBridge.py", line 18, in <module>
    from convert_log_function import *
  File "/Users/dg6/code/ips-testing/IPS-framework/framework/src/convert_log_function.py", line 7, in <module>
    import HTML
ImportError: No module named HTML
```

