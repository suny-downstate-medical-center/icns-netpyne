from neuron import h
#from neuron import gui


soma = h.Section(name='soma')
dend = h.Section(name='dend')


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

# VALS TO CHANGE IN NEURON t
#h.celsius
#soma.Ra


### SETTING VALUES
soma.L = 12.6157
soma.diam = 12.6157
dend.L = 200
dend.diam = 1
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

#vec.record()
#vec.record(dend(0.5)._ref_v)

# class BallAndStick:
  #  def __init__(self, gid):
  #      self._gid = gid
   #     self._setup_morphology()
   #     self._setup_biophysics()
   # def _setup_morphology(self):
       # self.soma = h.Section(name='soma', cell=self)
       # self.dend = h.Section(name='dend', cell=self)
       # self.all = [self.soma, self.dend]
#        self.dend.connect(self.soma)
#        self.soma.L = self.soma.diam = 12.6157
#        self.dend.L = 200
#        self.dend.diam = 1
#    def _setup_biophysics(self):
#        for sec in self.all:
#            sec.Ra = 100    # Axial resistance in Ohm * cm
#            sec.cm = 1      # Membrane capacitance in micro Farads / cm^2
#        self.soma.insert('hh')                                                    # <-- NEW                   for seg in self.soma:                                                     # <-- NEW
#           seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2                   # <-- NEW
#           seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2                # <-- NEW
#            seg.hh.gl = 0.0003    # Leak conductance in S/cm2                     # <-- NEW
#            seg.hh.el = -54.3     # Reversal potential in mV                      # <-- NEW
#    def __repr__(self):
#        return 'BallAndStick[{}]'.format(self._gid)

# my_cell = BallAndStick(0)

# Biophysics

soma.Ra = 100 # axial resistance in Ohm * cm
soma.cm = 1   # membrane capacitance in microFarads /cm^2

hh.gnabar = 0.12 # sodium condundtance in S/cm^2
hh.gkbar = 0.036 # potassium conductance in S/cm^2
hh.gl = 0.0003   # leak conductance in S/cm2
hh.el = -54.3 # reversal potential in mV

# Insert a passive (leak) current in dendrite
# Insert passive current in the dendrite                       # <-- NEW
 #       self.dend.insert('pas')                                        # <-- NEW
 #       for seg in self.dend:                                          # <-- NEW
 #           seg.pas.g = 0.001  # Passive conductance in S/cm2          # <-- NEW
 #           seg.pas.e = -65    # Leak reversal potential mV            # <-- NEW 
 dend.insert('pas')
 dend.pas.g = 0.001  # Passive conductance in S/cm2
 dend.pas.e = -65 # leak reversal potential in mV
