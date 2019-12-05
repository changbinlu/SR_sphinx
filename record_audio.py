import speech_recognition as sr
import sphinxbase
import pocketsphinx
r = sr.Recognizer()
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)        # listen to the source
    try:

        text = r.recognize_sphinx(audio,'zh-CN')  # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
    except:
        print("Sorry could not recognize your voice")