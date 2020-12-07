TITLE KDR channel from PN MATLAB/PYTHON model

NEURON {
	SUFFIX KDR
	USEION k READ ek WRITE ik
	RANGE gDrbar, gDr, ik
	RANGE miDR, tmDR, moDr
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)	
}

PARAMETER {
	gDrbar=0.031830989 (S/cm2) <0,1e9>
	moDr = 2.642252518522899e-02
	
}

STATE {
	 mDr 
}

ASSIGNED {
	v (mV)
	ik (mA/cm2)
	gDr (S/cm2)
	miDR 
	tmDR (ms)  
	ek (mV)      
}

INITIAL {
	rate(v)
	mDr = moDr
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gDr=gDrbar*mDr*mDr*mDr*mDr
	ik=1000*gDr*(v-(-94)) : based on M/P code of PN Neuron
}

DERIVATIVE states {	
	rate(v)
	mDr' = 1000*(miDR - mDr)/tmDR
}

UNITSOFF

PROCEDURE rate(v(mV)) {LOCAL numdr
	numdr = 0.01*((v+45)/(1-(exp(-(v+45)/5))))
	tmDR = 1/(	(0.01*((v+45)/(1-(exp(-(v+45)/5)))))	+	(0.17*exp(-(v+50)/40))	)
	miDR = numdr*tmDR
}
UNITSON
