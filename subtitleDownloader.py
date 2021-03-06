#!/usr/bin/env python
import os
import hashlib
import requests

list_of_subs = "http://api.thesubdb.com/?action=search&hash="
download_subs = "http://api.thesubdb.com/?action=download&hash="
headers = {"User-Agent" : "SubDB/1.0 (subsDown/0.1; http://theaidorus.github.io)"}
fileExtension = [".mkv", ".mp4", ".avi", ".3gp"]

def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

if __name__ == "__main__":
    for file in os.listdir(os.getcwd()):
        filename, ext  =  os.path.splitext(file)
        hashFile=0;
        if ext in fileExtension:
            hashFile = get_hash(file)
            respond = requests.get(list_of_subs+hashFile, headers=headers)
            subs = requests.get(download_subs+hashFile+"&language=en", headers=headers)
            if (subs.status_code==200):
                f = open(filename+".srt", 'w')
                f.write(subs.content)
                f.close()
