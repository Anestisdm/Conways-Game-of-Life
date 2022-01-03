---
<p align="center">
<img src="https://user-images.githubusercontent.com/72802400/147390953-1710cda5-3ec6-48bb-9e9a-545ed4f917ee.jpg" align="center"><img src="https://user-images.githubusercontent.com/72802400/147390801-6d7ec12e-b95a-4462-9816-05e6d87af24a.jpg" width ="90" height"100" align = "center">
</p>

---

# Conway's Game of Life

### 1 - Scope
The purpose of this project is to implement the Conway's Game of Life with Python programming and using a simple graphical interface to represent the game.

### 2 - Game of Life
Conways’s Game Of Life is a Cellular Automation Method created by John Conway inspired by the biology field. This game is not required user input because is a zero-player game, 
which means that its evolution is determined by its initial state. Τhe Game of Life is built on a board of n x n cells (10 x 10 cells in our case), every cell has eight neighbor cells, as shown in the figure. 
A cell (i, j) in the simulation is accessed on an array[i][j], where i and j are the row and column indices, respectively. 
The value of a given cell at a given instant of time depends on the state of its neighbors at the previous generation. 

<p align="left">
<img src="https://user-images.githubusercontent.com/72802400/147940215-9f76af32-81c0-49ba-8eb3-2914bf167183.gif">
</p>

### 3 - Conway’s Game of Life Rules

1. Any alive cell with fewer than two alive neighbours dies, as if by underpopulation.
2. Any alive cell with two or three alive neighbours lives on to the next generation.
3. Any alive cell with more than three alive neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three alive neighbours becomes a live cell, as if by reproduction.

<p align="left">
<img src="https://user-images.githubusercontent.com/72802400/147938562-e771e5cc-adce-41fe-81ac-0b87e6209546.png">
</p>

### 4 - How it works

**Workstation Specifications**
- Windows 10 or Linux or MacOS, 64 bit
- RAM, 8GB required
- 128 GB Storage 
- 4 Core CPU

**Steps to run the application**
1. Clone this repository to Intellij
2. Run 'game_of_life' application from Intellij
3. Watch the evolution of the game

Note: If you want you can change from the application's main the size of the game board (line 371) and the generations of the game by changing the iterations (line 378)


### 5 - User Support
For help or new feature suggestions you can contanct with the development team.
