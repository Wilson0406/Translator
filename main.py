from playsoung import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

dic = ('afrikaans', 'af',
       'amharic', 'am', 'arabic', 'ar',
       'azerbaijani', 'az', 'belarusian', 'be',
       'bulgarian', 'bg', 'bengali', 'bn',
       'bosnian', 'bs', 'catalan', 'ca',
       'cebuano', 'ceb', 'corsican', 'co',
       'czech', 'cs', 'welsh', 'cy',
       'danish', 'da', 'german', 'de',
       'greek', 'el', 'english', 'en',
       'esperanto', 'eo', 'spanish', 'es',
       'estonian', 'et', 'basque', 'eu',
       'persian', 'fa', 'finnish', 'fi',
       'french','fr', 'frisian', 'fy',
       'irish', 'ga', 'scots gaelic', 'gd',
       'galician', 'gl', 'gujarati', 'gu',
       'hausa', 'ha', 'hawaiian', 'haw',
       'hebrew', 'he', 'hindi', 'hi',
       'hmong', 'hmn', 'croatian', 'hr',
       'haitian creole', 'hr', 'hungarian', 'hu',
       'armenian', 'hy', 'indonesian', 'id',
       'igbo', 'ig', 'icelandic', 'is',
       'italian', 'it', 'hebrew', 'iw',
       'japanese', 'ja', 'javanese', 'jw',
       'georgian', 'ka', 'kazakh', 'kk',
       'khmer', 'km', 'kannada', 'kn',
       'korean', 'ko', 'kurdish (kurmanji)', 'ku',
       'kyrgyz', 'ky', 'latin', 'la',
       'luxembourgish', 'lb', 'lao', 'lo',
       'lithuanian', 'lt', 'latvian', 'lv',
       'malagasy', 'mg', 'maori', 'mi',
       'macedonian', 'mk', 'malayalam', 'ml',
       'mongolian', 'mn', 'marathi', 'mr',
       'malay', 'ms', 'maltese', 'mt',
       'myanmar (burmese)', 'my', 'nepali', 'ne',
       'dutch', 'nl', 'norwegian', 'no',
       'chichewa', 'ny', 'odia', 'or',
       'punjabi', 'pa', 'polish', 'pl',
       'pashto', 'ps', 'portugese', 'pt',
       'romanian', 'ro', 'russian', 'ru',
       'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'samoan', 'sm', 'shona', 'sn',
       'somali', 'so', 'albanian', 'sq',
       'serbian', 'sr', 'sesotho', 'st',
       'sundanese', 'su', 'swedish', 'sv',
       'swahili', 'sw', 'tamil', 'ta',
       'telegu', 'te', 'tajik', 'tg',
       'thai', 'th', 'filipino', 'tl',
       'turkish', 'tr', 'uyghur', 'ug',
       'ukrainian', 'uk', 'urdu', 'ur',
       'uzbek', 'uz', 'vietnamese', 'vi',
       'xhosa', 'xh', 'yiddish', 'yi',
       'yoruba', 'yo', 'chinese (simplified)', 'zh-cn',
       'chinese (traditional)', 'ch-tw', 'zulu', 'zu')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")
    except Exception as e:
        print("Say thah again please...)
              return "None"
    return query

query = takecommand()
while(query == "None"):
    query = takecommand()


def destination_language():
    print("Enter the language in which you want to translate(Eg: hindi, bengali, gujrati, etc): ")
    print()

    to_lang = takecommand()
    while(to_lang == "None"):
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang

to_lang = destination_language()

while(to_lang not in dic):
    print("Language in which you are trying to translate  is currently not available, please input some other language: ")
    print()
    to_lang = destination_lang()

to_lang = dic[dic.index(to_lang)+1]

translator = Translator()

text_to_translate = translator.translate(query, dest=to_lang)
text = text_to_translate.text

speak = sTTS(text=text, lang=to_lang, slow=False)

speak.save("captured_voice.mp3")

playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')
print(text)
