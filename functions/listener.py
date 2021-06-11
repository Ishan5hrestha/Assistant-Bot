import speech_recognition as sr

def listener(lang = 'en-US',howlong=3):
	#ne-NP
	heard = False
	r = sr.Recognizer()
	try:
		with sr.Microphone() as source:
			#while keyboard.is_pressed("up"):
			print("....",end='\r')
			r.adjust_for_ambient_noise(source,duration=0.2)
			audio = r.listen(source,2,howlong)
			heard = True

		if heard:
			print ('_____',end='\r')
			text = r.recognize_google(audio,language = lang)
			text = text.lower()
			heard = False
			return (text)
		return ""
	except sr.UnknownValueError:
		return("bujina")
	except sr.RequestError as e:
		return("Could not request")
	except:
		return("Fatal error aayo")
