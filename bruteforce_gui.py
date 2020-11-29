#Gui python module tkinter
from tkinter import * 

#calling tkinter mode 
frame_window = Tk()
#frame title
frame_window.title("Brute Force Simulator")

# sizing 
canvas1 = Canvas(frame_window, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#inside text
label = Label(frame_window, text = "Please introduce the test password")
canvas1.create_window(200, 60, window = label)

# entry txt box (in this case secret input)
txt_input = Entry(frame_window, show = '*')
canvas1.create_window(200, 140, window = txt_input)

#method that will be activate with the button command
def test_Password ():  
    #the get method give turn text into input
    password = txt_input.get() + '\n'
    #creating an array to pass the .txt file (pool)
    pass_word = []
    with open('pass.txt') as my_file:
        for line in my_file:
            pass_word.append(line)
    #comparing the user input with the array of the pool file      
    for i in range (0, len(pass_word)-1):
        #break if found
        if pass_word[int(i)] == password:            
            break          
        #terminal display
        print(pass_word[i])
    
    #control struture to display found password in the frame  
    if pass_word[int(i)] == password:
     
        label2 = Label(frame_window, text = 'Found password:' + pass_word[int(i)])
        canvas1.create_window(200, 260, window = label2)
        label3 = Label(frame_window, text = 'Number of trys: ' + str(i))
        canvas1.create_window(200, 290, window = label3)

    #if not found adding to the list
    else: 
        pass_word.append(password)
        label2 = Label(frame_window, text = 'Save password:' + password)
        canvas1.create_window(200, 290, window = label2)

#action button 
submit = Button(frame_window, text = 'Sumbmit', width = 10 ,command = test_Password)
canvas1.create_window(200, 200, window = submit)

#endless loop for keep open frame 
frame_window.mainloop()
