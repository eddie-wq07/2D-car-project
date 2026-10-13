import tkinter as tk
import math
from pathlib import Path
from PIL import Image, ImageTk

head = 0 #heading angle
init_x = 485 #inital x coord
init_y = 300 #inital y coord
fwd_vel = 10 #forward velocity in pixels
ang_vel = 0.25 #angular velocity in rad (25 rad = ~14 degrees)
dt = 1 #change in time

asset_dir = Path(__file__).resolve().parent.parent / "assets"
image_path_car = asset_dir / "Car.png"
image_path_background = asset_dir / "Background.png"

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
car_id = canvas.create_image(init_x, init_y, image=car, anchor="center")

keybinds = {
    "w" : (-1, 0), 
    "s" : (1, 0), 
    "a" : (0, 1),
    "d" : (0, -1)
}


def compute_next(x, y, h, a, f): #input: x coord, y coord, heading angle, applied angular velocity, applied forward velocity
    h = h + (a * dt)
    x = x + (f * math.sin(h)) * dt
    y = y + (f * math.cos(h)) * dt 
    return x, y, h

def render(event):
    global head, car, init_x, init_y

    forward_input, turn_input = keybinds[event.keysym]
    velocity = forward_input * fwd_vel
    angular_velocity = turn_input * ang_vel

    init_x, init_y, head  = compute_next(init_x, init_y, head, angular_velocity, velocity)

  
    canvas.coords(car_id, init_x, init_y)

    rotated_image = car_image.rotate(
        math.degrees(head), 
        expand=True
    )
    car = ImageTk.PhotoImage(image=rotated_image)
    canvas.itemconfigure(car_id, image=car)

for key in keybinds:
    root.bind("<KeyPress-" + key + ">", render)

def main():
    print("Sim started")
    root.mainloop()

if __name__ == "__main__":
    main()
    
 
