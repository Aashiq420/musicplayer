from tkinter import *
from pydub import AudioSegment
import pygame 

#convert mp3 to wav:
'''
filename = 'Post Malone - Enemies'
tempfile = filename+".mp3"
song = AudioSegment.from_mp3(tempfile)
newname = filename+".wav"
song.export(newname, format="wav")'''

#tkinter basics
root = Tk()
root.geometry('700x250')
root.title('Music Player')
root.configure(bg='red')

#Initializing pygame mixer
pygame.mixer.init()



#list of songs
song_names = ['Bas - Methylone','Bas - Night Job','Immortal Technique - Creation and Distruction',
                'Immortal Technique - Dominant Species','J.I.D - D_Vision','J.I.D - Lauder',
                'Joyner Lucas - Devils Work','Joyner Lucas - FYM','Joyner Lucas - Ultrasound',
                'Kendrick Lamar - Collard Greens','Logic - Confessions of a Dangerous Mind',
                'Post Malone - Circles','Post Malone - Enemies']

#Class to run program
class music:
    #init function will run main tkinter program
    def __init__(self):
        #labels
        label_1 = Label(root, text='Song Track:', bg='red', fg='white')
        label_2 = Label(root, text='Control Panel:', bg='red', fg='white')
        label_3 = Label(root, text='Song Playlist:', bg='red', fg='white')
        self.display_label = Label(root, text=">none selected<", borderwidth=5, relief="groove", padx=5, pady=5, bg='black', fg='green')

        #buttons
        play_btn = Button(root, text = 'PLAY', command=self.play, bg='darkgreen', fg='white')
        pause_btn = Button(root, text='PAUSE', command=self.pause, bg='darkgreen', fg='white')
        unpause_btn = Button(root, text='UNPAUSE', command=self.unpause, bg='darkgreen', fg='white')
        stop_btn = Button(root, text='STOPSONG', command=self.stop, bg='darkgreen', fg='white')

        #listbox + scrollbar
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill = Y )
        self.song_display = Listbox(root, yscrollcommand = scrollbar.set, width=35, bg='black',fg='green',selectbackground='red',selectforeground='white')

        #for loop to display song names in listbox
        for i in song_names:
            self.song_display.insert(END, str(i))

        #placing list box
        self.song_display.pack( side = RIGHT, fill = BOTH,pady=25)

        #Configuring scrollbar to work for the list box
        scrollbar.config( command = self.song_display.yview )


        #Label placements
        label_1.place(x=5,y=5)
        label_2.place(x=5,y=85)
        label_3.place(x=400,y=5)
        self.display_label.place(x=5,y=30)

        #Button placements
        play_btn.place(x=5,y=110)
        pause_btn.place(x=75,y=110)
        unpause_btn.place(x=155,y=110)
        stop_btn.place(x=255,y=110)

        #horizontal slide of words
        self.canvas=Canvas(root,bg='black')
        self.canvas.place(x=5,y=160)
        self.text_var="Hey there! Select a song from the playlist alongside and press 'PLAY' →"
        self.text=self.canvas.create_text(0,-75,text=self.text_var,font=('Times New Roman',20,'bold'),fill='green',tags=("marquee",),anchor='w')
        width = 390
        height = 40
        self.canvas['width']=width
        self.canvas['height']=height
        self.fps=60
        self.shift()

    #Functions for button commands
    #play button function
    def play(self):
        self.fps=35
        filename = self.song_display.get(ACTIVE)+'.wav'
        self.canvas.itemconfigure(self.text, text="Playing - "+self.song_display.get(ACTIVE))
        self.display_label['text'] = self.song_display.get(ACTIVE)+"   --Playing"
        pygame.mixer.music.load("/home/user/Documents/Python/Music/"+filename)
        pygame.mixer.music.play()
        

    #pause button function
    def pause(self):
        self.fps=35
        pygame.mixer.music.pause()
        self.canvas.itemconfigure(self.text, text="Paused - "+self.song_display.get(ACTIVE))
        self.display_label['text'] = self.song_display.get(ACTIVE)+"   --Paused"
    
    #unpause button function
    def unpause(self):
        self.fps=35
        pygame.mixer.music.unpause()
        self.canvas.itemconfigure(self.text, text="Playing - "+self.song_display.get(ACTIVE))
        self.display_label['text'] = self.song_display.get(ACTIVE)+"   --Playing"

    #stop button function
    def stop(self):
        self.fps=60
        pygame.mixer.music.stop()
        self.canvas.itemconfigure(self.text, text=self.text_var)
        self.display_label['text'] = "Song Stopped"
    
    #function for sliding words 
    def shift(self):
        x1,y1,x2,y2 = self.canvas.bbox("marquee")
        if(x2<0 or y1<0):
            x1 = self.canvas.winfo_width()
            y1 = self.canvas.winfo_height()//2
            self.canvas.coords("marquee",x1,y1)
        else:
            self.canvas.move("marquee", -2, 0)
        self.canvas.after(1000//self.fps,self.shift)

#Run program
run = music()
root.mainloop()
