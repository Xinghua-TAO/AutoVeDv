# use the package speech_recognition
import speech_recognition as sr

# define the function and the parameter audio_input means the path of the audio
# and the txt_output means the path and the name of your output file

def recognize_speech_w(audio_input,txt_output):
    r = sr.Recognizer()
    beginner = sr.AudioFile(audio_input)
    with beginner as source:
        audio = r.record(source)

    WIT_KEY = "HV7TA5VZIFRLT3PBPGE3WNGD7J3COYC7"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        # use Wit API
        print("Wit results:")
        txt = r.recognize_wit(audio, key=WIT_KEY)

         # store the result in a txt file
        if str is bytes:
            result = u"{}".format(txt).encode("utf-8")
        else:
            result = "{}".format(txt)

        with open(txt_output, "a") as f:
            f.write(result)
            print(result)

    except sr.UnknownValueError:
        print("Wit Recognition could not understand audio")
    except sr.RequestError as error:
        print("Could not request results from Wit Recognition service; {0}".format(error))
# test this function
recognize_speech_w("C:/Users/taotao/Desktop/research/test/car.wav", "C:/Users/taotao/Desktop/research/test/car(w).txt")
