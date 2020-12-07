TITLE Na channel from PN MATLAB/PYTHON model 

NEURON {
	SUFFIX Naf
	USEION na READ ena WRITE ina
	RANGE gNabar, ina, gNa
	RANGE moNa, hoNa, miNa, tmNa, hiNa, thNa
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)    
}

PARAMETER {
	gNabar=0.106103295 (S/cm2) <0,1e9> 
	moNa = 1.277236125734123e-02
 	hoNa = 3.429830012296679e-01               
}

ASSIGNED {
	v (mV)
	ena (mV)
	ina (mA/cm2)
	miNa hiNa
	tmNa (ms)
	thNa (ms) 
	gNa (S/cm2)
}

STATE {
	mNa hNa
}


INITIAL {
	rates(v)
	mNa = moNa
	hNa = hoNa	
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gNa = gNabar*mNa*mNa*mNa*hNa
	ina = 1000*gNa*(v - 55) : based on M/P code of PN Neuron
}

DERIVATIVE states {
	rates(v)
	mNa' = 1000*(miNa - mNa)/tmNa
	hNa' = 1000*(hiNa - hNa)/thNa
}

UNITSOFF
PROCEDURE rates(v(mV)) {LOCAL numna, nuhna
	numna = 0.091*((v+38)/(1-(exp(-(v+38)/5))))
	tmNa = 1/(	(0.091*((v+38)/(1-(exp(-(v+38)/5)))))	+	(0.062*	(v+38)/(exp((v+38)/5)-1))	)
	miNa = numna*tmNa

	nuhna = 0.016*(exp(-(v+55)/15))
	thNa = 1/((0.016*(exp(-(v+55)/15)))+(2.07/(1+(exp(-(v-17)/21)))))
	hiNa = nuhna*thNa
}
UNITSON
