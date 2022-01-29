import tkinter as tk
import requests
import time

def getWeather(canvas):
    city=textfield.get()
    api="api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=5c21562a6d4120a8102f48feedfaf4be"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)

    final_info=condition + '\n' + str(temp) + 'C'
    final_data="\n" + "Max_temp" + str(max_temp)+ "\n" + "Min_temp" + str(min_temp)
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas=tk.Tk()
canvas.geometry("600*500")
canvas.title("Weather App")

f=("poppins", 15, "bold")
t=("poppins", 35, "bold")

textfield=tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus
textfield.bind('<Return>', getWeather)

label1=tk.Label(canvas, font=t)
label1.pack()
label2=tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()