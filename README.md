# Intrinsic Cardiac Nervous System - Principal Neuron model
Version 0.1

# Description: 
Principle Neuron model adapted to run in NettPyNE, with graphical output of voltage v. time.


# Contents
## NetPyNE: 
init.py, cfg.py, netParams.py
## NMOD: 
‘mod’ folder containing ahp.mod, cabuff.mod, cal.mod, can.mod, kaar.mod, kdr.mod, naf.mod, SynE.mod


# Usage
## Download the above scripts, open new Terminal window, and cd to directory where files are saved.

## From cmd line, install most recent version of Python: enter pip3 install ipython

## Install NEURON: enter pip3 install neuron
This should also install the NMOD compiler.
Enter which nrnivmodl in the Terminal to ensure successful installation of NMOD compiler (should point to local compiler)

## Install NETPyNE: enter pip3 install netpyne

## Compile mod files: enter nrnivmodl mod. 
A new directory ‘x86_64’ will appear in the parent directory

## Run a simulation: enter ipython init.py
The result will plotted and saved as ‘example_plot_netpyne.png’ 

