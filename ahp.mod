TITLE AHP channel from PN MATLAB model (not present in thesis)

NEURON {
	SUFFIX AHP
	USEION k READ ek WRITE ik
	USEION ca READ cai
	RANGE gAHPbar, ik, gAHP
	RANGE moAHP, mAHP, miAHP, tmAHP
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)    
	(molar) = (1/liter)
  	(mM) = (millimolar)
}

PARAMETER {
	gAHPbar=0.005305165 (S/cm2) <0,1e9> 
	moAHP =  1.113929524548006e-01
}

ASSIGNED {
	v (mV)
	ek (mV)
	cai (mM)
	ik (mA/cm2)
	miAHP
	tmAHP (ms)
	gAHP (S/cm2)
}

STATE {
	mAHP
}


INITIAL {
	rates(v,cai)
	mAHP = moAHP
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gAHP = gAHPbar*mAHP*mAHP
	ik = 1000*gAHP*(v - (-94))
}

DERIVATIVE states {
	rates(v,cai)
	mAHP' = 1000*(miAHP - mAHP)/tmAHP
}

UNITSOFF
PROCEDURE rates(v(mV),cai(mM)) {LOCAL numahp
	numahp = 1.25e8*cai*cai
	tmAHP = 1e3/(numahp+2.5)
	miAHP = numahp*1e-3*tmAHP
}
UNITSON
