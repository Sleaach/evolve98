from pytube import YouTube

def youtb():
 try:
    link = input("Link: ")
    yt = YouTube(link)
    yr = yt.streams.get_highest_resolution()
    print("Video OK")
    yr.download(filename='video')
 except Exception as e:
  print(f"Hata! {e}")
