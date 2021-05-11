# collision-course
2D circular-body simulation 

## Project Goal
 The goal of this project is to design a flexible simulation for systems of 2d particles. I am primarily looking to test my programming fundamentals in areas like data visualization, algorithm development, and OOP, but I am also looking to break into new skills. These skills being package assembly, version control and modular design. I have a background in mechanics and have always been fascinated by the programming that underpins popular media like video games and animation, so I'm enjoying this process.

## Contents
At this time Collision-course consists of three files: particle.py which consists of the class definition for particle, evolution.py to handle simulation advancement, and main.py to configure the simulation environemnt and call the animation

## Features
### Particle class
The particle class has a variety of helpful methods to enable the particle simultion behavior of the project. These include getter and setters for intrinsic properties such as mass and radius as well as the extrinsic properties of position velocity and acceleration. 

Instances of the particle class are more or less contained objects to keep track of store data. 

### Evolution functions
evolution.py is a file of functions for evolving systems of particle objects and handling collision events. All collisions are elastic, energy is conserved. (except when a particle escapes... still working on that)

### main file
This is file instantiates a figure and created graphable objects using particle's methods. Here you will find the function animate_frame which is called by Matplotlib.animation.funcanimation() to generate the animation's frames. main.py produces an animation like that below.

https://user-images.githubusercontent.com/50345746/117763281-67aac400-b1df-11eb-915e-ab90746eff68.mov
