import pyttsx3
"""Function to add speech functionality to program"""
def speech(a):
	print(a)
	engine=pyttsx3.init()
	voices=engine.getProperty('voices')
	engine.setProperty('rate',120)
	engine.setProperty('volume',1.0)
	engine.setProperty('voice',voices[0].id)
	engine.say(a)
	engine.runAndWait()
speech("hey you ! i'm working  My name is chatbotlive")
