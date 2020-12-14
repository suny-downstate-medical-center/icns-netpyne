# Intrinsic Cardiac Nervous System-Right Atrial Genglionic Plexus: Principal Neuron model - NetPyNE

The mod files are from here:
https://senselab.med.yale.edu/ModelDB/ShowModel?model=3800

# Description: 
Principle Neuron model adapted to run in NetPyNE, with graphical output of voltage v. time.

# Contents
  NetPyNE: init.py, cfg.py, netParams.py;
  NMOD: ‘mod’ folder containing ahp.mod, cabuff.mod, cal.mod, can.mod, kaar.mod, kdr.mod, naf.mod, SynE.mod;
  README.md; 'example_plot_netpyne.png'

# Usage
## Clone repository

## Open a new Terminal window

## Install NEURON
### Enter: pip3 install neuron (This will also install the NMOD compiler)
### Enter: which nrnivmodl (This will indicate successful installation of NMOD compiler - should point to local compiler)

## Install NETPyNE 
  Enter: pip3 install -e netpyne

## Compile mod files 
    Enter: nrnivmodl mod

## Run a simulation: 
### Enter: ipython init.py or python3 init.py

# Output
The result will plotted and saved as ‘test_plot_netpyne.png’ 

