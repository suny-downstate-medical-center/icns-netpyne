TITLE CaL channel from PN MATLAB model i.e., without F_L,mod

NEURON {
	SUFFIX CaL
	USEION ca READ cai WRITE ica
	RANGE gcaL, gcaLbar, ica, ecal, cainit
	RANGE mocaL, micaL, tmcaL
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)	
	(molar) = (1/liter)
  	(mM) = (millimolar)
}

PARAMETER {
	gcaLbar=5.30516E-05 (S/cm2) <0,1e9>
	mocaL = 1.027134762959492e-02
	cainit = 5.007132151536936e-05 (mM)
}

STATE {
	 mcaL 
}

ASSIGNED {
	cai (mM)
	cao (mM)
	v (mV)
	ica (mA/cm2)
	gcaL (S/cm2)
	micaL 
	tmcaL (ms)  
	eca (mV) 
	ecal (mV)     
}

INITIAL {
	rate(v, cai)
	mcaL = mocaL
	cai = cainit
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gcaL=gcaLbar*(mcaL^2)
	ica=1000*gcaL*(v-(13.27*log(4/cai)))
}

DERIVATIVE states {	
	rate(v,cai)
	mcaL' = 1000*(micaL - mcaL)/tmcaL
}

UNITSOFF

PROCEDURE rate(v(mV),cai(mM)) {LOCAL numcal
	numcal = 1.6/(exp(-0.072*(v-5)))
	tmcaL = 1/(1.6/(exp(-0.072*(v-5)))+(0.02*(v-1.31))/(exp((v-1.31)/5.36)-1))
	micaL = numcal*tmcaL
}
UNITSON
