import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import math 
import particle

# This file includes a set of functions useful for plotting
# and animating objects of type: Particle.
def playTime(sys,delta_t):
    # time per step
    h = 0.01 
    # total time / time per step = number of steps required to evolve system.
    n = int(delta_t / h)
    for i in range(n):
        evolveOneStep(sys)


def playTimePlot(sys,delta_t,labels=False):
    # time per step
    h = 0.01 
    # total time / time per step = number of steps required to evolve system.
    n = int(delta_t / h)

    if labels: 
        labels = ' start'
    plotSystem(sys,labels) #plot starting point of system
    
    #evolve system by n steps
    for i in range(n):
        evolveOneStep(sys)

    if labels:
        labels = ' end'
    plotSystem(sys,labels) #plot system after time elapses
        
#evolve system at one step of 0.01 seconds
def evolveOneStep(sys):
    import math
    
    h = 0.01 # step size equal to 1/100th sec
    
    # loop through evolution equations for each particle in system
    for i in range (len(sys)):
        bounds = [10,10]
        wallBounce (sys[i],bounds)
        radius = sys[i].getRadius

        hit = collisionCheck(sys[i],sys)
        if hit:
            elasticCollision(sys[i],hit)

        #position evolution
        delta_x = h * sys[i].getV()[0] #position change in x-direction
        delta_y = h * sys[i].getV()[1] #position change in y-direction
        delta = np.array([delta_x,delta_y])
        sys[i].movePos(delta)
        
        #speed evolution
        delta_VX = h * sys[i].getAcc()[0] #speed change in x-direction
        delta_VY = h * sys[i].getAcc()[1] #speed change in y-direction
        sys[i].addV([delta_VX, delta_VY])

        #wallBounce (sys[i],bounds)
        
def collisionCheck(particle,sys):
    # This function checks if the obj, particle is colliding 
    # with a neighboring object or wall.
    
    # calling radius of particle in question
    r = particle.getRadius()
    # loop checks
    for neighbor in sys: 
        if not neighbor == particle:
            touch_distance = r + neighbor.getRadius()
            if dist(particle.getPos(), neighbor.getPos()) <= touch_distance:
                return neighbor
    return False


def dist(pos1,pos2):
    return math.sqrt( (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2 )


def wallBounce(particle, bounds):
    x , y = particle.getPos()
    vx , vy = particle.getV()
    r = particle.getRadius()

    if x + r >= bounds[0]:
        # right wall bounce
        particle.setV([-vx,vy])
    if abs(x - r) >= bounds[0]:
        # left wall bounce
         particle.setV([-vx,vy])
    if y + r >= bounds[1]:
        # top wall bounce
         particle.setV([vx,-vy])
    if abs(y - r) >= bounds[1]:
        # bottom wall bounce
         particle.setV([vx,-vy])

  


def elasticCollision(p1,p2):
    m1, m2 = p1.getMass(), p2.getMass()
    M = m1 + m2
    r1, r2 = p1.getPos(), p2.getPos()
    d = np.linalg.norm(np.array(r1) - np.array(r2))**2
    v1, v2 = p1.getV(), p2.getV()
    u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
    u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
    p1.setV(u1)
    p2.setV(u2)
        

#single frame of particle position and velocity vectors
def plotSystem (sys,labels=False):
    colors = ['blue','orange','green','red','yellow',
            'purple','black','cyan','wheat',
            'lime','darkred','gold','magenta','white',
            'gray','navy','dodgerblue','olivedrab']
    i = 0
    for obj in sys:
        #plotting object
        x,y = obj.getPos()
        plt.plot( x, y ,'o', color=colors[i] )
        #plotting velocity vector for obj
        plt.quiver( obj.getPos()[0],obj.getPos()[1], obj.getV()[0],obj.getV()[1] )
        plt.xlabel('position [m]')
        plt.ylabel('position [m]')
        # labels specifying the start and end locations
        if labels: 
            name = 'p ' + str(i)
            plt.text(x,y, name + labels)
        i = i+1


def init_figure(sys):
    # initialize figure and create a line object
    # for each particle in the system.

    # create plot and empty list to fill with line objects
    fig,ax = plt.subplots()
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    line_list =[]
    
    #create line object for each particle
    for i in range((len (sys))):
        line, = ax.plot(0,0,'o')
        line_list.append(line,)
    return fig, ax, line_list

def animate_frame(i):
    # This function returns a list of line objects for a single frame 
    # of data, according to the needs of matplotlib.animation.funcAnimation().
    # The line objects involved in this fucntion represent particles 
    # goverened by classical physics mechanics 

    # increment the system of particles by one step
    evolveOneStep(sys) 

    #  set line data to match position of each particle
    for j in range(len(sys)):
        #getting position data from current object
        position = sys[j].getPos() 
        x_data = position[0]
        y_data = position[1]
        # set x and y data for current line
        line_list[j].set_xdata(x_data) 
        line_list[j].set_ydata(y_data)

    return line_list
