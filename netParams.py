from netpyne import specs, sim

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters
from cfg import cfg

## Cell types
PYRcell = {'secs': {}}

PYRcell['secs']['soma'] = {'geom': {}, 'mechs': {}}  
PYRcell['secs']['soma']['geom'] = {'diam': 30, 'L': 30, 'Ra': 123.0, 'cm': 0.884194128} 

PYRcell['secs']['soma']['mechs']['pas'] = {'g': 1.768388, 'e': -43} 	#.001768388 * 1000
#PYRcell['secs']['soma']['mechs']['Naf'] = {'gNabar': 0.106103295} 		#0.106103295
#PYRcell['secs']['soma']['mechs']['KDR'] = {'gDrbar': 0.031830989} 		#0.031830989
#PYRcell['secs']['soma']['mechs']['KAAR'] = {'gAbar': 0.005305165} 	#0.005305165
#PYRcell['secs']['soma']['mechs']['KAAR'] = {'gARbar': 0.002122066} 	#0.002122066
#PYRcell['secs']['soma']['mechs']['CaL'] = {'gcaLbar': 5.30516E-05}		#5.30516E-05
#PYRcell['secs']['soma']['mechs']['CaN'] = {'gcaNbar': 7.07355E-05}		#7.07355E-05
PYRcell['secs']['soma']['mechs']['AHP'] = {'gAHPbar': 0.008305165} 		#0.005305165
#PYRcell['secs']['soma']['mechs']['SynE'] = {'tauE': 30, 'gnE': 0.000424413, 'eSynE': -10}
PYRcell['secs']['soma']['mechs']['cabuff'] = {'vshell': 2.5e-13,'Btot': 0.03,'Kbuff': 0.001,'cai0': 5e-5,'dia': 30e4}

netParams.cellParams['PYR'] = PYRcell

print()
for secName in PYRcell['secs']:
	print(secName)
	for mechName, mech in PYRcell['secs'][secName]['mechs'].items():
		print(mechName, mech)
		print()
		 
## Population parameters
netParams.popParams['ragp'] = {'cellType': 'PYR', 'numCells': 1}
#netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20}

# Stimulation parameters
netParams.stimSourceParams['iclamp'] = {'type': 'IClamp', 'amp': 1000, 'dur': cfg.duration, 'delay': 0} #0.012*1000
netParams.stimTargetParams['iclamp->PYR'] = {'source': 'iclamp', 'conds': {'cellType': 'PYR'}, 'sec': 'soma', 'loc': 0.5}


# Synaptic mechanism parameters
#netParams.synMechParams['exc'] = {'mod': 'PN_SynE', 'tauE': 30.0, 'gnE': 10, 'eSynE': 10}  # excitatory synaptic mechanism
#netParams.synMechParams['inh'] = {'mod': 'PN_SynI', 'tauI': 30.0, 'gnI': 0.0001, 'eSynI': -94}   # inhibitory synaptic mechanism
#netParams.synMechParams['inh'] = {'mod': 'AlphaSynapse', 'onset': 40.0, 'tau': 30.0, 'gmax': 0, 'e': -94}  # inhibitory synaptic mechanism


#netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}
#netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': cfg.stim_weight, 'delay': 5, 'synMech': 'exc'}

## Cell connectivity rules
# netParams.connParams['S->M'] = {'preConds': {'pop': 'S'}, 'postConds': {'pop': 'M'},  #  S -> M
#     'probability': 0.5,         # probability of connection
#     'weight': 0.01,             # synaptic weight 
#     'delay': 5,                 # transmission delay (ms) 
#     'sec': 'dend',              # section to connect to
#     'loc': 1.0,                 # location of synapse
#     'synMech': 'exc'}           # target synaptic mechanism

