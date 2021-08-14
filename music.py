import requests
import json
import random
import tkinter as tk
import tkinter.font


def get_tracks():
	url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks"
	querystring = {"id":"40008598","locale":"en-US"}

	headers = {
	    'x-rapidapi-key': "f701eef6dcmshcd924a190cf185ep1d7335jsn1bd4a450409a",
	    'x-rapidapi-host': "shazam.p.rapidapi.com"
	    }

	response = requests.get(url, headers=headers, params=querystring).json()

	json.dumps(response, indent = 4)
	return response['tracks']


def open_new_window(window, tracks):
	new_window = tk.Toplevel(window)
	new_window.geometry("600x100")
	s_font = tkinter.font.Font(family = "Comic Sans MS", size = 15)
	# choose a random index from tracks:
	a = random.randint(0, len(tracks))
	for i, tracks in enumerate(tracks):
		if i == a:
			text = 'Title: ' + tracks['title'] + '\n'
			text += 'Link: ' + tracks['share']['href'] + '\n'
			text += 'Artist: ' + tracks['subtitle']


	display = tk.Label(new_window, text = text, font = s_font)
	display.grid(row=0, column=1)


def musicMainFrame():
	window = tk.Tk()
	window.title("Pick your music")
	window.geometry('150x150')
	window.configure(background ='pink')
	t_font = tkinter.font.Font(family = "Comic Sans MS", size = 25, weight='bold')

	label = tk.Label(window, text = "Are\n You\n Ready?", bg = 'pink', font = t_font)
	label.pack()

	tracks = get_tracks()
	button_truth = tk.Button(window, text = "Yes", width= 16, command = lambda: open_new_window(window, tracks))
	button_truth.pack()

	window.mainloop()

# musicMainFrame()
# get_tracks()