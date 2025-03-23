import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def concentration(x, y, z, H, Q, k, sigma_y, sigma_z, V_s):
    term1 = Q / (2 * np.pi * k * sigma_y * sigma_z)
    term2 = np.exp(-y**2 / (2 * sigma_y**2))
    term3 = np.exp(-(z - H + (V_s * x) / H)**2 / (2 * sigma_z**2))
    term4 = np.exp(-(z + H - (V_s * x) / H)**2 / (2 * sigma_z**2))
    return term1 * term2 * (term3 + term4)

def calculate_and_plot():
    try:
        Q = float(entry_Q.get())
        k = float(entry_k.get())
        sigma_y = float(entry_sigma_y.get())
        sigma_z = float(entry_sigma_z.get())
        V_s = float(entry_V_s.get())
        H = float(entry_H.get())

        x = np.linspace(-1000, 1000, 100)
        y = np.linspace(-100, 100, 100)
        z = np.linspace(-1000, 1000, 100)
        X, Y, Z = np.meshgrid(x, y, z)
        C = concentration(X, Y, Z, H, Q, k, sigma_y, sigma_z, V_s)

        z_index = np.argmin(np.abs(z - 0))
        fig, ax = plt.subplots()
        contour = ax.contourf(X[:, :, z_index], Y[:, :, z_index], C[:, :, z_index], levels=50, cmap='viridis')
        plt.colorbar(contour, ax=ax, label='Концентрация')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Концентрация при z=0')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

    except ValueError as e:
        result_label.config(text=f"Ошибка: {e}")
window = tk.Tk()
window.title("Расчет концентрации")
tk.Label(window, text="Q (источник):").grid(row=0, column=0)
entry_Q = tk.Entry(window)
entry_Q.grid(row=0, column=1)

tk.Label(window, text="k (коэффициент):").grid(row=1, column=0)
entry_k = tk.Entry(window)
entry_k.grid(row=1, column=1)

tk.Label(window, text="sigma_y (стандартное отклонение по y):").grid(row=2, column=0)
entry_sigma_y = tk.Entry(window)
entry_sigma_y.grid(row=2, column=1)
tk.Label(window, text="sigma_z (стандартное отклонение по z):").grid(row=3, column=0)
entry_sigma_z = tk.Entry(window)import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def concentration(x, y, z, H, Q, k, sigma_y, sigma_z, V_s):
    term1 = Q / (2 * np.pi * k * sigma_y * sigma_z)
    term2 = np.exp(-y**2 / (2 * sigma_y**2))
    term3 = np.exp(-(z - H + (V_s * x) / H)**2 / (2 * sigma_z**2))
    term4 = np.exp(-(z + H - (V_s * x) / H)**2 / (2 * sigma_z**2))
    return term1 * term2 * (term3 + term4)

def calculate_and_plot():
    try:
        Q = float(entry_Q.get())
        k = float(entry_k.get())
        sigma_y = float(entry_sigma_y.get())
        sigma_z = float(entry_sigma_z.get())
        V_s = float(entry_V_s.get())
        H = float(entry_H.get())

        x = np.linspace(-1000, 1000, 100)
        y = np.linspace(-100, 100, 100)
        z = np.linspace(-1000, 1000, 100)
        X, Y, Z = np.meshgrid(x, y, z)
        C = concentration(X, Y, Z, H, Q, k, sigma_y, sigma_z, V_s)

        z_index = np.argmin(np.abs(z - 0))
        fig, ax = plt.subplots()
        contour = ax.contourf(X[:, :, z_index], Y[:, :, z_index], C[:, :, z_index], levels=50, cmap='viridis')
        plt.colorbar(contour, ax=ax, label='Концентрация')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Концентрация при z=0')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

    except ValueError as e:
        result_label.config(text=f"Ошибка: {e}")
window = tk.Tk()
window.title("Расчет концентрации")
tk.Label(window, text="Q (источник):").grid(row=0, column=0)
entry_Q = tk.Entry(window)
entry_Q.grid(row=0, column=1)

tk.Label(window, text="k (коэффициент):").grid(row=1, column=0)
entry_k = tk.Entry(window)
entry_k.grid(row=1, column=1)

tk.Label(window, text="sigma_y (стандартное отклонение по y):").grid(row=2, column=0)
entry_sigma_y = tk.Entry(window)
entry_sigma_y.grid(row=2, column=1)
tk.Label(window, text="sigma_z (стандартное отклонение по z):").grid(row=3, column=0)
entry_sigma_z = tk.Entry(window)
entry_sigma_z.grid(row=3, column=1)
tk.Label(window, text="V_s (скорость):").grid(row=4, column=0)
entry_V_s = tk.Entry(window)
entry_V_s.grid(row=4, column=1)
tk.Label(window, text="H (высота):").grid(row=5, column=0)
entry_H = tk.Entry(window)
entry_H.grid(row=5, column=1)
calculate_button = tk.Button(window, text="Рассчитать и построить график", command=calculate_and_plot)
calculate_button.grid(row=6, column=0, columnspan=2)
result_label = tk.Label(window, text="")
result_label.grid(row=8, column=0, columnspan=2)
window.mainloop()

entry_sigma_z.grid(row=3, column=1)
tk.Label(window, text="V_s (скорость):").grid(row=4, column=0)
entry_V_s = tk.Entry(window)
entry_V_s.grid(row=4, column=1)
tk.Label(window, text="H (высота):").grid(row=5, column=0)
entry_H = tk.Entry(window)
entry_H.grid(row=5, column=1)
calculate_button = tk.Button(window, text="Рассчитать и построить график", command=calculate_and_plot)
calculate_button.grid(row=6, column=0, columnspan=2)
result_label = tk.Label(window, text="")
result_label.grid(row=8, column=0, columnspan=2)
window.mainloop()
