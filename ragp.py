from neuron import h,gui


soma = h.Section(name='soma')
### h.topology()

### soma.psection()
#{'point_processes': {}, 
#'density_mechs': {}, 
#'ions': {}, 
#'morphology': {'L': 100.0, 
#'diam': [500.0], 
#'pts3d': [], 
#'parent': None, 
#'trueparent': None}, 
#'nseg': 1, 
#'Ra': 35.4, 
#'cm': [1.0], 
#'regions': set(), 
#'species': set(), 
#'name': 
#'soma', 
#'hoc_internal_name': 
#'__nrnsec_0x7ff4af765000', 
#'cell': None}

# pprint.pprint
soma.psection()['morphology']['L']

# NOTE: to change vals
#h.celsius
#soma.Ra



### SETTING VALUES
soma.L = 20
soma.diam = 20
# dir(soma)
#import textwrap
#print(textwrap.fill(', '.join(dir(h))))
# dir()
# help()

### INSERT ION CHANNELS
soma.insert('hh')