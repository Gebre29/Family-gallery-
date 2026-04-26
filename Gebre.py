import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("ናይ ስድራቤት መዝገብ")
root.geometry("800x600")
root.configure(bg="#FAFAF6")

folder_path = "images"
photos = [f"{folder_path}/{img}" for img in os.listdir(folder_path) 
          if img.lower().endswith(('.jpg', '.jpeg', '.png', '.heic'))]
photos.sort()

current_index = 0

def check_password():
    if password_entry.get() == "1234":
        login_frame.pack_forget() 
        main_frame.pack(fill="both", expand=True) 
        update_display()
    else:
        messagebox.showerror("ጌጋ", "ዝተጋገየ ሚስጥር ቃል!")

def show_next():
    global current_index
    if photos:
        current_index = (current_index + 1) % len(photos)
        update_display()

def show_prev():
    global current_index
    if photos:
        current_index = (current_index - 1) % len(photos)
        update_display()

def update_display():
    if photos:
        img_path = photos[current_index]
        img = Image.open(img_path)
        
        # ፎቶው እንዳይለጠጥ መጠኑን የማመጣጠን ስራ (Aspect Ratio)
        max_size = (900,480) # ከፍተኛው ስፋት እና ቁመት
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        photo = ImageTk.PhotoImage(img)
        img_label.config(image=photo)
        img_label.image = photo
        counter_label.config(text=f"ስእሊ {current_index + 1} ካብ {len(photos)}")

# --- UI ---
login_frame = tk.Frame(root, bg="#f4f4f4")
login_frame.pack(pady=150)

tk.Label(login_frame, text="ሚስጥር ቃል የእትዉ", font=("Nyala", 15)).pack()
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 15))
password_entry.pack(pady=10)
tk.Button(login_frame, text="እቶ", command=check_password, width=10).pack()

main_frame = tk.Frame(root, bg="#dadfde")
tk.Label(main_frame, text="ናይ ስድራቤት ጋለሪ", font=("Nyala", 20, "bold"), bg="#FEFDE4").pack(pady=20)

img_label = tk.Label(main_frame, bg="#f5dddd")
img_label.pack(pady=10, expand=True) # ፎቶው መሃል ላይ እንዲሆን

counter_label = tk.Label(main_frame, text="", font=("Nyala", 15), bg="#f4f4f4")
counter_label.pack()

btn_frame = tk.Frame(main_frame, bg="#f9c8a0")
btn_frame.pack(pady=40)

# command= በትክክል መኖሩን አረጋግጥ
tk.Button(btn_frame, text="⬅️ ንድሕሪት", command=show_prev, font=("Nyala", 12), width=15).grid(row=0, column=0, padx=25)
tk.Button(btn_frame, text="ንቅድሚት ➡️", command=show_next, font=("Nyala", 12, "bold"), bg="#727DFB", fg="white", width=15).grid(row=0, column=1, padx=25)

root.mainloop()