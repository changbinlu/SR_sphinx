import speech_recognition as sr
import sphinxbase
import pocketsphinx
from glob import glob
from api_getaudio import *
def predict():
    files = glob('data/*.wav')
    r = sr.Recognizer()
    sum = len(files)
    count = 0
    for f in files:
        test = sr.AudioFile(f)
        with test as source:
            audio = r.record(source)
            result = r.recognize_sphinx(audio, language='zh-CN')
            target = f[5:].split('_')[0]
            print('Expected:' + target, 'Output:' + result)
            if target == result:
                count += 1

    print('Accuracy:', float(count / sum))
def predict_single(word):
    # generate wav fuke
    baidu_api(client, [word])
    # recognize
    r = sr.Recognizer()
    path = './baidu/' + word + '_发音人3.wav'
    test = sr.AudioFile(path)

    with test as source:
        audio = r.record(source)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio,language='nurse_model'))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

if __name__ == '__main__':
    # test
    word = '体重一百二十,舒张压一百二十,舒张压一百二十,舒张压一百二十'
    predict_single(word)