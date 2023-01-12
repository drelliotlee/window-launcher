# Window Launcher
A single button to launch 7 programs/windows and move them into my favorite positions to immediately start being productive.

![](demo.gif)

VS Code, Chrome, Obsidian, ChatGPT, Gmail, Windows File Explorer, and my To-do App
All in 1 click!

## Lessons Learned
I first wasted 4 hours trying to make [this](https://stackoverflow.com/questions/50494633/using-win32gui-to-center-a-window) stackoverflow-based solution work. Instead, I went straight to the documentation for the `win32gui` and built a new solution from scratch to finish in under an hour!

This project was less about the actual application, and using best coding best practices/habits, such as:
- frequent commits to github, all via command line
- thorough documentation and commenting of my code
- using my mouse as little as possible to practice VScode's keyboard shortcuts

## Small headaches I had
- `subprocess.Popen()` in python requires the additional argument `shell=True` for commands such as `cd` and `dir`
- Windows directories which use backslashes can easily be accomodated in python by simply turning them into raw strings, i.e. `r"C:\Users\Elliot"`
- OOP still seems unnecessarily cumbersome to me. My scientific programming background still makes me think purely procedural programming / scripting is superior.