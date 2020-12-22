from neuron import h
soma = h.Section(name='soma')

soma.L, soma.diam, soma.cm = 12.6157, 12.6157, 1

soma.insert('hh')
hh.gnabar = 0.12 # sodium condundtance in S/cm^2
hh.gkbar = 0.036 # potassium conductance in S/cm^2
hh.gl = 0.0003   # leak conductance in S/cm2
hh.el = -54.3 # reversal potential in mV
