import requests
import json
import tkinter as tk
import tkinter.font



def get_drink():
	url = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
	data = requests.get(url)
	# print(data.status_code)
	data = data.json()
	return data


def coctailsMainFrame():
	c_window = tk.Tk()
	c_window.title("Pick your poison")
	c_window.geometry('400x400')
	c_window.configure(background ='pink')
	b_font = tkinter.font.Font(family = "Comic Sans MS", size = 10, weight = "bold") 
	label = tk.Label(c_window, text = "Pick your poison", bg = 'pink', font = 'bold 25')
	label.pack()

	drinks = get_drink()['drinks']
	for drink in drinks:
		name = drink['strDrink']
		# print(name)
		inst = drink['strInstructions']
		# print(inst)
		ingredients = ''
		for i in range(1, 16):
	 		ingredient = drink['strIngredient' + str(i)]
	 		if ingredient != None:
	 			ingredients += ingredient + '\n'
	 			
		# insert the open_new_window function inside promised that each button has a different value 
		def open_new_window(c_window = c_window, ingredients = ingredients, inst = inst):
			new_window = tk.Toplevel(c_window)
			new_window.geometry("1000x300")

			c_font = tkinter.font.Font(family = "Comic Sans MS", size = 6)

			text = 'Instruction:\n' + inst 
			text += '\n\n'
			text += 'Ingredients: \n' + str(ingredients)

			display = tk.Label(new_window, text = text, font= c_font)
			display.pack()
			
			
		button = tk.Button(c_window, text = name, width= 30, font = b_font, command = open_new_window)
		button.pack()
	 			
	
	c_window.mainloop()


# coctailsMainFrame()

# get_drink()