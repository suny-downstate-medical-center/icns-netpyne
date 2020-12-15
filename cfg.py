from netpyne import specs, sim


# Simulation options
cfg = specs.SimConfig()       # object of class cfg to store simulation configuration

cfg.hParams = {'celsius': 35, 'v_init': -61.656} #, 'clamp_resist': 0.001}
cfg.duration = 1          # Duration of the simulation, in SEC
cfg.dt = 0.000025                # Internal integration timestep to use
cfg.verbose = False           # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}


cfg.recordStep = 0.000025           # Step size in SEC to save data (eg. V traces, LFP, etc)
cfg.filename = 'ragpv1'         # Set file output name
cfg.savePickle = False        # Save params, network and sim output to pickle file

cfg.analysis['plotTraces'] = {'include': [0, 1, 2], 'saveFig': False}  # Plot recorded traces for this list of cells
