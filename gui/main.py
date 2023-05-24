import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os
import keras
import numpy as np
from skimage import transform
import tensorflow as tf


img = None
filename = None
def get_file_name():
    global filename
    filename = fd.askopenfilename(filetypes=[('Image', '*.jpg')],initialdir="C:\\Users\\fijal\Documents\Repository\BIAI")
    return filename


def open_image():
    path = get_file_name()
    global img
    img = Image.open(path)
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img
    classify_button.pack()


def classify():
    path_to_model = fd.askdirectory(parent=root,initialdir="C:\\Users\\fijal\Documents\Repository\BIAI",title='Please select a directory to model')
    loadedModel = keras.models.load_model(path_to_model)
    global img
    original_image = Image.open(filename)
    your_image = np.array(original_image).astype("float32") / 255
    your_image = transform.resize(your_image, (256, 256, 3))
    your_image = np.expand_dims(your_image, axis=0)
    prediction = loadedModel.predict(your_image)
    print(prediction)
    index = prediction.tolist()[0].index(max(prediction.tolist()[0]))
    images_path = "C:\\Users\\fijal\Documents\Repository\BIAI\current_data_set_equal"
    class_names = os.listdir(images_path)
    print(class_names)
    result = class_names[index]
    print(result)
    print(filename)
    ai_result.config(text=result)
    ai_result.text = result
    ai_result.pack()
    loadedModel = None


root = tk.Tk()
root.geometry("500x500")
root.title("Car classification AI")
root.resizable(width=False, height=False)

label = tk.Label(root, text="Please choose image to classify", font=('Arial', 18))
label.pack()

load_button = tk.Button(root, text="Load image", font=('Arial', 14), command=open_image)
load_button.pack()

panel = tk.Label(root)
panel.pack()

ai_result = tk.Label(root, text="Your result",font=('Arial', 32))

classify_button = tk.Button(root, text="Classify", font=('Arial', 14), command=classify)



root.mainloop()
