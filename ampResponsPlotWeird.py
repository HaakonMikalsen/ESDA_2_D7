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
skipLinesEnd = -2
f,A= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()


f = np.array([element for element in f],dtype=float)
A = np.array([element for element in A],dtype=float)


plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=f[0], color="black", linewidth=1)



plt.plot(
    f,
    A,
    linewidth=2,
    color="royalblue",
    label="Amplitude respons"
)
# plt.plot(
#     t,
#     noise,
#     linewidth=2,
#     color="crimson",
#     label="vo"
# )

# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f V"))
# plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f V"))



plt.xlabel("frekvens [Hz]", fontsize=12)
plt.ylabel("Amplitude [dB]", fontsize=12)

plt.title(
    f"Amplituderespons med 1V", fontweight="bold"
)

plt.xscale("log")
# plt.yscale("log")
# plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()




# plt.show()
# plt.plot(
#     np.linspace(0,len(vivo[1]),len(vivo[1])),
#     vivo[1]-V0,
#     linewidth=2,
#     color="royalblue",
#     label="vi"
# )
plt.savefig("./bilder/ApresponsWeird.png")
plt.show()