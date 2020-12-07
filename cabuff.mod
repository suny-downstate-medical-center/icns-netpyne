TITLE Ca Buffers from PN Model in MATLAB


NEURON {
	SUFFIX cabuff
	USEION ca READ ica,cai WRITE cai	:Calcium flux from membrane mechanisms is crucial for intracellular calcium dynamics
	RANGE vshell, Btot, Kbuff, cai0, dia, cainit 						
}

UNITS {
	(um) = (micron)
	(mM) = (milli/liter)
	(mA) = (milliamp)
}

CONSTANT {
	FARADAY = 96480		(coulomb/mole)		
	PI = 3.142857 
}

PARAMETER {
	vshell = 2.5e-13 (liter)
	Btot = 0.03 (mM)
	Kbuff = 0.001 (mM)
	cai0 = 5e-5 (mM)
	dia = 30e4 (um)	
	cainit = 5.007132151536936e-05 (mM)												
}

ASSIGNED {
	v (mV)
	ica	(mA/cm2)
}

STATE {
		cai	(mM) 
	}

INITIAL {
	cai = cainit
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
}

DERIVATIVE states {	
	cai' = 1000*( ((ica*PI*dia*dia)*(1-(Btot/(cai+Kbuff+Btot)))/(2*vshell*FARADAY)) + ((cai0-cai)/(17.7*exp(v/35))) )
}

