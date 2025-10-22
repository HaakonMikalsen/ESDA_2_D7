import os
import codecs
import csv
import numpy as np
import dataFinder 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"

dataFile = codecs.open(dir_path+"/data/"+"frekvREsponFull.csv", encoding="utf-8", errors="ignore")
skipLinesStart = 27
skipLinesEnd = 256
f,A= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()



f = np.array([element for element in f],dtype=float)
A = np.array([element for element in A],dtype=float)

plt.figure(figsize=(12,8))
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)


plt.plot(
    f,
    A,
    linewidth=2,
    color="royalblue",
    label="Amplitude respons"
)

# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f V"))
# plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f V"))



plt.xlabel("Frekvens [Hz]", fontsize=12)
plt.ylabel("Amplitude [dB]", fontsize=12)

plt.title(
    f"Amplituderespons med punkter ved 1V", fontweight="bold"
)

plt.xscale("log")
# plt.yscale("log")
plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()
plt.savefig("./bilder/Aprespons.png")
plt.show()