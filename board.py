# -*- coding: utf-8 -*-
from scipy import signal
from cmath import pi
from math import tan, sqrt
import matplotlib.pyplot as plt

# 伝達関数の定義

f1 = 8
f2 = 20

omega_c = 2 * pi * (f1 * f2) ** 0.5
w = 2 * pi * (f2 - f1)

num = [w ** 2, 0, 0] # 分子の係数
den = [1, 2 ** 0.5 * w, 2 * omega_c ** 2 + w ** 2, 2 ** 0.5 * omega_c ** 2 * w, omega_c ** 4] # 分母の係数
G = signal.lti(num, den)
print(2400 % (360))
# ボード線図の計算
w, mag, phase = signal.bode(G)

# ゲイン線図の描画
plt.subplot(2, 1, 1)
plt.semilogx(w / 2 / pi, mag)
plt.ylabel("Gain[dB]")
plt.xlim(1, 30)
plt.grid()

# 位相線図の描画
plt.subplot(2, 1, 2)
plt.semilogx(w / 2 / pi, phase)
plt.xlabel("w[rad/sec]")
plt.ylabel("Phase[deg]")
plt.xlim(1, 30)
plt.grid()
plt.show()