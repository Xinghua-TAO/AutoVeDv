# use the package speech_recognition
import speech_recognition as sr

# define the function and the parameter audio_input means the path of the audio
# and the txt_output means the path and the name of your output file

def recognize_speech_h(audio_input,txt_output):
    r = sr.Recognizer()
    beginner = sr.AudioFile(audio_input)
    with beginner as source:
        audio = r.record(source)

    HOUNDIFY_CLIENT_ID = "OY4XbrF34ntmOQmlher4Uw=="  # Houndify client IDs are Base64-encoded strings
    HOUNDIFY_CLIENT_KEY = "RkVECP2PWXw5h2SpTMbjlu4G16PZANwgj3eDM1JMUrZdbSlE__A7pYGhcWuFuqxJ1QKHB0PAYtzGWSfg8uhHow=="  # Houndify client keys are Base64-encoded strings
    try:
        # use Houndify API
        print("Houndify results:")
        txt = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)

         # store the result in a txt file
        if str is bytes:
            result = u"{}".format(txt).encode("utf-8")
        else:
            result = "{}".format(txt)

        with open(txt_output, "a") as f:
            f.write(result)
            print(result)

    except sr.UnknownValueError:
        print("Houndify Recognition could not understand audio")
    except sr.RequestError as error:
        print("Could not request results from Houndify Recognition service; {0}".format(error))
# test this function
recognize_speech_h("C:/Users/taotao/Desktop/research/test/car.wav", "C:/Users/taotao/Desktop/research/test/car(h).txt")
