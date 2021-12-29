from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
#pyttsx3 lib
import pyttsx3 as pp
# for speach recognation
import speech_recognition as s
#thread
import threading


engine=pp.init()

voices=engine.getProperty('voices')
print(voices)



engine.setProperty('voice',voices[0].id)#0 mins male voice

def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("My Bot")
conversation = [
    'Hello',
    'Hi there!',
    'what is your name ?',
    'My name is bot,I am created by sourabh',
    "How are you doing?",
    'Im doing great',
    'That is good to hear',
    "Thank you.",
    'You are welcome'
]

trainer = ListTrainer(bot)
trainer.train(conversation)

#response = bot.get_response("Good morning!")
#print(response)
####
#print("Talk to bot ")
#while True:
#    query=input()
#    if query=='exit':
#        break
#    answer=bot.get_response(query)
#    print("bot :",answer)

##########


main=Tk()

main.geometry("400x500")

main.title("My chat bot ")
img=PhotoImage(file="download.png")

photoL=Label(main,image=img)

photoL.pack(pady=5)

#take query :it takkes audio as input from user and converts it to string
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold= 1
    print("your bot is listning try to speak")


    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.delete(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")






#asking to bot--------------------------
def ask_from_bot():
    query=textF.get()
    answer_from_bot =bot.get_response(query)
    msgs.insert(END,"you :"+ query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot :" + str(answer_from_bot))

    speak(answer_from_bot)

    textF.delete(0,END)
    msgs.yview(END)




frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=60,height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

#creating text field
textF=Entry(main,font=("verdana",20))
textF.pack(fill=X,pady=10)

#create butten
btn=Button(main,text="ask from bot",font=("verdana",20),command=ask_from_bot)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()  #invoke the butten

#Going to bind main window with enter key

main.bind('<Return>',enter_function) #rwturn mins enter

#-----------------
def repearL():
    while True:
        takeQuery()

#-----------------

t=threading.Thread(target=repearL)

main.mainloop()