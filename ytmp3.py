#Coded By AdelwinNL

import os, sys

os.system("clear")

try:
  url = sys.argv[1]

except:
  print("""

        _                  ____           _ _ 
       | |                |___ \         | | |
  _   _| |_ _ __ ___  _ __  __) |_____ __| | |
 | | | | __| '_ ` _ \| '_ \|__ <______/ _` | |
 | |_| | |_| | | | | | |_) |__) |    | (_| | |
  \__, |\__|_| |_| |_| .__/____/      \__,_|_|
   __/ |             | |                      
  |___/              |_|                      
      .:Tools by AdelwinNL - DragonXploiter:.
        Tutorial : python ytmp3.py (urlnya)

""")
  sys.exit()

os.system("youtube-dl -x --audio-format mp3 -o 'hasil/%(title)s.%(ext)s' "+url)
print('\nSukes untuk mendownload lagu dari youtubenya hasil ada di folder hasil')
