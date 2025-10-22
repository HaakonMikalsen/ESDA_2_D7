import os
import codecs
import csv
import numpy as np
import dataFinder 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"

dataFile = codecs.open(dir_path+"/data/"+"1v 1khz.csv", encoding="utf-8", errors="ignore")
skipLinesStart = 29
skipLinesEnd = None
t,v1,v2= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()



t = np.array([element for element in t],dtype=float)
v1 = np.array([element for element in v1],dtype=float)
v2 = np.array([element for element in v2],dtype=float)

indexStart =dataFinder.findClosestIndex(v2,0)
t =  t[indexStart:]
v2 = v2[indexStart:]
indexEnd =dataFinder.findClosestIndex(v2[1:],0)
indexEnd =dataFinder.findClosestIndex(v2[indexEnd+10:],0)+indexEnd+11


t =  t[:indexEnd]
v2 = v2[:indexEnd]
print(indexEnd)

plt.figure(figsize=(12,8))
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)



plt.plot(
    t*1000-t[0]*1000,
    v2,
    linewidth=2,
    color="royalblue",
    label="Amplitude respons"
)

# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f V"))
# plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f V"))



plt.xlabel("Tid (ms)", fontsize=12)
plt.ylabel("Spenning [V]", fontsize=12)

plt.title(
    f"Utgang ved påtrykk av sinussignal med 1V amplitude og frekvens 1kHz", fontweight="bold"
)

# plt.xscale("log")
# plt.yscale("log")
# plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()
plt.savefig("./bilder/scope1V1khz.png")
plt.show()

