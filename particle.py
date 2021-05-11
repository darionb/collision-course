import numpy as np
import math
import random

class Particle:
    
    """ a class representing a particle in two-dimensional space """
    
    def __init__(self, mass=1, radius=0.1 , position=[0,0], velocity=[0,0],
     randomValues=False, bounds = [5,5], max_radius=7, max_speed=5, max_mass=100, max_charge=1):

        self.mass = mass
        self.radius = radius
        self.position = np.asarray(position) 
        self.v = np.asarray(velocity)
        if velocity[0] == 0:
            self.angleV = float('inf')
        else:
            self.angleV = math.atan(velocity[1]/velocity[0])
   
        self.acceleration = np.asarray([0,0])
        self.charge = 0
        if randomValues:
            self.randomize(bounds, max_radius, max_speed, max_mass, max_charge)


    # Methods which return the specified class properties
    def getMass (self):
        return self.mass
    def getRadius(self):
        return self.radius
    def getPos (self):
        return self.position
    def getV (self):
         return self.v 
    def getAngleV (self):
        return self.angleV
    def getAcc (self):
        return self.acceleration
    def getCharge (self):
        return self.charge
    
    def setMass(self, new_mass):
        self.mass = new_mass
    def setRadius(self, new_radius):
        self.radius = new_radius
    def movePos (self,delta):
        self.position = np.add(self.position, delta)  
    def setPos (self, pos):
        self.position = np.asarray(pos)        
    def addV (self,delta_v):
        self.v = np.asarray( [self.v[0] + delta_v[0],
         self.v[1] + delta_v[1] ] )
        self.angleV = math.atan(self.v[1]/self.v[0])
    def setV (self,v_new):
        self.v = np.asarray(v_new)
        self.angleV = math.atan(self.v[1]/self.v[0]) 
    def setCharge (self,q):
        self.charge = q  
    def randomize(self, bounds, max_mass, max_radius=10, max_speed=100, max_charge = 1):
        x_bound = bounds[0]
        y_bound = bounds[1]
        self.setPos([random.randrange(-x_bound,x_bound), random.randrange(-y_bound,y_bound)])
        self.setRadius(0.1*random.randrange(5,max_radius))
        self.setV([0.01*random.randrange(-max_speed*100,max_speed*100), 0.01*random.randrange(-max_speed*100,max_speed*100)])
        self.setCharge(random.randrange(-max_charge,max_charge))  #needs functionality !
        self.setMass(random.randrange(1,max_mass))
        

        
    def __str__(self):
        return "this particle has the following properties: " + str(self.getMass()) +'[kg]  '+ str(self.getPos()) + '[m]  ' + str(self.getV())+ '[m/s] '+ str(self.getCharge())+ '[C]'

    