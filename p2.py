'''Importing os(operating system) because we need to find files with extension under input directory '''
import os
import sys
'''Initialized input directory and extension with variables dir and ext respectively.Getting current directory in dir and given specific directory to ext'''
dir=os.getcwd()         #'C:\\Users\\swath\\PycharmProjects\\DATA200Assignment\\venv'
ext='.py'
'''Defining function called findPath to find the directory is Absolute or Relative. If it is relative converting that to absolute'''
def findPath(dir,ext):
    try:
        if not os.path.isabs(dir):
            abs=os.path.abspath(dir).strip()
        else:
            abs=dir
    except Exception:
        print("Path not found")
    checkExtension(abs,ext)
'''Defining another function which takes inputs as dir and ext to find or loop through files in current directory and given specific extension.'''
'''Inside the loop joining every file to dir and storing it in path and checking if file endswith ext,
If yes joining file with directory and printing output.Else check if file is dir and calling function again by passing path and ext.'''
'''This function works recursively to find folders and extensions'''
def checkExtension(dir,ext):
    for f in os.listdir(dir):
        path=os.path.join(dir,f).strip()
        try:
            if os.path.isdir(path):
                checkExtension(path,ext)
            elif f.endswith(ext):
                print(os.path.join(dir,f))
        except Exception:
            print("File Not Found")


findPath(dir,ext)




















