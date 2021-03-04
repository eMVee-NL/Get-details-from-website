#!/usr/bin/python3
import sys, os, time

def createDirectory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass

def createWorkingDirectory(path, website):
    try:
        os.chdir(path)
        createDirectory('Collected-Data')
        time.sleep(1)
        os.chdir('Collected-Data')
        time.sleep(1)
        createDirectory(website)
        print("Collected data will be written to directory Collected-Data/" + website)
    except FileExistsError:
        pass
    except Exception:
        pass