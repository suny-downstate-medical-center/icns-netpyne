# Intrinsic Cardiac Nervous System - Principal Neuron model
Version 0.1

# Description: 
Principle Neuron model adapted to run in NetPyNE, with graphical output of voltage v. time.


# Contents
NetPyNE: init.py, cfg.py, netParams.py;
NMOD: ‘mod’ folder containing ahp.mod, cabuff.mod, cal.mod, can.mod, kaar.mod, kdr.mod, naf.mod, SynE.mod;
README.md; 'xample_plot_netpyne.png'


# Usage
## Download the above scripts from repo.

## Opem a mew Terminal window.

## Install most recent version of Python: 
Enter pip3 install ipython

## Install NEURON: 
Enter pip3 install neuron
  This should also install the NMOD compiler.
  Enter which nrnivmodl in the Terminal to ensure successful installation of NMOD compiler (should point to local compiler).

## Install NETPyNE: 
Enter pip3 install netpyne

## Compile mod files: 
Enter nrnivmodl mod. 
  A new directory ‘x86_64’ will appear in the parent directory

## Run a simulation: 
Enter ipython init.py

# Output
The result will plotted and saved as ‘example_plot_netpyne.png’ 

