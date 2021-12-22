from pytube import YouTube

link = "https://www.youtube.com/watch?v=W52_91o4mw4&t=6s"

yt = YouTube(link)

print("Titulo: ", yt.title)
print("Views: ", yt.views)

#ys = yt.streams.get_highest_resolution()

#ys.download()