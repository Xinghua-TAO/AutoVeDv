# use the package speech_recognition
import speech_recognition as sr

# define the function and the parameter audio_input means the path of the audio
# and the txt_output means the path and the name of your output file

def recognize_speech_m(audio_input,txt_output):
    r = sr.Recognizer()
    beginner = sr.AudioFile(audio_input)
    with beginner as source:
        audio = r.record(source)

    try:
        # use Microsoft Bing Voice Recognition
        print("Microsoft Bing Voice Recognition results:")
        BING_KEY = "c685b1b235824d2bbaaa0078a4f420a8"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
        txt = r.recognize_bing(audio, key=BING_KEY)


         # store the result in a txt file
        if str is bytes:
            result = u"{}".format(txt).encode("utf-8")
        else:
            result = "{}".format(txt)

        with open(txt_output, "a") as f:
            f.write(result)
            print(result)

    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as error:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(error))
# test this function
recognize_speech_m("C:/Users/taotao/Desktop/research/test/car.wav", "C:/Users/taotao/Desktop/research/test/car(m).txt")
