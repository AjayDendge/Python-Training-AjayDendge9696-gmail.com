import os
import pyttsx3
import webbrowser
url = "https://aws.amazon.com/"
url2 = "https://console.cloud.google.com/"


pyttsx3.speak("Welcome to my world")

while True:
	print("Let me know what you want:", end="")
	p=input()

	if (("run" in p) or ("execute" in p) or ("open" in p)) and ("chrome" in p):
 	  os.system("chrome")

	elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
 	  os.system("notepad")

	elif(("run" in p) or ("play" in p) or ("open" in p))and (("media" in p) or ("player" in p)):
	  os.system("wmplayer")

	elif(("run" in p) or ("draw" in p) or ("open" in p))and ("paint" in p):
	  os.system("mspaint")

	elif(("run" in p) or ("execute" in p) or ("open" in p))and ("powershell" in p):
	  os.system("powershell")

	elif(("open" in p) or ("start" in p)) and ("aws" in p) and ("console"):
          webbrowser.open(url)

	elif(("open" in p) or ("start" in p)) and ("gcp" in p) and ("console"):
          webbrowser.open(url2)

	elif("quit" in p) or ("stop" in p) or ("exit" in p):
	  break

	else:
	  print("don't support")
