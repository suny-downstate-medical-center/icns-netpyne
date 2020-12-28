from neuron import h
from neuron.units import ms, mV

soma = h.Section(name='soma')
soma.L, soma.diam, soma.cm = 12.6157, 12.6157, 1
soma.insert('hh')
#hh.gnabar, hh.gkbar, hh.gl, hh.el = 0.12 , 0.036 , 0.0003 , -54.3 #NOTE: hh. throws an error
soma(0.5).hh.gnabar # = 0.12
soma(0.5).hh.gkbar # = 0.036
soma(0.5).hh.gl = #0.0003
soma(0.5).hh.el = #-54.3

# SET NSEG - setting hh.gnabar for all nseg
# for seg in soma: print(seg)
#    seg.hh.gnabar
# soma.nseg = 3

mech = soma(0.5).hh
#print(dir(mech))

## INSERT AN ICLAMP/STIMULUS
iclamp = h.IClamp(soma(0.5))

#looking at iclamp params:
print([item for item in dir(iclamp) if not item.startswith('__')])
#['amp', 'baseattr', 'delay', 'dur', 'get_loc', 'get_segment', 'has_loc', 'hname', 'hocobjptr', 'i', 'loc', 'same']
iclamp.delay = 2 #ms
iclamp.dur = 0.1 #ms
iclamp.amp = 0.9 #nA

# get representation of current model
soma.psection()

## SET UP RECORDING VARIABLES
v = h.Vector().record(soma(0.5)._ref_v)             # membrane potential vector
t = h.Vector().record(h._ref_t)                     # timestamp vector

## RUN SIMULATION
h.load_file('stdrun.hoc')
# initalize sim w/ resting potential
h.finitialize(-65 * mV)
# continue sim thru 40 ms
h.continuerun(40 * ms)

# PLOT RESULTS
import matplotlib.pyplot as plt

plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()
# SAVE figure


## MISC CODE
#print(mech.gkbar)
#print(mech.gnabar)
#print(mech.gl)
#print(mech.el)
#print(soma(0.5).hh.gkbar)

#print("type(soma) = {}".format(type(soma)))
#print("type(soma(0.5)) = {}".format(type(soma(0.5))))

## inserting IClamp
