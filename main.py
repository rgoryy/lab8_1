import tkinter as tk
import random
from PIL import Image, ImageTk


def flip_coin(p):
    result = random.random()
    coin_image_label.config(image="")

    if result < p:
        coin_image_label.config(image=heads_image)
    else:
        coin_image_label.config(image=tails_image)


def update_probability():
    try:
        probability = float(probability_entry.get())
        if 0 <= probability <= 1:
            probability_label.config(text=f"Вероятность выпадения решки: {probability * 100:.2f}%")
        else:
            probability_label.config(text="Вероятность должна быть в диапазоне от 0 до 1.")
    except ValueError:
        probability_label.config(text="Введите корректное значение вероятности.")


root = tk.Tk()
root.title("Бросок монеты")

heads_image = ImageTk.PhotoImage(Image.open("tail.png"))
tails_image = ImageTk.PhotoImage(Image.open("head.png"))

coin_image_label = tk.Label(root, image=ImageTk.PhotoImage(Image.open("tail.png")))
coin_image_label.pack()

probability_entry = tk.Entry(root)
probability_entry.insert(0, '0.5')
probability_entry.pack()

probability_label = tk.Label(root, text="Введите вероятность выпадения решки (от 0 до 1):")
probability_label.pack()

update_button = tk.Button(root, text="Обновить вероятность", command=update_probability)
update_button.pack()

flip_button = tk.Button(root, text="Бросить монету", command=lambda: flip_coin(float(probability_entry.get())))
flip_button.pack()

root.mainloop()