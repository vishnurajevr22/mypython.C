import tkinter as tk
import speech_recognition as sr

def recognize_s():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        status_lable.config(text="listening")
        Window.update()
        try:
            audio=recognizer.listen(source,timeout=5)
            text=recognizer.recognize_google(audio)
            result_text.set(text)
            status_lable.congig(text="recognize completed")
        except sr.UnknownValueError:
            result_text.set("could no runderstand")
            status_lable.congig(text="try again")
        
Window=tk.Tk()
Window.title("speech recognize app")
Window.geometry("400x200")
result_text=tk.StringVar()

tk.Label(Window,text="click to speek",font=("Arial",14)).pack()
tk.Button(Window,text="stat lis",command=recognize_s).pack()
tk.Label(Window,textvariable=result_text,wraplength=300,font=("Arial",12)).pack()
status_lable=tk.Label(Window,text="",font=("Arial",10),fg="blue")
status_lable.pack()
Window.mainloop()