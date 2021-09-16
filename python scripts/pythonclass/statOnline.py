import tkinter as tk
import math
from scipy.stats import norm


def compute():
    #Read from data input fields
    Q = float(entry_q.get())
    df = float(entry_df.get())

    #Formulas
    K = df + 1
    level = 95
    levelci = level * 0.005 + 0.50

    if Q >= K:
        SElnH = 0.5 * ((math.log(Q) - math.log(df)) / (math.sqrt(2 * Q) - math.sqrt(2 * K - 3)))
    else:
        SElnH = math.sqrt((1 / (2 * (K - 2)) * (1 - 1 / (3 * (K - 2) ** 2))))

    H2 = (Q / df)

    I2 = (100 * (Q - df)) / Q
    I22 = (H2 - 1) / H2
    varI2 = 4 * SElnH ** 2 / math.exp(4 * math.log(math.sqrt(H2)))
    I2_LL = (I22 - norm.ppf(levelci) * math.sqrt(varI2)) * 100
    I2_UL = (I22 + norm.ppf(levelci) * math.sqrt(varI2)) * 100

    entry_I2.configure(text=str(I2))
    entry95LL.configure(text=str(I2_LL))    
    entry95UL.configure(text=str(I2_UL))

window = tk.Tk()

window.title("Heterogi")
window.geometry("400x400")

#Data input fields
label_q = tk.Label(window, text="Q: ")
label_q.grid(row=0, sticky="E")
label_df = tk.Label(window, text="df: ")
label_df.grid(row=1, sticky="E")

entry_q = tk.Entry(window)
entry_q.grid(row=0, column=1)
entry_df = tk.Entry(window)
entry_df.grid(row=1, column=1)


#Compute button
button = tk.Button(text="Compute", bg="red", command=compute)
button.grid(row=2, column=1)

#Results fields
label_I2 = tk.Label(window, text="I2: ")
label_I2.grid(row=4, sticky="E")
label_95LL = tk.Label(window, text="95% LL: ")
label_95LL.grid(row=4, column=2)
label_95UL = tk.Label(window, text="95% UL: ")
label_95UL.grid(row=5, column=2)

entry_I2 = tk.Label(window, width=15, height=1, bg="light grey")
entry_I2.grid(row=4, column=1)
entry95LL = tk.Label(window, width=15, height=1, bg="light grey")
entry95LL.grid(row=4, column=3)
entry95UL = tk.Label(window, width=15, height=1, bg="light grey")
entry95UL.grid(row=5, column=3)

window.mainloop()
share