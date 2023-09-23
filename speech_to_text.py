# coding: iso-8859-1
#importing modules

import streamlit as st
import speech_recognition as sr
import pyaudio
from PIL import Image
from gtts import gTTS
from googletrans import Translator
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
from pytube import extract
from googletrans import Translator, constants
from playsound import playsound
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from pprint import pprint



from translate import Translator


#application function for speech to text converter page
def application():
    #function for converting microphone speech input to text
    def main(output):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            st.header("Please say something...")
            audio = r.listen(source)
            try:
                query = st.write("You have said: \n" + r.recognize_google(audio))

                #translating from one language to our desired language and
                #dislaying the translation by taking desired language(output)
                #as argument








                translator = Translator(to_lang=output)
                translation = translator.translate(r.recognize_google(audio))
                st.header(f"Your translated text to {output} is: ")
                st.write(translation)


                obj = gTTS(text=translation,  slow=False)

                # Here we are saving the transformed audio in a mp3 file named
                # venky.mp3
                obj.save("venky.mp3")

                # Play the exam.mp3 file
                playsound("venky.mp3")

                os.remove("venky.mp3")







            except Exception as e:
                st.write("Error: " + str(e))
            return query







    #function for converting URL input to transcript
    #this contains both taking url as argument and extracting youtube id to convert
    #to text
    def main1(url):

        vid_id = extract.video_id(url)
        data = yta.get_transcript(vid_id)

        transcript = " "
        for value in data:
            for key, val in value.items():
                if key == "text":
                    transcript += val
        l = transcript.splitlines()
        data=(" ".join(l))
        final_tra =st.write(" ".join(l))


        obj = gTTS(text=data, slow=False)

        # Here we are saving the transformed audio in a mp3 file named
        # venky.mp3
        #obj.save("venky.mp3")

        # Play the exam.mp3 file
        #playsound("venky.mp3")

        #os.remove("venky.mp3")




        return final_tra

    #application interface

    st.title("Speech-to-Text Converter")

    image = Image.open('C:\\Users\\sammu\\Pictures\\speech.jpeg')
    st.image(image)

    option = st.selectbox("How would you like to convert ?",
                          ('URL', 'Microphone'))
    st.write("You selected: ", option)
    if option == 'URL':
        url = st.text_input("Enter your URL")





    if option == 'Microphone' :

        #Available languages in application

        output = st.selectbox("Output Language", ('afrikaans', 'albanian',
                                                  'amharic', 'arabic',
                                                  'armenian',
                                                  'azerbaijani',
       'basque', 'belarusian',
       'bengali', 'bengali', 'bulgarian',
        'catalan', 'cebuano',
        'chichewa', 'chinese (simplified)',
       'chichewa', 'chinese (traditional)',
       'croatian',
       'czech', 'danish', 'dutch',
        'english', 'esperanto',
       'estonian', 'filipino', 'finnish',
     'french', 'frisian', 'galician',
        'georgian', 'german',
        'greek', 'gujarati',
       'haitian creole',  'hausa',
       'hawaiian', 'hebrew', 'hindi',
        'hmong', 'hungarian',
     'icelandic', 'igbo', 'indonesian',
        'irish', 'italian',
     'japanese', 'javanese',
       'kannada', 'kazakh',  'khmer',
        'korean',  'kurdish (kurmanji)',
        'kyrgyz',  'lao',
       'latin',  'latvian', 'lithuanian',
        'luxembourgish',
       'macedonian', 'malagasy', 'malay',
        'malayalam',  'malayalam',
        'maori',  'marathi', 'mongolian',
       'myanmar (burmese)',
       'nepali',  'norwegian', 'odia',
       'pashto',  'persian',
       'polish', 'portuguese', 'punjabi',
     'romanian', 'russian',
        'samoan', 'scots gaelic',
       'serbian', 'serbian',
       'shona', 'sindhi', 'sinhala',
       'slovak', 'slovenian',
       'somali', 'spanish', 'sundanese',
     'swahili', 'swedish',
     'tajik', 'tamil', 'telugu',
        'thai',  'turkish',
     'ukrainian',  'urdu', 'uyghur',
        'uzbek',
       'vietnamese', 'welsh', 'xhosa',
       'yiddish',  'yoruba',
        'zulu'))
        st.write("You selected output language:", output)




    form = st.form(key="my_form")
    submit_button = form.form_submit_button(label='Submit')
    if submit_button:
        if option == 'Microphone':

            #Function call

            query = main(output)



            st.subheader("Thank you for using our application")
            st.write("If you wanna reuse in different languages, "
                     "pls select your desired language "
                     "and click submit button again. ")



        elif option == 'URL':

            st.write("your video URL:", url)
            st.video(url)



            #function call

            final_tra = main1(url)



            st.subheader("Thank you for using our application")
            st.write("If you wanna reuse in different languages, "
                     "pls select your desired language "
                     "and click submit button again ")




