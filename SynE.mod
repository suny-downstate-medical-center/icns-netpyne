TITLE Excitatory synaptic input from PN model in MATLAB/PYTHON

NEURON {
   SUFFIX SynE
   RANGE tauE, eSynE, gnE, iSynE
   NONSPECIFIC_CURRENT iSynE
}

UNITS {
   (nA) = (nanoamp)
   (mV) = (millivolt)
   (uS) = (microsiemens)
}

PARAMETER {
   tauE = 30 (ms) <1e-9,1e9>
   gnE = 0.000424413 (S/cm2)
   eSynE = -10   (mV)
}

ASSIGNED { 
  v (mV) 
  iSynE (mA) 
}

STATE {
    gSynE (S/cm2)
}

INITIAL {
 gSynE = 0 (S/cm2) 
}

BREAKPOINT {
  SOLVE states METHOD cnexp
  iSynE = 1000*gSynE*(v - eSynE)
}

DERIVATIVE states {
 gSynE' = 1000*(gnE-gSynE)/tauE
}
