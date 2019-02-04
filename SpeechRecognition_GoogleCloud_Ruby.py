def transcribe_gcs_with_word_time_offsets(speech_file):
    import io
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-UK',
        enable_word_time_offsets=True)

    operation = client.long_running_recognize(config, audio)

    result = operation.result(timeout=90)

    for result in result.results:
        alternative = result.alternatives[ 0 ]

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print('{}, {}, {}'.format(
                word,
                start_time.seconds * 1000 + start_time.nanos * 1e-6,
                end_time.seconds * 1000 + end_time.nanos * 1e-6))


transcribe_gcs_with_word_time_offsets("C:/Users/taotao/Desktop/research/test/HHcut.wav")