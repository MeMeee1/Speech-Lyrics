import sys
import pyttsx3
import os
class Log():
    def __init__(self):
        file_name=input("Enter the name of your new file:\n**************NOTE:IT MUST BE A .TXT FILE**************\n");
        self.file_name=file_name

    def write(self):
        with open(self.file_name,'w',) as myFile:
            print("\n ******----Only 20 words are allowed per line!---*****\n")
            print("[First Stanza]\n")
            
            first_stanza_line=input("Please enter the first line of the first stanza:")
            self.first_stanza_line=first_stanza_line
            myFile.write('\n[First Stanza]\n'+ first_stanza_line +'\n')
            

            first_stanza_sec_line=input("Please enter the second line of the first stanza:")
            self.first_stanza_sec_line=first_stanza_sec_line
            myFile.write(first_stanza_sec_line +'\n')
            
            
            first_stanza_third_line=input("Please enter the third line of the first stanza:")
            self.first_stanza_third_line=first_stanza_third_line
            myFile.write(first_stanza_third_line +'\n')

            
            first_stanza_fourth_line=input("Please enter the fourth line of the first stanza:")
            self.first_stanza_fourth_line=first_stanza_fourth_line
            myFile.write(first_stanza_fourth_line+'\n')
                    
            print("\n[Second Stanza]\n")
            
            sec_stanza_line=input("Please enter the first line of the second stanza:")
            self.sec_stanza_line=sec_stanza_line
            myFile.write('\n[Second Stanza]\n'+ sec_stanza_line +'\n')
            

            sec_stanza_sec_line=input("Please enter the second line of the second stanza:")
            self.sec_stanza_sec_line=sec_stanza_sec_line
            myFile.write(sec_stanza_sec_line +'\n')
            
            
            sec_stanza_third_line=input("Please enter the third line of the second stanza:")
            self.sec_stanza_third_line=sec_stanza_third_line
            myFile.write(sec_stanza_third_line +'\n')

            
            sec_stanza_fourth_line=input("Please enter the fourth line of the second stanza:")
            self.sec_stanza_fourth_line=sec_stanza_fourth_line
            myFile.write(sec_stanza_fourth_line+'\n')

            print("\n[Chorus]\n")
            
            chorus_stanza_line=input("Please enter the first line of the chorus:")
            self.chorus_stanza_line=chorus_stanza_line
            myFile.write('\n[Chorus]\n'+ chorus_stanza_line +'\n')
            

            chorus_stanza_sec_line=input("Please enter the second line of the chorus:")
            self.chorus_stanza_sec_line=chorus_stanza_sec_line
            myFile.write(chorus_stanza_sec_line +'\n')
            
            
            chorus_stanza_third_line=input("Please enter the third line of the chorus:")
            self.chorus_stanza_third_line=chorus_stanza_third_line
            myFile.write(chorus_stanza_third_line +'\n')

            
            chorus_stanza_fourth_line=input("Please enter the fourth line of the chorus:")
            self.chorus_stanza_fourth_line=chorus_stanza_fourth_line
            myFile.write(chorus_stanza_fourth_line+'\n')

            write_chorus=str('\n[Chorus]\n'+ chorus_stanza_line +'\n'+chorus_stanza_sec_line +'\n'+ chorus_stanza_third_line +'\n'+chorus_stanza_fourth_line)
            self.write_chorus=write_chorus
            while True:
                
                try:
                    count=int(input("\nHow many times would you like the chorus to be repeated:"))
                    counted = int(count)
                    counted = counted - 1
                    for i in range(counted):
                        myFile.write(write_chorus+'\n')
                    break
                except:
                    print("\nProgram having issues running your code.\nYour input must be an integer.\nTry again!")
                
            
        print('These are the lyric for '+ self.file_name + ' file:')
        with open(self.file_name,'r') as readFile:
            r = readFile.read()
            print(r)

l = Log()
f = l.write()

while True:
    text_to_speech=input("Would you like to listen to your song?\n 1. Yes\n 2. No\n")
   
    try:
        if text_to_speech == '1':
            engine = pyttsx3.init()
            
            
            # convert this text to speech
            text=input("Enter the name of the file you want to listen to\n **************NOTE:IT MUST BE A .TXT FILE**************\n")
            b =open(text)
            i = b.read()
            # setting new voice rate (faster)
            engine.setProperty("rate", 250)
            engine.say(i)
            
            # play the speech
            engine.runAndWait()
            print("Thank you for using this program.")
            break

        elif text_to_speech == '2':
            print("Thank you for using this program.")
            break
            

        else:
            print("\nInvalid input! Either input these values when asked 1  or 2 \n")
    except:
        print("Invalid Input! Enter either of these values 1  or 2 \n")
