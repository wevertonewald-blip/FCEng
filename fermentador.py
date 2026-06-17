from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp

@dataclass
class paran:
  '''
  k(T): Cinética (L/min)
  S: Concentração de Glicose (g/L)
  dsdt: Derivada da concentração de glicose (g/L/min)
  t: Tempo (min)
  Tamb: Temperatura ambiente (°C)
  So: Concentração inicial de glicose (g/L)
  '''
  k: float
  S: float
  t: float
  Tamb: float = 35
  k:float
  So: float = 100

def cine(paran):
  k = 464,8*np.exp(-3985/(paran.Tamb+273))
  return k

def conc(t, cine, paran):
  dsdt=paran.S*(-cine.k)
  return dsdt

def sol(t, conc):
  sol=solve_ivp(conc,[t[0], t[-1]], [Xo], t_eval=t, args=(T, parans))
  return sol.t, sol.y[0]
