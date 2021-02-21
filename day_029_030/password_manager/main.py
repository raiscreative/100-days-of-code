from tkinter import *
from tkinter import messagebox
import random, string, json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()_+') for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) < 16:
        password = generate()

    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }


    
    if len(website) == 0:
        messagebox.showinfo(title='Something went wrong', message='Please make sure you\'ve filled the website field.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'You entered:\nWebsite: {website}\nEmail/username: {email}\nPassword: {password}\n\nSave these data?')

        if is_ok:
            #with open("data.txt", 'a') as db:
                #print(f"{website} | {email} | {password}", file=db)
            try:
                with open("data.json", 'r', encoding='utf-8') as db:
                    data = json.load(db)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
                #with open("data.json", 'w') as db:
                    #json.dump(new_data, db, indent=4)
            else:
                data.update(new_data)

                #with open("data.json", 'w') as db:
                    #json.dump(data, db, indent=4)
            finally:
                with open("data.json", 'w', encoding='utf-8') as db:
                    json.dump(data, db, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- # 
def search_website():
    website = website_entry.get()

    try:
        with open("data.json", mode="r", encoding="utf-8") as file:
            data = json.load(fp=file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title='File not found', message='There is not a data file yet. \nAdd new data now.')
    else:

        if website in data:
            email = data[website]['email']
            password = data[website]['password']

            is_ok = messagebox.askokcancel(title=website, message=f'Email: \t{email}\nPassword: \t{password}\nUse saved data?')
            if is_ok:
                window.clipboard_clear()
                window.clipboard_append(password)
                
        else:
            messagebox.showinfo(title=website, message=f'{website} was not found.\nAdd it now.')      
    
# ---------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title('My Password Manager')
window.iconbitmap('logo.ico')
window.config(padx=50, pady=50)
#window.geometry('200x200')

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)



website_label = Label(text="Website:")
website_entry = Entry(width=35)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_entry = Entry(width=35)
email_entry.insert(0, 'eu@comp.com')

password_label = Label(text="Password:")
password_entry = Entry(width=30)
#password_button= Button(text="Generate Password", command=generate)

add_button= Button(text="Add", width=36, command=save_data)

search_button = Button(window, text="Search", command=search_website)

canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3, sticky="W")
#password_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button.grid(row=1, column=2, sticky='EW')


window.mainloop()