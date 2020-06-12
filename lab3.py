# Laba3. DFT

import sys
sys.path.append('../lab1')

import numpy as np
import matplotlib.pyplot as plt
import math

from random import random
from lab1 import generate_signal, draw, DrawOption, N, n, w, A, x

def dft(signal):
  def factor(pk, n):
    angle = -2 * math.pi / n * pk
    return complex(math.cos(angle), math.sin(angle))

  length = len(signal)
  result = np.zeros(length, dtype=complex)

  for p in range(length):
    for k in range(length):
      result[p] += factor(p * k, length) * signal[k]

  real, image = np.array([i.real for i in result]), np.array([i.imag for i in result])
  return real, image

def main_fn():
  signal = np.array([generate_signal(i) for i in range(N)])
  real, image = dft(signal)
  options = [
    DrawOption("Signal", "plot"),
    DrawOption("DFT: Real", "bar"),
    DrawOption("DFT: Imaginary", "bar")
  ]
  draw([signal, real, image], options, "lab3.png")

if __name__ == '__main__':
  main_fn()