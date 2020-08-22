import os
import webbrowser
import pyttsx3

print("Welcome sir/ma'am")
print('How may I help you')

while True:
	print("Which task would you like to perform : " , end='')
	p = input()

	if ((("run" in p) or ("open" in p)) and ("firefox" in p)):
		pyttsx3.speak("opening firefox")
		os.system("firefox")

	elif (("search" in p) and ("web browser" in p)):
		print("What would you like to search ? ", end='')
		q = input()
		pyttsx3.speak("seaching for")
		pyttsx3.speak(q)
		url = "https://www.google.com.tr/search?q={}".format(q) 
		b = webbrowser.get("firefox")
		b.open(url)
	
	elif (("search" in p) and ("youtube" in p)):
		print("What would you like to search ? ", end='')
		q = input()
		pyttsx3.speak("seaching for")
		pyttsx3.speak(q)
		url = "https://www.youtube.com/search?q={}".format(q) 
		b = webbrowser.get("firefox")
		b.open(url)

	elif ((("see" in p) or ("check" in p)) and ("mail" in p)):
		pyttsx3.speak("opening gmail")
		url = "https://mail.google.com/mail/u/0/?q=cisco#inbox"
		b = webbrowser.get("firefox")
		b.open(url)

	elif ((("run" in p) or ("open" in p)) and (("vlc" in p) and ("media player" in p))):
		pyttsx3.speak("opening vlc media player")
		os.system("vlc")

	elif ((("run" in p) or  ("open" in p )) and (("gedit" in p) or ("text editor" in p))):
		pyttsx3.speak("opening text editor")
		os.system("gedit")

	elif (("exit" in p)  or ("quit" in p)):
		pyttsx3.speak("see you soon")
		pyttsx3.speak("have a good day ahead")
		break

	else:
		print("dont support")
