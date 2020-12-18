from neuron import h,gui


soma = h.Section(name='soma')
### h.topology()

### somttpsection()
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

# VALS TO CHANGE IN NEURON t
#h.celsius
#soma.Ra



### SETTING VALUES
soma.L = []
soma.diam = []
# dir(soma)
#import textwrap
#print(textwrap.fill(', '.join(dir(h))))
# dir()
# help()

### INSERT ION CHANNELS
soma.insert('hh')


### SECTIONS AND SEGMENTS ###
# Section: section
# Segment: segment
print("type(soma)={}".format(type(soma)))
