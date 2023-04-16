from pytube import Playlist
from pytube import YouTube
from tkinter import filedialog
import webbrowser
print("Created by : Mahmoud Mohamed Mahmoud @ 2023 \n")
link = input("Enter YouTube Playlist URL : ")

print("Please Choose Directory To Save : ")
path = filedialog.askdirectory()

yt_playlist = Playlist(link)

i = 1
for video in yt_playlist.videos:

    video.streams.get_highest_resolution().download(output_path=path, filename=str(i)+" "+video.title+".mp4")
    print("Video Downloaded: ", video.title)
    i=i+1


print("\n All videos are downloaded....")