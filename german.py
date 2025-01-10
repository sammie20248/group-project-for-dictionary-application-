from tkinter import *

def german_dictionary_app():

    window = Tk()
    window.title("german Dictionary")
    window.geometry("350x300")

    german_dictionary  = {
    "house": "haus",
    "car": "auto",
    "road": "straße",
    "book": "buch",
    "tree": "baum",
    "sun": "sonne",
    "moon": "mond",
    "water": "wasser",
    "fire": "feuer",
    "bread": "brot",
    "milk": "milch",
    "cheese": "käse",
    "friend": "freund",
    "school": "schule",
    "teacher": "lehrer",
    "dog": "hund",
    "cat": "katze",
    "mountain": "berg",
    "river": "fluss",
    "work": "arbeit",


    }


    def autocomplete():
        typed_word = entry_text.get()


        if typed_word == "":
            suggestion_listbox.place_forget()
            feedback_label.config(text = " enter a german word", fg = "green")
            return


        suggestions = [
            word for word in german_dictionary.keys()
            if word.lower().startswith(typed_word.lower())
        ]


        suggestion_listbox.delete(0, END)
        for suggestion in suggestions:
            suggestion_listbox.insert(END, suggestion)

        if not suggestions:
            suggestion_listbox.place_forget()
            feedback_label.config(text = "No suggestions found", fg = "red")
        else:
            suggestion_listbox.place(x = entry_box.winfo_x(), y = entry_box.winfo_y() + 30)
            feedback_label.config(text = f"{len(suggestions)} suggestions found", fg = "blue")


    def on_select():
        selected_word = suggestion_listbox.get(suggestion_listbox.curselection())
        entry_text.set(selected_word)
        search(selected_word)


    def search(word):
        if word.lower() in german_dictionary:
            result.set(german_dictionary[word.lower()])
        else:
            result.set("Not Found")


    def clear():
        entry_text.set("")
        result.set("")
        suggestion_listbox.place_forget()
        feedback_label.config(text = "")


    entry_text = StringVar()
    result = StringVar()


    entry_text.trace("w", autocomplete)
    title_label = Label(window, text = "german Dictionary", font = ("Helvetica", 18, "bold"), fg = "red")
    title_label.pack(pady = 10)


    entry_box = Entry(window, textvariable = entry_text, font = ("Helvetica", 14))
    entry_box.pack(pady = 10)


    feedback_label = Label(window, text = " enter a german word", font = ("Helvetica", 10), fg = "gray")
    feedback_label.pack()

    suggestion_listbox = Listbox(window, width = 30, height = 6, selectmode = SINGLE, font = ("Helvetica", 12))
    suggestion_listbox.bind("<ButtonRelease-1>", on_select)
    suggestion_listbox.place_forget()


    result_label = Label(window, textvariable = result, font = ("helvetica", 14), fg = "blue")
    result_label.pack(pady = 10)


    button_frame = Frame(window)
    button_frame.pack(pady = 10)

    search_btn = Button(
        button_frame,
        text = "Search",
        font = ("helvetica", 12),
        command = lambda: search(entry_text.get())
    )
    search_btn.grid(row = 0, column = 0, padx = 5)

    refresh_button = Button(
        button_frame,
        text = "Refresh",
        font = ("helvetica", 12),
        command = clear
    )
    refresh_button.grid(row = 0, column = 2, padx = 5)

    window.mainloop()


german_dictionary_app()

