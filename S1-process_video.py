# converts the Videos to MP3 using ffmpg and store it in a folder 
import os
import subprocess


files = os.listdir("ALL_Tutorials")

for file in files:
    tutorial_number, tutorial_title = file.split(" ", 1)
    print("Number:", tutorial_number)
    print("Title:", tutorial_title)
    # subprocess.run(["ffmpeg","-i",f"ALL_Tutorials/{file}",f"audios/{tutorial_number}_{tutorial_title}.mp3"])

    subprocess.run(["ffmpeg","-y", "-i", f"ALL_Tutorials/{file}",f"audios/{tutorial_number}_{tutorial_title}.mp3"])
    print("-" * 40)
