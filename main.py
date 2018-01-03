import speech_recognition as sr
 
# To Record Audio

r = sr.Recognizer()
audio = None
def listen():
    with sr.Microphone() as source:
        print("Say something!")
        global audio
        audio = r.listen(source)
 
listen()
try:
    output = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Sorry I did not understand! Can you say it again?")
    listen()
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# if output is not undefined
try:
    output
except NameError:
    print ("Oops there is an error in audio output :(")
else:
    print(output)
  


