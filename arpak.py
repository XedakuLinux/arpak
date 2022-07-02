# import required modules
import os
import time
import sys
import distro

if distro.name() == 'Arch Linux':
    print("Running on Arch Linux, Arpak will function normally")
else:
    print("Running on a non-Arch Linux distro, Arpak will now exit")
    sys.exit()

try:
    if sys.argv[1] == "--help":
        print("Arpak v1.1")
        print("This program is licensed under the GNU General Public License v3.0.")
        print("You can find a copy of the license in the LICENSE file.")
        print("Copyright (c) 2022, Archimax")
        print("")
        print("Arguments:")
        print("install: Install a package")
        print("localinstall: Install a local package")
        print("remove: Remove a package")
        print("update: Update the package list")
        print("list: List all packages")
        print("search: Search for a package")
        print("upgrade: Upgrade a package")
        print("")
        print("Usage example:")
        print("arpak install nodejs")
    elif sys.argv[1] == "install":
        print("Installing " + sys.argv[2])
        # check if user is root
        if os.geteuid() != 0:
            root = False
        if root == False:
            os.system("sudo pacman -S " + sys.argv[2])
        else:
            os.system("pacman -S " + sys.argv[2])
    elif sys.argv[1] == "remove":
        print("Removing " + sys.argv[2])
        # check if user is root
        if os.geteuid() != 0:
            root = False
        if root == False:
            os.system("sudo pacman -R " + sys.argv[2])
        else:
            os.system("pacman -R " + sys.argv[2])
    elif sys.argv[1] == "update":
        print("Updating package list")
        # check if user is root
        if os.geteuid() != 0:
            root = False
        if root == False:
            os.system("sudo pacman -Sy")
        else:
            os.system("pacman -Sy")
    elif sys.argv[1] == "list":
        print("Listing all packages")
        os.system("pacman -Q")
    elif sys.argv[1] == "search":
        print("Searching for " + sys.argv[2])
        os.system("pacman -Ss " + sys.argv[2])
    elif sys.argv[1] == "localinstall":
        print("Installing local package " + sys.argv[2])
        # check if user is root
        if os.geteuid() != 0:
            root = False
        if root == False:
            os.system("sudo pacman -U " + sys.argv[2])
        else:
            os.system("pacman -U " + sys.argv[2])
    elif sys.argv[1] == "upgrade":
        print("Upgrading " + sys.argv[2])
        # check if user is root
        if os.geteuid() != 0:
            root = False
        if root == False:
            os.system("sudo pacman -Syu " + sys.argv[2])
        else:
            os.system("pacman -Syu" + sys.argv[2])
     elif sys.argv[1] == "--version":
        print("Arpak - version 1.1")
        print("Running on " + distro.name())
    else:
        print("Arpak - Invalid argument")
        print("Use --help for more information")
        sys.exit(1)
except IndexError:
    print("Arpak - no arguments given")
    print("Use --help for help")
    sys.exit(1)

    
