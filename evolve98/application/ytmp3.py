from pytube import YouTube 
import os 
def ytmp3(): 
 yt = YouTube( 
    str(input("URL\n: "))) 
  
 video = yt.streams.filter(only_audio=True).first() 
  
 destination = str(input("Hedef: ")) or '.'
  
 out_file = video.download(output_path=destination) 
  
 base, ext = os.path.splitext(out_file) 
 new_file = base + '.mp3'
 os.rename(out_file, new_file) 
  
 print(yt.title + " DOWNLOAD 200")