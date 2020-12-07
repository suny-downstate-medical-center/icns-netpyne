from netpyne import specs, sim


# Simulation options
cfg = specs.SimConfig()       # object of class cfg to store simulation configuration

cfg.hParams = {'celsius': 35, 'v_init': -61.656} #, 'clamp_resist': 0.001}
cfg.duration = 1          # Duration of the simulation, in SEC
cfg.dt = 0.000025                # Internal integration timestep to use
cfg.verbose = False           # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
#cfg.recordTraces['iNaf'] = {'sec':'soma','loc':0.5,'var':'ina_Naf'}
#cfg.recordTraces['ikdr'] = {'sec':'soma','loc':0.5,'var':'ik_KDR'}
#cfg.recordTraces['ika'] = {'sec':'soma','loc':0.5,'var':'ik_KAAR'}
#cfg.recordTraces['ical'] = {'sec':'soma','loc':0.5,'var':'ica_CaL'}
#cfg.recordTraces['ican'] = {'sec':'soma','loc':0.5,'var':'ica_CaN'}
#cfg.recordTraces['iahp'] = {'sec':'soma','loc':0.5,'var':'ik_AHP'}
#cfg.recordTraces['cai'] = {'sec':'soma','loc':0.5,'var':'cai_cabuff'}
#cfg.recordTraces['iSynE'] = {'sec':'soma','loc':0.5,'var':'iSynE_SynE'}
#cfg.recordTraces['gSynE'] = {'sec':'soma','loc':0.5,'var':'gSynE_SynE'}


cfg.recordStep = 0.000025           # Step size in SEC to save data (eg. V traces, LFP, etc)
#cfg.filename = 'ragpv1'         # Set file output name
cfg.savePickle = False        # Save params, network and sim output to pickle file

#cfg.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster
cfg.analysis['plotTraces'] = {'include': [0, 1, 2], 'saveFig': False}  # Plot recorded traces for this list of cells
#cfg.analysis['plot2Dnet'] = {'saveFig': True}                   # plot 2D cell positions and connections

# Parameters to be varied
#cfg.stim_weight = 0.0001  # Default value is 0.01
