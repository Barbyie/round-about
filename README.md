# Minecraft Server Backup writen completely in Python.

- Round About started as an idea for a first project when I decided to study python. I always had an issue where I would end up losing my server or something happened and I was not able to recover what I had lost.
- This program will only work on Linux, and was not tested on Windows, so feel free to try.
- At first, it was written using a functional programming language, but I decided to challenge myself and rewrite using OOP.  
- The script was programmed having in mind that people would like to use a service manager to start the script (I only tested with systemd, but it should work with OpenRC), since it makes it easier to manage when you want the backups to run.

 
# How to use ?

- First, run the settings.py and reply with your full path for each folder requested.
- Once that is done, it will create a file called parameters.pk1 that will contain the input from the previous file.
- You do not necessarily need to place the main.py inside your Server folder, but I would recommend doing so.
- Now run the main.py whenever you start your server, and it should trigger backups based in the timeframe that you have configured in the settings.py.
- If you run the program manually, you can stop it once you do not need it anymore, or if you use a service manager, it should stop once it receives a SIGINT or SIGTERM.


# Additional Information

- As I said before, this was the first "real" project that I made. It was made for me and my friends to use, but since I imagined other people would have similar hurdles, I decided to share it here.
- This program is far from perfect, but it does its job.
- Feel welcome to add any constructive criticism or improve this program if you see potential in it.
