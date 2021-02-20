from tkinter import *

window = Tk()
window.title('My GUI program')
window.minsize(width = 500, height = 300)


label = Label(text = 'I am a label', font=('Arial', 24, 'bold'))
label.pack(side = 'bottom', expand = True)


label['text'] = 'New label'
label.config(text='Some text')


def button_clicked():
    label.config(text='You clicked the button!')


button = Button(text='Click me now!', command=button_clicked)
button.pack()








window.mainloop()