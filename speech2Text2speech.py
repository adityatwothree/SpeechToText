import speech_recognition as sr 
import pyttsx3 
from tkinter import *
from gtts import gTTS 
import os 


def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 

def stop():
	root.destroy()
	os._exit(0)	

def play(): 
	global flag
	while True:	 

		try: 
			
			with sr.Microphone() as source2: 
				

				r.adjust_for_ambient_noise(source2, duration=0.2) 

				audio2 = r.listen(source2) 
				
				# Using ggogle to recognize audio 
				MyText = r.recognize_google(audio2) 
				MyText = MyText.lower() 
				if "terminate" in MyText :
					root.destroy()
					os._exit(0)
				
				with open('inputText.txt', 'a') as f:
					if 'terminate' not in MyText:
						f.write(MyText) 
				print("You Said "+MyText) 
				SpeakText(MyText) 
				
		except sr.RequestError as e: 
			print("Could not request results; {0}".format(e)) 
			
		except sr.UnknownValueError: 
			print("unknown error occured") 

r = sr.Recognizer() 
flag = True
root = Tk() 

frame1 = Frame(root, 
			bg = "lightPink", 
			height = "150") 


frame1.pack(fill = X) 


frame2 = Frame(root, 
			bg = "lightgreen", 
			height = "750") 
frame2.pack(fill=X) 


label = Label(frame1, text = "Speech to Text", 
			font = "bold, 30", 
			bg = "lightpink") 

label.place(x = 180, y = 70) 

btn = Button(frame2, text = "START", 
			width = "15", pady = 10, 
			font = "bold, 15", 
			command = play, bg='yellow') 

btn.place(x = 250, y = 130) 

btn = Button(frame2, text = "STOP", 
			width = "15", pady = 10, 
			font = "bold, 15", 
			command = stop, bg='yellow') 

btn.place(x = 250, y = 200) 

root.title("Speech to text convertor") 

root.geometry("650x550+350+200") 

# start the gui 
root.mainloop() 


