# 伝達関数の定義
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
f1 = 8
f2 = 20

# 自分で計算した係数
omega_c = 2 * np.pi * (f1 * f2) ** 0.5
W = 2 * np.pi * (f2 - f1)

num = [W ** 2, 0, 0]
den = [1, 2 ** 0.5 * W, 2 * omega_c ** 2 + W ** 2, 2 ** 0.5 * omega_c ** 2 * W, omega_c ** 4]

w, h = signal.freqs(num, den, worN=np.logspace(-1, 4, 1000))

# signal.butterを用いて計算した係数
b, a = signal.butter(2, [f1 * 2 * np.pi, f2 * 2 * np.pi], btype='bandpass', analog=True)
w1, h1 = signal.freqs(b, a, worN=np.logspace(-1, 4, 1000))

print(num, den)
print(b, a)

plt.subplot(2, 1, 1)
plt.xlim(1, 1000)
plt.semilogx(w / (2 * np.pi), 20 * np.log10(abs(h)))
plt.semilogx(w1 / (2 * np.pi), 20 * np.log10(abs(h1)))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude response [dB]')
plt.grid()
plt.subplot(2, 1, 2)
plt.xlim(1, 1000)
plt.semilogx(w / (2 * np.pi), np.angle(h, deg=True))
plt.semilogx(w1 / (2 * np.pi), np.angle(h1, deg=True))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase response [deg]')
plt.grid()

plt.show()