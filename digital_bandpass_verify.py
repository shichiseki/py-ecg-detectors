# 伝達関数の定義
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 250
f1 = 8
f2 = 20
omega_c = 2 * np.pi * (f1 * f2) ** 0.5
W = 2 * np.pi * (f2 - f1)

omega_c_p = np.sqrt(np.tan(np.pi * f2 / fs) * np.tan(np.pi * f1 / fs))
W_p = np.tan(np.pi * f2 / fs) - np.tan(np.pi * f1 / fs)

# 自分で計算した係数
z4 = 1 + np.sqrt(2) * W_p + 2 * omega_c_p ** 2 + W_p ** 2 + np.sqrt(2) * omega_c_p ** 2 * W_p + omega_c_p ** 4
z3 = -4 - 2 * np.sqrt(2) * W_p * (1 - omega_c_p ** 2) + 4 * omega_c_p ** 4
z2 = 6 - 2 * (2 * omega_c_p ** 2 + W_p ** 2) + 6 * omega_c_p ** 4
z1 = -4 + 2 * np.sqrt(2) * W_p * (1 - omega_c_p ** 2) + 4 * omega_c_p ** 4
z0 = 1 - np.sqrt(2) * W_p + 2 * omega_c_p ** 2 + W_p ** 2 - np.sqrt(2) * omega_c_p ** 2 * W_p + omega_c_p ** 4

num = [W_p ** 2 / z4, 0, -2 * W_p ** 2 / z4, 0, W_p ** 2 / z4]
den = [1, z3 / z4, z2 / z4, z1 / z4, z0 / z4]

# w, h = signal.freqz(num, den, worN=np.logspace(-2, 4, 1000))
w, h = signal.freqz(num, den)

# signal.butterを用いて計算した係数
b, a = signal.butter(2, [f1 / fs * 2, f2 / fs * 2], btype='bandpass')
w1, h1 = signal.freqz(b, a)

print(num, den)
print(b, a)

plt.subplot(2, 1, 1)
# plt.xlim(0, 1)
plt.plot(w / np.pi, 20 * np.log10(abs(h)))
plt.plot(w1 / np.pi, 20 * np.log10(abs(h1)))
plt.xlabel('Frequency [-]')
plt.ylabel('Amplitude response [dB]')
plt.grid()
plt.subplot(2, 1, 2)
# plt.xlim(0, 1)
plt.plot(w / np.pi, np.angle(h, deg=True))
plt.plot(w1 / np.pi, np.angle(h1, deg=True))
plt.xlabel('Frequency [-]')
plt.ylabel('Phase response [deg]')
plt.grid()

plt.show()