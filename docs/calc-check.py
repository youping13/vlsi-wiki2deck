"""驗算 wiki 裡所有標「（計算）」的數字。執行：python docs/calc-check.py（全部通過才算數）"""
import math

def check(name, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"{'OK ' if ok else 'BAD'} {name}: 算出 {got:.4g}，wiki 寫 {want}")
    return ok

n = 10
e_conv = sum(2 ** (n + 1 - 2 * i) * (2 ** i - 1) for i in range(1, n + 1))
e_mono = sum(2 ** (n - 2 - i) for i in range(1, n))
lsb = 1.2 / 1024
q = lsb / math.sqrt(12)
enob = (57.0 - 1.76) / 6.02
results = [
    # switching-schemes
    check("式(1) n=10 E_conv [CVref²]", e_conv, 1363.3, 0.05),
    check("式(2) n=10 E_mono [CVref²]", e_mono, 255.5, 0.05),
    check("省電比例 1-255.5/1363.3", 1 - e_mono / e_conv, 0.813, 0.001),
    # quantization-noise-snr
    check("量化雜訊 RMS [mV]（不四捨五入）", q * 1e3, 0.338, 0.0005),
    check("A 的 SNR [dB]", 20 * math.log10(0.6 / math.sqrt(2) / q), 61.97, 0.01),
    check("B 的 SNR [dB]", 20 * math.log10(0.3 / math.sqrt(2) / q), 55.95, 0.01),
    check("B 的比值 0.212/0.34e-3", 0.212 / 0.34e-3, 624, 1),
    check("B 的 SNR 20log(624)", 20 * math.log10(0.212 / 0.34e-3), 55.9, 0.05),
    check("6.02×10+1.76", 6.02 * 10 + 1.76, 61.96, 0.001),
    check("6.02×9+1.76", 6.02 * 9 + 1.76, 55.94, 0.001),
    # adc-architectures
    check("4-bit Flash 比較器 2^4-1", 2 ** 4 - 1, 15, 0),
    check("2-2 two-step 比較器 2×(2^2-1)", 2 * (2 ** 2 - 1), 6, 0),
    # adc-dynamic-parameters
    check("ENOB = (57.0-1.76)/6.02", enob, 9.18, 0.005),
    check("2^9.18", 2 ** 9.18, 580, 1),
    check("FoM [fJ] = 0.826mW/(2^9.18·50MHz)", 0.826e-3 / (2 ** 9.18 * 50e6) * 1e15, 28.5, 0.05),
]
print("全部通過" if all(results) else "有錯，先修 wiki")
raise SystemExit(0 if all(results) else 1)
