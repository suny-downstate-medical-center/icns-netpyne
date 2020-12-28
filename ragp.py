from neuron import h
soma = h.Section(name='soma')

soma.L, soma.diam, soma.cm = 12.6157, 12.6157, 1

soma.insert('hh')
hh.gnabar, hh.gkbar, hh.gl, hh.el = 0.12 , 0.036 , 0.0003 , -54.3


## inserting IClamp
