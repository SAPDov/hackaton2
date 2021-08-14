import tkinter as tk
from tkinter.messagebox import *
import tkinter.font
import pandas as pd 
import random


data = pd.read_csv('./truth_dare.csv', header=None)

# print(df_truth)
pd.set_option('display.max_colwidth', None) #Show full rows in a long string
df_truth = data.loc[data.iloc[:,0] == 'T']
df_dare = data.loc[data.iloc[:,0] == 'D']

df_truth = df_truth.drop(columns = 0)
df_dare = df_dare.drop(columns = 0)

# print(df_truth)

def dare():
	text = df_dare.sample()
	print(text)
	return text

def truth():
	text = df_truth.sample()
	return text

def open_new_window(window, button_id):
	new_window = tk.Toplevel(window)
	new_window.geometry("600x100")
	td_font = tkinter.font.Font(family = "Comic Sans MS", size = 12, weight = "bold") 

	if button_id == 0:
		text = truth()
	elif button_id == 1:
		text = dare()
	display = tk.Label(new_window, text=text, font=td_font, padx=20)
	display.grid(column=0, row=0)
	
def truthDareMainFrame():
	window = tk.Tk()
	window.title("Truth or Dare")
	window.geometry('250x200')
	window.configure(background ='pink')
	# Font style
	td_font = tkinter.font.Font(family = "Comic Sans MS", size = 35, weight = "bold")
	b_font = tkinter.font.Font(family = "Comic Sans MS", size = 10, weight = "bold")  


	label = tk.Label(window, text = "Truth or Dare", bg = 'pink', font = td_font)
	label.grid(column=1, row =0, padx=50)
	label_gap = tk.Label(window, text ='?',bg = 'pink',font = b_font).grid(column=1, row =1)
	
	# setting button_id
	button_truth = tk.Button(window, text = 'Truth', width= 10, command = lambda: open_new_window(window, 0))
	button_truth.grid(column=1, row =2, padx=20)
	button_dare = tk.Button(window, text = 'Dare', width= 10, command = lambda: open_new_window(window, 1))
	button_dare.grid(column=1, row =3, padx=20)

	# setting buttons fonts
	button_truth['font'] = b_font
	button_dare['font'] = b_font

	window.mainloop()


# truthDareMainFrame() 	

# dare()



