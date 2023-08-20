from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk , Image 
# ====================
root = tk.Tk()
root.title("DataSet_HeartDisease")
root.geometry("870x579")
img = Image.open("C:\\Users\\rewan ahmed\\project (1)\\final_project\\photo.jpg")
photo = ImageTk.PhotoImage(img)
img_label = Label(root,image=photo)
img_label.place(x=0 , y=0 , relwidth=1 , relheight= 1)
#title
title = Label(root, text="Data Set  - Astro team", font="calibre 20 bold" , )
title.grid(row=0, column=0, pady=70,padx=300, columnspan=4 )
# ===============================
# Age
age_label= Label(root, text="Age" , font = " 10")
age_label.grid(row=1, column=0, padx=10, sticky="e")
age_entry= Entry(root )
age_entry.grid(row=1, column= 1 , sticky="w" )
# =============================
#trestbps
trestbps_Label= Label(root, text="trestbps" , font = " 10")
trestbps_Label.grid(row=4, column=0, padx=10 , sticky="e")
trestbps__entry= Entry(root)
trestbps__entry.grid(row=4, column=1 ,sticky="w")
# ======================
#Cholesterol
Cholesterol_Label= Label(root, text="Cholesterol" , font = " 10")
Cholesterol_Label.grid(row=6, column=0, padx=10 , sticky="e")
Cholesterol__entry= Entry(root)
Cholesterol__entry.grid(row=6, column=1 , sticky="w")
# =======================
#Thalach
Thalach_Label= Label(root, text="Thalach" ,font = " 10")
Thalach_Label.grid(row=8, column=0, padx=10 ,sticky="e")
Thalach__entry= Entry(root)
Thalach__entry.grid(row=8, column=1 , sticky="w")
# ================
#Oldpeak
ol_Label= Label(root, text="Oldpeak" ,font = " 10")
ol_Label.grid(row=10, column=0, padx=10 ,sticky="e")
ol__entry= Entry(root)
ol__entry.grid(row=10, column=1 ,sticky="w")
# ===============================
# chest pain type 
C_label= Label(root, text="chest pain type" ,font = " 10")
C_label.grid(row=12, column=0, padx=10, sticky="e")
C_choices= ttk.Combobox(root, values=["0 = typical angina"," 1 = atypical angina"," 2 = non-anginal pain"," 3 = asymptomatic"])
C_choices.grid(row=12, column=1, pady=5,  sticky="w")
# ==========================
#restecg
rr_label= Label(root, text="restecg" ,font = " 10")
rr_label.grid(row=14, column=0, padx=10, sticky="e")
rr_choices= ttk.Combobox(root, values=[0,1,2])
rr_choices.grid(row=14, column=1, pady=5, sticky="w")
# ====================
# sex of the patient
G_label= Label(root, text="sex of the patient" ,font = " 10")
G_label.grid(row=1, column=2, sticky="w")
G_choices= ttk.Combobox(root, width=20, values=[0,1])
G_choices.grid(row=1, column=3, pady=5,  sticky="w")
# ===============================
#Fasting blood sugar
fast_label= Label(root, text="Fasting blood sugar" , font = " 10")
fast_label.grid(row=4, column=2,  sticky="w")
fast_choices= ttk.Combobox(root, width=20, values=[0,1])
fast_choices.grid(row=4, column=3, pady=5,  sticky="w")
# ===============================
#Exang
ex_label= Label(root, text="Exang" ,font = " 10")
ex_label.grid(row=6, column=2, sticky="w")
ex_choices= ttk.Combobox(root, width=20, values=[0,1])
ex_choices.grid(row=6, column=3, pady=5,  sticky="w")
# =======================
#slope
slope_label= Label(root, text="slope" ,font = " 10")
slope_label.grid(row=8, column=2, sticky="w" )
slope_choices= ttk.Combobox(root, width=20, values=[0,1,2])
slope_choices.grid(row=8, column=3, pady=5, sticky="w" )
# =========================
#number of major vessels
co_label= Label(root, text="(co)number of\nmajor vessels" ,font = " 10")
co_label.grid(row=10, column=2, sticky="w" )
co_choices= ttk.Combobox(root, width=20, values=[0,1,2,3])
co_choices.grid(row=10, column=3, pady=5, sticky="w"  )
# =======================
# thalassemia
th_label= Label(root, text=" thalassemia" ,font = " 10")
th_label.grid(row=12, column=2, sticky="w")
th_choices= ttk.Combobox(root, width=20, values=[0,1,2,3])
th_choices.grid(row=12, column=3, pady=5,sticky="w")
# ===========================
#Target
target_label= Label(root, text=" target" ,font = " 10")
target_label.grid(row=14, column=2, sticky="w")
target_choices= ttk.Combobox(root, width=20, values=[0,1])
target_choices.grid(row=14, column=3, pady=5,  sticky="w")
#Buttons
def Save_Data():
    Age_entry1=age_entry.get()
    Gender= G_choices.get()
    chestpaintype=C_choices.get()
    trestbpsentry=trestbps__entry.get()
    Cholesterol=Cholesterol__entry.get()
    Fast=fast_choices.get()
    Restecg=rr_choices.get()
    Thalach=Thalach__entry.get()
    exang=ex_choices.get()
    oldpeak=ol__entry.get()
    Slope=slope_choices.get()
    major=co_choices.get()
    th=th_choices.get()
    targGET=target_choices.get()
    text=  Age_entry1+","+Gender +"," + chestpaintype +"," + trestbpsentry +"," + Cholesterol+","+ Fast +","+Restecg+","+Thalach+","+exang+","+oldpeak+","+Slope+","+major+","+th+","+targGET+ "\n"
    with open(r"C:\\Users\\rewan ahmed\\project (1)\\final_project\\heart_1.csv", "a")as file:
        file.write(text)
Save_button= Button(root, text="Save", command=Save_Data )
Save_button.grid(row=25, column=1,pady=10, padx=10, sticky="e", ipadx=50 )
root.mainloop()