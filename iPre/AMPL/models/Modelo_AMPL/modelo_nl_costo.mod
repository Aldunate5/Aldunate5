set T := 1..30;	;
set F;
set K;
set Delta := 1..14;

param hold{F};
param alfa{F};
param precio{F};
param beta{F};
param c_cut{K};
param insumos{T};
param n_cuts{F,K};
param Inv_I{F,Delta};
param delta1 = 14;
param TF=30;
param apren{K};
param por_ap{K};

var P{F,T} >=0;
var W{F,T,T} >=0;
var W_0{F,Delta,Delta} >=0;
var L{F,T} >=0;
var X{K,T} >=0;
var C_Corte{K,T} >=0;
var c_hold;
var preci{F,T};
var TInv{F,T} >=0;

maximize FO: 
         sum{t in T,f in F} (P[f,t]*(alfa[f] - beta[f]*P[f,t])) - sum{f in F, s in 1..TF, u in s..TF } (hold[f]*W[f,s,u]*(u-s)) - sum{f in F, s in 1..delta1, u in s..delta1 } (hold[f]*W_0[f,s,u]*(u-s)) - sum{k in K, t in T} (X[k,t]*C_Corte[k,t]);
 
#subject to costo_corte{k in K, t in T}:
#	C_Corte[k,t] == (1-(0.001*X[k,t])^0.5)*0.4*c_cut[k]+0.6*c_cut[k];
	
subject to costo_corte{k in K, t in T}:
	C_Corte[k,t] == c_cut[k]*((1 - por_ap[k]) + por_ap[k]*(exp(-(apren[k])*X[k,t])));

subject to producc{t in T}:
	sum{k in K} X[k,t] <= insumos[t];

	
subject to Prod1{f in F, t in T}:
	sum{k in K} X[k,t]*n_cuts[f,k] == (if (t+delta1)<TF then sum {u in t..(t+delta1)} W[f,t,u] else sum {u in t..TF} W[f,t,u]);

	
subject to dda2{f in F, t in 1..delta1}:
	P[f,t] == sum{tt in 1..t: t < delta1} W_0[f,tt,t] + sum{s in 1..t} W[f,s,t];
	
#subject to Perida1{f in F, t in 1..delta1}:
#	L[f,t]  == sum{u in 1..delta1: u <= t} W_0[f,u,t]; 

subject to dda3_Nueva {f in F,t in (delta1+1)..TF}:
 	P[f,t] ==  sum{s in (t-delta1)..t} W[f,s,t];
	
subject to inv_ini{f in F, tt in Delta}:
	sum{t in Delta} W_0[f,t,tt] <= Inv_I[f,tt];

subject to Inv_neg_tiempo{f in F,t in Delta}:
	sum{tt in 1..delta1: tt > t} W_0[f,tt,t]==0;

subject to Inv_neg_tiempo2{f in F,t in T}:
	sum{tt in T: tt < t} W[f,t,tt]==0;
	
subject to perecibilidad{f in F, t in T}:
	sum{tt in T: tt > (t + delta1)} W[f,t,tt]==0;	

subject to Max_Perdida{f in F, t in T}:
	L[f,t]  <= 20; 
	
#subject to Max_prod{f in F, t in T}:
#	P[f,t] <= 10000;

subject to costo_hold: 
	c_hold == sum{f in F, s in 1..TF, u in s..TF } (hold[f]*W[f,s,u]*(u-s)) + sum{f in F, s in 1..delta1, u in s..delta1 } (hold[f]*W_0[f,s,u]*(u-s));
	
subject to prec{f in F, t in T}:
	preci[f,t] == (alfa[f] - beta[f]*P[f,t]);
	
subject to crea_inv{f in F, t in T}:
	TInv[f,t] == sum{tt in T: tt != t} W[f,t,tt];
	
#subject to inv_back{f in F, t in T}:
#	TInv[f,t] == sum{tt in T: tt != t} W[f,t,tt];

	 
#subject to crea_inv{f in F, t in 1..delta1}:
#	Inv[f,t] == sum{tt in 1..t: t < TF} W_0[f,t,tt];
	#Inv[f,t] == if (t != tt) then sum{tt = t} W[f,t,tt] else 0;
