# Window Launcher
A single button to launch 7 programs/windows and move them into my favorite positions to immediately start being productive.

![](demo2.gif)

## Lessons Learned
### Documentation > Stack Overflow
I first wasted 4 hours trying to make [this](https://stackoverflow.com/questions/50494633/using-win32gui-to-center-a-window) stackoverflow-based solution work. Instead, I went straight to the documentation for the `win32gui` and built a new solution from scratch to finish in under an hour!

## Procedural Scripting > OOP
OOP is unnecessarily cumbersome for many things. Why do people create a class with a method, when they really just want a function? Why do people create a class with an attribute just to create 2-3 instances, when they can just create the naked attribute itself in the global scope?

## Small technical headaches 
- command line method to open (1) chrome websites, (3) applications, and (3) windows file explorer are all different. Learned a lot about windows command line!
- Windows directories which use backslashes can easily be accomodated in python by simply turning them into raw strings, i.e. `r"C:\Users\Elliot"`


## Technologies Practiced
1. Windows command line / Shell (what's the difference?)
2. `win32gui` package in python
3. git
4. markdown (to write readme.md on github)
5. Adobe Photoshop (to create & edit gifs)