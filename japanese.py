import tkinter as tk


dictionary = {
    "house": "ie",
    "car": "kuruma",
    "road": "michi",
    "book": "hon",
    "clock": "tokei",
    "phone": "denwa",
    "school": "gakko",
    "teacher": "sensei",
    "friend": "tomodachi",
    "love": "ai",
    "hello": "konnichiwa",
    "goodbye": "sayonara",
    "thank you": "arigato",
    "good morning": "ohayo",
    "excuse me": "sumimasen",
    "flower": "hana",
    "mountain": "yama",
    "sea": "umi",
    "sky": "sora",
    "moon": "tsuki",
    "rain": "ame",
    "snow": "yuki",
    "wind": "kaze",
    "forest": "mori",
    "water": "mizu",
    "tea": "ocha",
    "meat": "niku",
    "rice": "gohan",
    "fish": "sakana",
    "alcoholic drink": "sake",
    "fruit": "kudamono",
}

def translate_word():
    word = entry_word.get().strip().lower()
    reverse_dictionary = {v: k for k, v in dictionary.items()}  

    
    if word in dictionary:
        translation = dictionary[word]  
    elif word in reverse_dictionary:
        translation = reverse_dictionary[word]  
    else:
        translation = "Word not found in the dictionary."

    label_result.config(text=f"Translation: {translation}")


root = tk.Tk()
root.title("japanese Dictionary")
root.geometry("400x300")

label_title = tk.Label(root, text="japanese Dictionary", font=("Arial", 17, "bold"))
label_title.pack(pady=10)

frame_word = tk.Frame(root)
frame_word.pack(pady=10)

label_word = tk.Label(frame_word, text="Enter Word:")
label_word.pack(side=tk.LEFT, padx=5)

entry_word = tk.Entry(frame_word, width=20)
entry_word.pack(side=tk.LEFT, padx=5)

button_translate = tk.Button(root, text="Translate", command=translate_word)
button_translate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()