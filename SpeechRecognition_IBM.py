# use the package speech_recognition
import speech_recognition as sr

# define the function and the parameter audio_input means the path of the audio
# and the txt_output means the path and the name of your output file

def recognize_speech_ibm(audio_input,txt_output):
    r = sr.Recognizer()
    beginner = sr.AudioFile(audio_input)
    with beginner as source:
        audio = r.record(source)
    IBM_KEY = "4b9ZXrpMUL6jo5Q9lw1htmo_Y4xdiku9tydRKVY8Q9Pv"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX


    try:
        # use Microsoft Bing Voice Recognition
        print("IBM Cloud Recognition results:")
        txt = r.recognize_ibm(audio, apikey=IBM_KEY)



         # store the result in a txt file
        if str is bytes:
            result = u"{}".format(txt).encode("utf-8")
        else:
            result = "{}".format(txt)

        with open(txt_output, "a") as f:
            f.write(result)
            print(result)

    except sr.UnknownValueError:
        print("IBM Cloud Recognition could not understand audio")
    except sr.RequestError as error:
        print("Could not request results from IBM Cloud Recognition service; {0}".format(error))
# test this function
recognize_speech_ibm("C:/Users/taotao/Desktop/research/test/female.wav", "C:/Users/taotao/Desktop/research/test/test.txt")