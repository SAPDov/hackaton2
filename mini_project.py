import tkinter as tk
import tkinter.font
import random
import truth_dare
import coctail
import music


main_window = tk.Tk()
# Font Style
main_font = tkinter.font.Font(family = "Comic Sans MS", size = 40, weight = "bold")
bu_font = tkinter.font.Font(family = "Comic Sans MS", size = 15, weight = "bold")


def open_truth_or_dare():
	truth_dare.truthDareMainFrame()

def open_cocktails():
	coctail.coctailsMainFrame()

def open_music():
	music.musicMainFrame()

def mainFrame():
	main_window.title("Game Night")
	main_window.geometry('400x400')	
	main_window.configure(background ='pink')
	main_label = tk.Label(main_window, text = "Game Night", bg = 'pink', font = main_font)
	gap_label = tk.Label(main_window, text = "What Do You Wanna...\n do Tonight?", bg = 'pink', font = bu_font)

	main_label.pack()
	gap_label.pack()

	button_truth = tk.Button(main_window, text = 'Truth or Dare', width= 25, font = bu_font, command = lambda: open_truth_or_dare())
	button_truth.pack()

	button_truth = tk.Button(main_window, text = 'Pick your poison', width= 25, font = bu_font, command = lambda: open_cocktails())
	button_truth.pack()

	button_truth = tk.Button(main_window, text = 'Play a song', width= 25, font = bu_font, command = lambda: open_music())
	button_truth.pack()

	main_window.mainloop()



mainFrame() 	

  
