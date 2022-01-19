# Innis Python Exercises

This repo holds the code and notes produced by instructors during the python module.

## Running Code Interactively in VS Code

In general, after performing the steps in the python setup section below, you can press shift + enter to evaluate a line or selected block of python code and see the results.

If your shift-enter does nothing, read below:

In order to run code, VS Code needs to think that the workspace is trusted. If you open up a single file, with, e.g. `code myfile.py` then that file might not be trusted. To do this, you need to open the project folder in VS Code.

```
code ~/codeup-data-science/python-exercises
```

OR

```
cd ~/codeup-data-science/python-exercises
code .
```

## Python Setup for VS Code

* Install the python extension from microsoft.
* In order to do the interactive code evaluation you’ll need the jupyter VS Code extension in addition to the python one. Search for jupyter and install the one from Microsoft.
* Open up your preferences (keyboard shortcut: command + , (comma)) and search for "jupyter: send selection". Make sure the checkbox there is checked.
* When prompted for a python interpreter, choose the one that comes from anaconda (i.e. you should see anaconda3 in the file path).
* If you have multiple versions of python installed, or you need to change the interpreter in VS Code every time you try to run code interactively, do this:

    1. Open up a terminal
    1. Open your settings in VS Code (command + ,)
    1. Search for "Python: Default Interpreter Path"
    1. In your terminal, run which python
    1. Copy the command output to the "Python: Default Interpreter Path" setting in VS Code

## Default Git Branch

If you have a master branch (i.e. you run `git status` and see `on branch master`), do this:

```
git branch -m main
git push -u origin main
git push origin :master
```

This renames your branch to main, pushes it, and deletes the old master branch.

Next run this:

```
git config --global init.defaultBranch main
```

Now any new repositories you create will have a main branch instead of master.

## VS Code Shortcuts

There are too many keyboard shortcuts to list here, but the most important (IMHO) are:

* Command + Shift + P: open the command palette. This is a searchable listing of all the actions you can perform in VS Code. I often discover new keyboard shortcuts by searching for a command / action here.
* Command + P: search through and open files if you opened VS Code in a directory with, e.g., `code .` or `code ~/codeup-data-science/python-exercises`.
* Control + backtick (the key above tab): open the terminal inside VS Code. If you opened VS Code in a directory, you will automatically be `cd`d to that directory.
