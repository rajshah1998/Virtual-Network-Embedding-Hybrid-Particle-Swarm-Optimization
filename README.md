#Virtual-Network-Embedding-Hybrid-Particle-Swarm-Optimization
Project Title :- Virtual-Network-Embedding-Hybrid-Particle-Swarm-Optimization

Project Description :-

This project contains all the details about how Virtual Network request is generated dynamically and embedding in the existing substrate 
network using hybrid particle swarm optimization.

For this project I have used python as a primary programming language.
Tools: alib, Google Colab.


Table of Contents:-

The root folder contains following files & directories:-

1. Generate.ipynb - This is main file where the code resides.
2. Readpickle.py - This file consists of code for generating the substrate network
3. vne.py - This file is used to create the virtual network request and embbed it on the substrate network
4. graph.py - Generates the graph. This is the dependency file for Generate.ipynb file.
5. graph_extraction.py - Extract the graph features. This is the dependency file for Generate.ipynb file.
6. input.pickle - This file contains the parameters of the graph used to create the substrate network.
7. norm.py - This file contains the code for normalisation.
8. PSO Folder:
	A. app.py - this file shows in how many iterations it will reach global minima and hence reduces overall cost
	B. _init_.py - this file is used for initialisation of parameters of each particle in the swarm


How to run/view the project :-

Recommended Tool : - Google Colab

Steps:-

1. Upload Generate.ipynb file.
2. Along with that upload all the files as they are the dependencies for the main file.
3. Run each cell of Generate.ipynb file.
