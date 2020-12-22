from neuron import h,gui
soma = h.Section(name='soma')
# soma.psection()['morphology']['L']

# SETTING VALUES
soma.L = []
soma.diam = []

# INSERT ION CHANNELS
soma.insert('hh')

# SECTIONS AND SEGMENTS ###
