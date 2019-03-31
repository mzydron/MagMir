import tkinter as tk
import time
from WeatherWidget import ApiCaller


class Utilities:
    weatherApi = ApiCaller()


class TimeWidget(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.Time = tk.StringVar()
        self.LastUpdated = tk.StringVar()
        tk.Label(self, textvariable=self.Time, background='black', fg='white', font=('Helvetica', 40)).pack()

        def getTime():
            self.currentTime = time.strftime("%H:%M:%S")
            self.Time.set(self.currentTime)
            self.after(1000, getTime)

        getTime()


class TemperatureWidget(tk.Frame):

    def __init__(self, *args, **kwargs):
        # Current Temperature
        tk.Frame.__init__(self, *args, **kwargs)
        self.Temperature = tk.StringVar()
        self.weatherWidget = Utilities.weatherApi
        tk.Label(self, textvariable=self.Temperature, background='black', fg='white', font=('Helvetica', 20)).pack()


        def getTemperature():
            self.currentTemperature = self.weatherWidget.getCurrentTemp()
            self.Temperature.set("{0} °C".format(self.currentTemperature))
            self.after(600000, getTemperature)

        self.TemperatureF1 = tk.StringVar()
        self.TemperatureF2 = tk.StringVar()
        self.TemperatureF3 = tk.StringVar()

        tk.Label(self, textvariable=self.TemperatureF1, background='black', fg='white', font=('Helvetica', 15)).pack()
        tk.Label(self, textvariable=self.TemperatureF2, background='black', fg='white', font=('Helvetica', 15)).pack()
        tk.Label(self, textvariable=self.TemperatureF3, background='black', fg='white', font=('Helvetica', 15)).pack()

        def getFutureTemperature():
            self.TemperatureF1.set("{0} °C".format(self.weatherWidget.getFutureTemp(1)))
            self.TemperatureF2.set("{0} °C".format(self.weatherWidget.getFutureTemp(2)))
            self.TemperatureF3.set("{0} °C".format(self.weatherWidget.getFutureTemp(3)))
            self.after(600000, getFutureTemperature)

        getTemperature()
        getFutureTemperature()


class WeatherIcon(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        def weatherIcon():
            try:
                iconName = Utilities.weatherApi.getIconCode()
                if not iconName:
                    iconName = "default.gif"

                self.weatherIcon = tk.PhotoImage(file=iconName)
                tk.Label(self, image=self.weatherIcon, borderwidth=0).pack()

            except Exception as e:
                print("No suitable icon for : {}".format(e))

        weatherIcon()


root = tk.Tk()
TimeWidget().place(relx=0.4, rely=0.03, anchor='w')
TemperatureWidget().place(relx=0.93, rely=0.025, anchor='w')
WeatherIcon().place(relx=0.9, rely=0.028, anchor='w')


def close(event):
    root.quit()
    root.destroy()
    exit()

root.bind('<Escape>', close)
root.attributes('-fullscreen', True)
root.configure(background="black")
root.mainloop()
