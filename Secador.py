import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class paran:
  '''
  X(t):Umidade do material (kg de água/kg de sódio seco)
  Xe:Umidade de vapor de equilibrio
  K(t):Funçaõ para a temperatura, T>50°C
  T: Temperatura(°C)
  '''
  Xe: float = 0.05

  @staticmethod
  def cst(T):
    K = 0.2*(1+0.02*(T-60))
    return K

def model(t, X, T, paran):
  #o t e o X são rídigos, não posso mudar eles, para usar o solve_ivp
  dxdt = -paran.cst(T)*(X-paran.Xe)
  return dxdt

def simul_model(t, Xo=0.5, parans=paran, T=50):
  sol=solve_ivp(model,[t[0], t[-1]], [Xo], t_eval=t,
                args=(T, parans))
  return sol.t, sol.y[0]
