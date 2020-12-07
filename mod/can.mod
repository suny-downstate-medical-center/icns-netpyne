TITLE CaN channel from Vadigepalli et al. (2001)

NEURON {
	SUFFIX CaN
	USEION ca READ cai WRITE ica
	RANGE gcaN, gcaNbar, ica, ecal, cail
	RANGE micaN, tmcaN, hicaN1, thcaN1, hicaN2, thcaN2, cainit
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)	
	(molar) = (1/liter)
  	(mM) = (millimolar)
}

PARAMETER {
	gcaNbar=7.07355E-05 (S/cm2) <0,1e9>
	cainit = 5.007132151536936e-05 (mM)
}

STATE {
	 mcaN hcaN2 hcaN1
}

ASSIGNED {
	v (mV)
	ica (mA/cm2)
	gcaN (S/cm2)
	micaN
	hicaN1
	hicaN2 
	tmcaN (ms)  
	thcaN1 (ms)
	thcaN2 (ms)  
	eca (mV) 
	ecal (mV) 
	cai (mM)
	cao (mM)    
}

INITIAL {
	:rate(v,cai)
	mcaN = 0
	hcaN1 = 0
	hcaN2 = 0
	cai = cainit
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gcaN=gcaNbar*mcaN*((0.55*hcaN1)+(0.45*hcaN2))
	ica=1000*gcaN*(v-(13.27*log(4/cai)))
}

DERIVATIVE states {	
	rate(v,cai)
	mcaN' = 1000*(micaN - mcaN)/tmcaN
	hcaN1' = 1000*(hicaN1 - hcaN1)/thcaN1
	hcaN2' = 1000*(hicaN2 - hcaN2)/thcaN2
}

UNITSOFF

PROCEDURE rate(v(mV),cai(mM)) {
	micaN = 1/(1+(exp(-(v+20)/4.5)))
	tmcaN = (0.364*exp(-(0.042^2)*((v+31)^2)))+0.442
	hicaN1 = 1/(1+(exp((v+20)/25)))
	thcaN1 = (3.752*(exp(-(0.0395^2)*((v+30)^2))))+0.56
	hicaN2 = (0.2/(1+(exp(-(v+40)/10))))+(1/(1+(exp((v+20)/40))))
	thcaN2 = (25.2*exp(-(0.0275^2)*((v+40)^2)))+8.4
}
UNITSON
