import matplotlib.animation as ani
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import evolution as evo
import particle


# x and y limits representing spacial limits of sim envirionment
sim_size = [10,10] 

# empty list for particle members
sys = [] 
n = 7 # number of elements in system

for i in range (n):
    # Add Particles to system positions and speed are 
    # randomized with randomValues = True and given a
    #  max speed of 25
   sys.append(particle.Particle())
   sys[i].randomize(sim_size,50,max_radius=15,max_speed=30)

# initializing figure and giving dimensions "sim_size"
fig,ax = plt.subplots()
ax.set_xlim(-sim_size[0],sim_size[0])
ax.set_ylim(-sim_size[1],sim_size[1])
circle_list = []
    
#create line object for each particle
for i in range(n):
    # code used as hexcode to randomly assign color to circles
    random_tuple =(random.random(),random.random(),random.random()) 
    # create circle object from particle data
    position = sys[i].getPos()
    x,y = position[0],position[1]
    circle = patches.Circle((x,y),radius=sys[i].getRadius(),color=random_tuple)
    # Add circle to figure- matplotlib.animation will take things from here as
    #  long as they are first added to the plot.
    ax.add_artist(circle) 
    # add circle to list for later reference
    circle_list.append(circle)



def animate_frame(i):
    # This function returns a list of line objects for a single frame 
    # of data, according to the needs of matplotlib.animation.funcAnimation().
    # The line objects involved in this fucntion represent particles 
    # goverened by classical physics mechanics 

    # increment the system of particles by one step
    evo.evolveOneStep(sys) 

    #  set line data to match position of each particle
    for j in range(n):
        #getting position data from current object
        position = sys[j].getPos() 
        x_data = position[0]
        y_data = position[1]
        # set x and y data for current line
        circle_list[j]._center = (x_data,y_data)
    
    return circle_list

# function from matplotlib.animation creates and displayes the animation
animation = ani.FuncAnimation(fig, func=animate_frame, interval= 100)
plt.show()
