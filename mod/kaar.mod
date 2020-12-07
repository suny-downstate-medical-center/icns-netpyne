TITLE KA channel from PN MATLAB/PYTHON model and KAR (Anomalous Rectifier) channel

NEURON {
	SUFFIX KAAR
	USEION k READ ek WRITE ik
	RANGE gAbar, gA, ik, gARbar, iar, ia
	RANGE miA1, tmA1, hiA1, thA1, miA2, tmA2, hiA2, thA2, moA1, moA2, hoA1, hoA2
	GLOBAL z,T
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)	
}

CONSTANT {
	FARADAY = 96480		(coulomb/mole)		: moles do not appear in units
	R = 8.314 (k-mole*joule/degC)
}

PARAMETER {
	gAbar = 0.005305165 (S/cm2) <0,1e9>
	moA1 = 4.514268765351059e-01
	moA2 = 2.170679363371657e-01
	hoA1 = 6.157878435363050e-02
	hoA2 = 6.157878220370643e-02
	gARbar = 0.002122066 (S/cm2)
	z = 2
	T = 308
}

STATE {
	 mA1 hA1 
	 mA2 hA2
}

ASSIGNED {
	v (mV)
	ik (mA/cm2)
	ia (mA/cm2)
	iar (mA/cm2)
	gA (S/cm2)
	miA1
	miA2
	hiA1
	hiA2 
	tmA1 (ms)
	tmA2 (ms)  
	thA1 (ms)
	thA2 (ms)
	ek (mV)      
}

INITIAL {
	rate(v)
	mA1 = moA1
	mA2 = moA2
	hA1 = hoA1
	hA2 = hoA2
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gA=gAbar*((0.6*hA1*(mA1^4))+(0.4*hA2*(mA2^4)))
	ia = gA*(v-(-94)) 		: based on M/P code of PN Neuron
	iar = (gARbar*((v-(-94)+5.66)/(1+(exp(((v-(-94)-15.3)*z*FARADAY)/(1000*R*T))))))		: based on M/P code of PN Neuron
	ik = 1000*(ia+iar)
}

DERIVATIVE states {	
	rate(v)
	mA1' = 1000*(miA1 - mA1)/tmA1
	hA1' = 1000*(hiA1 - hA1)/thA1
	mA2' = 1000*(miA2 - mA2)/tmA2
	hA2' = 1000*(hiA2 - hA2)/thA2
}

UNITSOFF

PROCEDURE rate(v(mV)) {
	miA1 = 1/(1+(exp(-(v+60)/8.5)))
	tmA1 = 1/((exp((v+35.82)/19.69))+(exp(-(v+79.69)/12.7))+0.37)
	hiA1 = 1/(1+(exp((v+78)/6)))
	if (v>=-63) {
		thA1 = 19
	} else {
		thA1 = 1/((exp((v+46.05)/5))+(exp(-(v+238.4)/37.45))+0.37)
	}
	miA2 = 1/(1+(exp(-(v+36)/20)))
	tmA2 = 1/((exp((v+35.82)/19.69))+(exp(-(v+79.69)/12.7))+0.37)
	hiA2 = 1/(1+(exp((v+78)/6)))
	if (v>=-73) {
		thA2 = 60
	} else {
		thA2 = 1/((exp((v+46.05)/5))+(exp(-(v+238.4)/37.45))+0.37)
	}

}
UNITSON
