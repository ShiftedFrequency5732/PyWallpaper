# PyWallpaper
Python script, for fetching random wallpapers from the web, for Windows OS.\
There are two versions, one that grabs image from Unsplash, and one that grabs Microsoft's daily Bing image.

You can use these scripts, in conjunction with Task Scheduler, in Windows OS.\
You can set-up a task, that repeats daily, or at startup, or at certain interval, to change wallpaper.

The package that you will need for this is `requests`, it can be installed with the following `pip install requests`.\

This script also uses one component from [ImageGlass](https://github.com/d2phap/ImageGlass) `igcmdWin10.exe`
It is a command line utility, that allows this script to change the background image of lockscreen.

## Disclaimer
It is recommended, if you will use this in conjunction with Task Scheduler, it is recommended to use `.pyw` instead of `.py` extension.\
That is because, python script with `.py` extension, will launch in console, and `.pyw` won't.
