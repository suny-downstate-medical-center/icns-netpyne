TITLE Ca Buffers from PN Model in MATLAB


NEURON {
	SUFFIX cabuff
	USEION ca READ cai, ica WRITE cai	:Calcium flux from membrane mechanisms is crucial for intracellular calcium dynamics
	RANGE vshell, Btot, Kbuff, cai0, dia, cainit, cal
	GLOBAL Pb, taupump						
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)    
	(molar) = (1/liter)
  	(mM) = (millimolar)
}

CONSTANT {
	FARADAY = 96480		(coulomb) : coulomb per mole		
	PI = 3.142857 
}

PARAMETER {
	vshell = 2.8e-10 :mL
	Btot = 0.03 (mM)
	Kbuff = 0.001 (mM)
	cai0 = 5e-5 (mM)
	dia = 30 (um)	: in cm
	cainit = 5.007132151536936e-05 (mM)											
}

ASSIGNED {
	area (um2)
	v (mV)
	ek (mV)
	cal (mM)
	ik (mA/cm2)
	ica (mA/cm2)
	miAHP
	tmAHP (ms)
	gAHP (S/cm2)
	Pb
	taupump (ms)
}

STATE {
		cai	(mM) 
	}

INITIAL {
	cai = cainit
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	cal = cai 
}

DERIVATIVE states {	
	cai' = 1000*( (((-ica/1000)*area*1e-8)*(1-(Btot/(cai+Kbuff+Btot)))/(2*vshell*FARADAY)) + ((cai0-cai)/(17.7*exp(v/35))) ) :ica is negative current (inward current)
}

