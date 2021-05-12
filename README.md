# collision-course
2D circular-body simulation tool-kit

## Project Goal
 The goal of this project is to design a flexible simulation for systems of 2d particles. I am primarily looking to test my programming fundamentals in areas like data visualization, algorithm development, and OOP, but I am also looking to break into new skills. These skills being package assembly, version control and modular design. I have a background in mechanics and have always been fascinated by the programming that underpins popular media like video games and animation, so I'm enjoying this process.

## Contents
At this time Collision-course consists of three files: particle.py which consists of the class definition for particle, evolution.py to handle simulation advancement, and main.py to configure the simulation environemnt and call the animation

## Features
### Particle class
The [particle](https://github.com/darionb/collision-course/blob/main/particle.py) class has a variety of helpful methods to enable the particle-like behavior of its objects. These include getter and setters for intrinsic properties such as mass and radius as well as the extrinsic properties of position velocity and acceleration. 

> Instances of the particle class are more or less contained objects to keep track of store data. 

### Evolution functions
[Evolution.py](https://github.com/darionb/collision-course/blob/main/evolution.py) is a file of functions designed to work with instances of the class particle. Evolution.py currently includes 10 supported and non-supported(non_functional) function.

The Primary functions are organized as below: 

>playTime
>>evolveOneStep
>>>elasticCollision, wallBounce


>playTimePlot
>>evolveOneStep, plotSystem

### main file
This is file instantiates a figure and creates graphable objects using particle's built-in methods. Here you will find the function animate_frame which is called by [Matplotlib.animation.funcanimation()](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html) to generate the animation's frames. main.py produces an animation like that below. 

https://user-images.githubusercontent.com/50345746/117763281-67aac400-b1df-11eb-915e-ab90746eff68.mov

### Coming Features
The goal is to take most of the work done in main.py and transer it to evolution.py. The idea here is that a user will be able to import evolution and particle and use them as workhorses to quickly create 2D simulations and calculations.

