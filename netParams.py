from netpyne import specs, sim

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters
from cfg import cfg

## Cell types
PYRcell = {'secs': {}}

PYRcell['secs']['soma'] = {'geom': {}, 'mechs': {}}  
PYRcell['secs']['soma']['geom'] = {'diam': 30, 'L': 30, 'Ra': 123.0, 'cm': 0.884194128} 

PYRcell['secs']['soma']['mechs']['pas'] = {'g': 1.768388, 'e': -43} 	#.001768388 * 1000
PYRcell['secs']['soma']['mechs']['Naf'] = {'gNabar': 0.106103295} 		#0.106103295
PYRcell['secs']['soma']['mechs']['KDR'] = {'gDrbar': 0.031830989} 		#0.031830989
PYRcell['secs']['soma']['mechs']['KAAR'] = {'gAbar': 0.005305165} 		#0.005305165
PYRcell['secs']['soma']['mechs']['KAAR'] = {'gARbar': 0.002122066} 		#0.002122066
PYRcell['secs']['soma']['mechs']['CaL'] = {'gcaLbar': 5.30516E-05}		#5.30516E-05
PYRcell['secs']['soma']['mechs']['CaN'] = {'gcaNbar': 7.07355E-05}		#7.07355E-05
PYRcell['secs']['soma']['mechs']['AHP'] = {'gAHPbar': 0.005305165} 		#0.005305165
PYRcell['secs']['soma']['mechs']['SynE'] = {'tauE': 30, 'gnE': 0.000424413, 'eSynE': -10} #0.000424413
PYRcell['secs']['soma']['mechs']['cabuff'] = {'vshell': 2.8e-10,'Btot': 0.03,'Kbuff': 0.001,'cai0': 5e-5,'dia': 30}

netParams.cellParams['PYR'] = PYRcell

print()
for secName in PYRcell['secs']:
	print(secName)
	for mechName, mech in PYRcell['secs'][secName]['mechs'].items():
		print(mechName, mech)
		print()
		 
## Population parameters
netParams.popParams['ragp'] = {'cellType': 'PYR', 'numCells': 1}

# Stimulation parameters
netParams.stimSourceParams['iclamp'] = {'type': 'IClamp', 'amp': 000, 'dur': cfg.duration, 'delay': 0} #1000
netParams.stimTargetParams['iclamp->PYR'] = {'source': 'iclamp', 'conds': {'cellType': 'PYR'}, 'sec': 'soma', 'loc': 0.5}


