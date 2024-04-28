import speedtest
import math
def maintest(size_byte):
 i = int(math.floor(math.log(size_byte, 1024)))
 power = math.pow(1024, i)
 size = round(size_byte / power, 2)
 return f"{size} Mbps"

def sptest():
 
 wifi = speedtest.Speedtest()
 print("\nDownload hızı ölçülüyor...")
 download_speed = wifi.download()

 print("\nUpload hızı ölçülüyor...")
 upload_speed = wifi.upload()

 print("\nDownload:", maintest(download_speed))
 print("Upload:", maintest(upload_speed))
