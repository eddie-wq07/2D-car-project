import tkinter as tk
from PIL import Image, ImageTk

image_path_car = "assets/Car.png"
image_path_background = "assets/background.png"

root = tk.Tk()
root.title("Car Simulation")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

background_image = Image.open(image_path_background)
background_image = background_image.resize((800, 600))
background = ImageTk.PhotoImage(image=background_image)

car_image = Image.open(image_path_car)
car_image = car_image.resize((125, 127))
car = ImageTk.PhotoImage(image=car_image)

background_id = canvas.create_image(0, 0, image=background, anchor="nw")
car_id = canvas.create_image(485, 300, image=car, anchor="center")

#def moveUp(event):
    #canvas.move(car_id, 0, -10)

directions = {
    "w" : (0, -10), 
    "a" : (-10, 0), 
    "s" : (0, 10), 
    "d" : (10, 0),
}
def move(event):
    dx, dy = directions[event.keysym]
    canvas.move(car_id, dx, dy)

for key in directions:
    root.bind("<KeyPress-" + key + ">", move)

#root.bind("<KeyPress-w>", move)
#root.bind("<KeyPress-a>", move)
#root.bind("<KeyPress-s>", move)
#root.bind("<KeyPress-d>", move)

def main():
    print("Sim started")
    root.mainloop()

if __name__ == "__main__":
    main()
    
# dont make it move left or right, but as a veloctity based thing. 