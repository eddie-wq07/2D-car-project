### Intro to Simulation 2D Project

# Goal

The car starts in a position at the starting line. 

The red lines on the track do not let the car pass through. 

WASD style movement with space bar allowing constant acceleration. 

When car reaches the end (hits the wall), the game ends and there is a graphic says game over. Theres two buttons. One to restart, one to quit the application. You can always exit by hitting Esc which opens a menu with the two options. Restart or quit. 

The application opens by running main.py. 

There is at timer that counts down that tracks your score. 

# 3 Layers

1. World State: What state describes the car, and how does that change over time?
2. Platform: How does the program actually ask my OS to open the interface and recieve input?
3. Rendering: How to get world state rendering on the interface?

# Phases

0. Setup main.py so when I run it in terminal, it starts the program.
1. Setup platform such that the interface shows up as blank canvas.
2. Have constants for our assets and test populate the interface with static assets in pre-determined coordinate.
3. Implement world logic for car. 
--
TBD


# Open Questions

1. Program start. How does if __name__ == "__main__" that calls main(), actually start the program? I get why its necessary, but how is it written into the OS?

2. Why do we need a separate window and canvas in Tkinter?

3. How does tkinter actually create a window and run window.mainloop() 




