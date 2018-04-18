# marketsim
Agent-based model of tokenized carbon storage market

Run simulation.py

Once we get simulation running, will need rudimentary UI and graphical outputs (plotly seems a little friendlier than matplitlib)

### Usage

Create a virtual environment and install from requirements.txt.

```
mkvirtualenv marketsim
pip install -r requirements.txt
```

Run simulation.py.

```
python simulation.py
```

### Troubleshooting

```
$ pip show abce

Name: abce
Version: 0.9.1b1
Summary: Agent-Based Complete Economy modelling platform
Home-page: https://github.com/AB-CE/abce.git
Author: Davoud Taghawi-Nejad
Author-email: Davoud@Taghawi-Nejad.de
License: UNKNOWN
Location: /home/wicker/envs/marketsim/lib/python3.5/site-packages
Requires: future, flexx, pandas, dataset, numpy, networkx, bokeh
Required-by: 
(marketsim) 
```

```
pip 10.0.0 from /home/wicker/envs/marketsim/lib/python3.5/site-packages/pip (python 3.5)
```

When I run `python simulation.py` I get the following trace:

```
/home/wicker/envs/marketsim/lib/python3.5/site-packages/bokeh/util/deprecation.py:34: BokehDeprecationWarning: 
The bokeh.charts API has moved to a separate 'bkcharts' package.

This compatibility shim will remain until Bokeh 1.0 is released.
After that, if you want to use this API you will have to install
the bkcharts package explicitly.

  warn(message)
Traceback (most recent call last):
  File "/home/wicker/envs/marketsim/lib/python3.5/site-packages/abce/processorgroup.py", line 42, in make_an_agent
    agent.init(parameters, agent_parameters)
  File "/home/wicker/proj/Work/marketsim/supplier.py", line 21, in init
    self.num_suppliers = simulation_parameters['num_suppliers'] # See line 7 above - what's the best way to address this?
KeyError: 'num_suppliers'
Traceback (most recent call last):
  File "/home/wicker/envs/marketsim/lib/python3.5/site-packages/abce/processorgroup.py", line 42, in make_an_agent
    agent.init(parameters, agent_parameters)
  File "/home/wicker/proj/Work/marketsim/supplier.py", line 21, in init
    self.num_suppliers = simulation_parameters['num_suppliers'] # See line 7 above - what's the best way to address this?
KeyError: 'num_suppliers'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "simulation.py", line 73, in <module>
    main()
  File "simulation.py", line 37, in main
    simulation.build_agents(Supplier, 'supplier', 100) # Put these in parameters.csv and use .build_agents_from_file
  File "/home/wicker/envs/marketsim/lib/python3.5/site-packages/abce/__init__.py", line 476, in build_agents
    agent_params_from_sim=agent_params_from_sim)
  File "/home/wicker/envs/marketsim/lib/python3.5/site-packages/abce/processorgroup.py", line 22, in add_group
    agent_parameters=agent_parameters[i])
  File "/home/wicker/envs/marketsim/lib/python3.5/site-packages/abce/processorgroup.py", line 53, in make_an_agent
    raise Exception()
Exception
```


