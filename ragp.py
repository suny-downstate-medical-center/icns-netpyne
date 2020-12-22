from neuron import h
soma = h.Section(name='soma')
dend = h.Section(name='dend')

soma.L = 12.6157
soma.diam = 12.6157
dend.L = 200
dend.diam = 1

soma.cm = 1   # membrane capacitance in microFarads /cm^2

soma.insert('hh')
hh.gnabar = 0.12 # sodium condundtance in S/cm^2
hh.gkbar = 0.036 # potassium conductance in S/cm^2
hh.gl = 0.0003   # leak conductance in S/cm2
hh.el = -54.3 # reversal potential in mV
