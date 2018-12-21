from watson_developer_cloud import SpeechToTextV1
import json
import pandas as pd


def recognize_speech_ibm_plus(yourkey, url_address, audio_input, csv_output):
    # set your authorization
    speech_to_text = SpeechToTextV1(
        iam_apikey=yourkey,
        url=url_address
    )

    # use IBM API to recognize your audio
    files = audio_input
    with open(files, 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            model="en-US_NarrowbandModel",
            # there are 8 models in the IMB API, check their website and get the most suitable one
            content_type='audio/wav',  # the format of your audio and wav is a recommended one
            timestamps=True,  # choose if you want to get the onset and offset of your transcription
        ).get_result()

    # since the result is sent to a url in json, you need to download it
    with open("C:/Users/taotao/Desktop/research/test/data.json", "w") as write_file:
        json.dump(speech_recognition_results, write_file)
    data = r"C:/Users/taotao/Desktop/research/test/data.json"

    # Read and convert json to dictionary
    def js_r(data):
        with open(data, encoding='utf-8') as f_in:
            return (json.load(f_in))
    my_dic_data = js_r(data)

    # make sure you remember the audio you opened and double check
    print(audio_input)

    # pick the lists we need from the dictionary and combine them in one list
    dict_step1 = my_dic_data['results']
    words = []
    for n in dict_step1:
        sentence = n['alternatives'][0]['timestamps']
        words = words + sentence

    # change the list we get to a table and add a head to it
    list_headline = ['word', 'onset', 'offset']
    table = pd.DataFrame(columns=list_headline, data=words)
    table[['onset']] = table[['onset']]*1000
    table[['offset']] = table[['offset']]*1000

    # to fit this table with datavyu, we need to change the order of the columns
    table = table[['onset', 'offset', 'word']]
    print(table)

    # store the table in a csv file
    table.to_csv(csv_output)




recognize_speech_ibm_plus('4b9ZXrpMUL6jo5Q9lw1htmo_Y4xdiku9tydRKVY8Q9Pv',
                          'https://stream.watsonplatform.net/speech-to-text/api',
                          "C:/Users/taotao/Desktop/research/test/HHcut.wav",
                          "C:/Users/taotao/Desktop/research/test/HHcut.csv")
