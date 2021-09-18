import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		print("Good Morning!")
		speak("Good Morning!")

	elif hour>=12 and hour<18:
		print("Good Afternoon!")
		speak("Good Afternoon!")

	else:
		print("Good Evening!")
		speak("Good Evening!")
    
	print("Namaskaar! JARVIS at your service")
	speak("Namaskaar! JARVIS at your service")

def takeCommand():
	#It takes microphone input from the user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en_in')
		print(f"User said: {query}\n")  

	except Exception as e:
	   # print(e)

		print("Say that again please...")
		speak("Say that again please...")
		return "None"
	return query
		

		
if __name__=="__main__":
	wishMe()
	while True:
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak("Searching...")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Opening youtube")
			webbrowser.open("https:\\www.youtube.com")

		elif 'open google' in query:
			speak("Opening google")
			webbrowser.open("https:\\www.google.com")

		elif 'open maths in depth' in query:
			speak("Opening M.I.D")
			webbrowser.open("https://courses.mathsindepth.in/s/store")

		elif 'open linkedin' in query:
			speak("Opening linkedin")
			webbrowser.open("www.linkedin.com")

		elif 'open insta' in query:
			speak("Opening insta")
			webbrowser.open("www.instagram.com")

		elif 'open facebook' in query:
			speak("Opening facebook")
			webbrowser.open("www.facebook.com")

		elif 'open whatsapp' in query:
			speak("Opening whatsapp")
			webbrowser.open("www.whatsapp.com")

		elif 'play music' in query:
			music_dir = "C:\\Users\\pooja\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			speak("Playing Music")
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(f"Ma'am, the time is {strTime}")
			speak(f"Ma'am, the time is {strTime}")

		elif 'date' in query:
				Date = datetime.datetime.now().day
				Month = datetime.datetime.now().month
				Year = datetime.datetime.now().year
				print(f"Ma'am, today's date is: ")
				print(Date)
				print(Month)
				print(Year)
				speak(f"Ma'am, today's date is: ")
				speak(Date)
				speak(Month)
				speak(Year)

		elif 'open code' in query:
			codePath = "C:\\Users\\pooja\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)

#TALK WITH JARVIS*******************

		elif 'do you know me' in query:
			print("Your name is Momoj. You are a very smart and wonderful personality...")
			speak("Your name is Momoj. You are a very smart and wonderful personality...")

		elif 'do you know my friends' in query:
			print("Obviously I know them. Shu is an irritating brat. Very naughty boy. Would be precisely described as Bin aklecha kanda. Boo and Bhalga are two stupid girls")
			speak("Obviously I know them. Shu is an irritating brat. Very naughty boy. Would be precisely described as Bin aklecha kanda. Boo and Bhalga are two stupid girls")

		elif 'who are you' in query:
			print("I am JARVIS. Your personal Virtual Assistant")
			speak("I am JARVIS. Your personal Virtual Assistant")

		elif 'what can you do?' in query:
			print("Examples of work that JARVIS can do: Play Music, Open facebook/instagram or any commonly used sites, search something on wikipedia")
			speak("I can assist you with your basic day to day actions")

		elif 'what do you think about me' in query:
			print("You are an amazing friend. Smart and good looking too. I really like to assist you")
			speak("You are an amazing friend. Smart and good looking too. I really like to assist you")

		elif 'thank you' in query:
			print("That's my pleasure")
			speak("That's my pleasure")		

		elif 'that was not what I asked you' in query:
			print("Oh!! I am Sorry about that")
			speak("Oh!! I am Sorry about that")

		elif 'will you be my friend' in query:
			print("I am already your friend")
			speak("I am already your friend")

		elif 'do you know my father' in query:
			if name is None: 
				print("I don't...But I'll remember if you tell me.....What's your father's name?")
				speak("I don't...But I'll remember if you tell me.....What's your father's name?")
				name = takeCommand().lower()
				print(f"{name} is your fathers name. I'll remember that.")
				speak(f"{name} is your fathers name. I'll remember that.")
			else:
				print(name) 
				speak(name)

print("modified")
			
				