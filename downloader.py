import urllib.request as req


def download(url):
    response= req.urlopen(url)
  
    local_file = open(url.split("/")[-1],"wb")
    print("downloading " + url.split("/")[-1])
    file_size = response.getheader("Content-Length")
    byte_block = 256
    downloaded_size = 0
    while True:
         buffer = response.read(byte_block)
         downloaded_size += len(buffer)
         if not buffer:
             local_file.close() 
             break
         local_file.write(buffer)
         status = (int(downloaded_size)/int(file_size))*100
         print("download status: " + str(int(status)) + "% ")
    local_file.close()         
           



download("https://www.sample-videos.com/video/mp4/240/big_buck_bunny_240p_30mb.mp4")       
 