#main function

if __name__ == '__main__':

    def intro():

        #Home page

        st.title("HOME")
        st.write("Speech to text is a speech recognition software that enables"
                 " the recognition and translation of spoken language into text "
                 "through computational linguistics. It is also known as speech "
                 "recognition or computer speech recognition.Speech-to-text enables"
                 " the real-time transcription of audio streams into text."
                 " Speech-to-text service can be tailored to your voice or "
                 "vocabulary to build custom recognition models, further enhancing "
                 "accuracy.")
        st.write(" ")
        st.header("Types of Transcription models")
        st.write("In speech-to-text transcription, we have two types of models.")
        st.write("1. Streaming transcription")
        st.write("2. batch streaming.")
        st.subheader("Streaming Transcription")
        st.write("This is a type of transcription that deals with real-time audio "
                 "or video files. In streaming transcription, it breaks the "
                 "input audio into chunks. The model then outputs the transcribed "
                 "text in real-time as the audio is processed. It is effective when"
                 " you have live events and you want the transcribed text in real-time.")
        st.write("Streaming transcription can be applied in the following areas:")
        st.write("A. Livepodcasts, webinars, and videos.")
        st.write("B. Live online events and teleconferencing.")
        st.write("C. Real-time phone calls.")
        st.subheader("Batch Streaming")
        st.write("This is a type of transcription that deals with offline audio "
                 "and video files. It is best suitable when we have large recorded "
                 "video and audio files. The model only produces the transcribed text "
                 "when it has finished the processing.")
        st.write("Speech to text is software that works by listening to audio "
                 "and delivering an editable, verbatim transcript on a given device."
                 " The software does this through voice recognition."
                 " A computer program draws on linguistic algorithms to "
                 "sort auditory signals from spoken words and transfer those"
                 " signals into text using characters called Unicode. Converting "
                 "speech to text works through a complex machine learning model "
                 "that involves several steps. Let's take a closer look at how "
                 "this works:")
        st.write("1. When sounds come out of someone's mouth to create words, "
                 "it also makes a series of vibrations. Speech to text technology "
                 "works by picking up on these vibrations and translating them into"
                 " a digital language through an analog to digital converter.")
        st.write("2. The analog-to-digital-converter takes sounds from an audio file,"
                 " measures the waves in great detail, and filters them to distinguish "
                 "the relevant sounds.")
        st.write("3. The sounds are then segmented into hundredths or thousandths of "
                 "seconds and are then matched to phonemes. A phoneme is a unit of "
                 "sound that distinguishes one word from another in any given language."
                 " For example, there are approximately 40 phonemes in the English "
                 "language.")
        st.write("4. The phonemes are then run through a network via a mathematical "
                 "model that compares them to well-known sentences, words, and phrases.")
        st.write("5. The text is then presented as text or a computer-based demand "
                 "based on the audio?s most likely version.")

        st.header("Why should you use speech to text?")
        st.write("Like all forms of technology, speech to text has many benefits "
                 "that help us improve daily processes. These are some of the main"
                 " advantages of using speech to text:")
        st.write("1. Save time: Automatic speech recognition technology saves time "
                 "by delivering accurate transcripts in real-time.")
        st.write("2. Cost-efficient: Most speech to text software has a subscription"
                 " fee, and a few services are free. However, the cost of the "
                 "subscription is far more cost-efficient than hiring human "
                 "transcription services.")
        st.write("3. Enhance audio and video content: Speech to text capabilities "
                 "mean that audio and video data can be converted in real-time for "
                 "subtitling and fast video transcription.")
        st.write("4. Streamline the customer experience: By drawing on natural "
                 "language processing, the customer experience is transformed "
                 "through ease, accessibility, and seamlessness.")
        st.header("What are the types of speech to text technology?")
        st.write("There are two main types of speech to text technology:")
        st.write("1. Speaker-dependent: Mainly used for dictation software.")
        st.write("2. Speaker-dependent: Mainly used for dictation software.")
        st.write("These two speech recognition systems rely on software and "
                 "services to function adequately, with the main type being"
                 " built-in dictation technology. Many devices now have"
                 " built-in dictation tools, such as laptops, smartphones, and tablets")
    def user():

        #user manual page

        st.title("USER GUIDE")
        st.header("INTRODUCTION")
        st.write("This is an speech-to-text application build-on streamlit webapp")
        st.write("Streamlit is an open source app framework in Python language."
                 " It helps us create web apps for data science and machine learning "
                 "in a short time. It is compatible with major Python libraries such "
                 "as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, "
                 "Matplotlib etc.")
        st.write("With Streamlit, no callbacks are needed since widgets are treated"
                 " as variables. Data caching simplifies and speeds up computation "
                 "pipelines. Streamlit watches for changes on updates of the linked "
                 "Git repository and the application will be deployed automatically "
                 "in the shared link.")
        st.header("Applications of speech-to-text-converter!")
        st.write("1. Vlog bloggers can convert the video to text after recording "
                 "the speech video and add subtitles quickly.")
        st.write( "2. Teachers can convert the course into text and "
                 "add it to the video after recording.")
        st.write("3. Podcasters can "
                 "convert the audio into text for listeners after recording.")
        st.header("Fields where Speech-to-text-converter is used!")
        st.write("A speech to text model is applied in various areas such as:")
        st.write("1. Subtitle generation in audio and video files.")
        st.write("2. Medical sector to convert spoken words to text.")
        st.write("3. Online voice services. ")
        st.write("4. It is applied in businesses that use online customer support.")
        st.header("How to use this application and how it works?")
        st.write("The embedded Speech-to-Text (STT) tool allows students testing "
                 "with the appropriate accommodations to dictate responses to "
                 "constructed-response items. To use STT, select the microphone icon "
                 "or URL option in or near the item response area and begin speaking."
                 " The dictated response will be transcribed as text in the item "
                 "response area.")
        st.write("As the student speaks, the words are transcribed into the text "
                 "response area. There may be a slightdelay while the text is being "
                 "transcribed and dots appear in the text response area to indicate "
                 "that thetranscription is in process.")
        st.write("Students can dictate for five minutes at a time. Depending on the"
                 " tool settings, the entered text may beauto-punctuated. The student "
                 "can also control the punctuation and grammar of the text through "
                 "speechcommands to some extent. For example, the student can say, "
                 "?New Paragraph? to create a newparagraph."
                 " It is ultimately the student?s responsibility to ensure the accuracy"
                 " of the transcription as wellas grammar and punctuation."
                 "The buttons in the formatting toolbar are disabled while dictation "
                 "is on. The buttons are enabled onceyou stop the recording. "
                 "You also cannot navigate away from the test page while dictation "
                 "is on")
        st.write("This can take speech input from 2 ways:")
        st.write("1. URL")
        st.write("2. Microphone")
        st.write("In URL you can provide the video's URL and this application "
                 "converts each and every word of the video into text which is "
                 "a form of subtitle or transcript of the video")
        st.write("Through Microphone option you can provide the speech input "
                 "through microscope i.e., it uses audio given by user as input, "
                 "and recognizes the audio and convert it into text.")
        st.write("This application gives you best accuracy rate.")
        st.write("After giving the input through URL or Microphone you will "
                 "click the Submit button to get the output i.e.,text transcript "
                 "of the speech input.")
        st.write("There are more than 50 langauges where you can tranlate your "
                 "input to different languages of 50+.")

    page_names_to_funcs  ={
        "HOME":intro,

        "USER MANUAL":user,

        "SPEECH-TO-TEXT-APPLICATION":application
    }

    #sibebar of selctbox to choose between pages.

    demo_name = st.sidebar.selectbox("Pages",page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()







