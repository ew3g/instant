# -*- encoding: utf-8 -*-
from pypexels import PyPexels
#from InstagramAPI import InstagramAPI as instagram_api
from instapy_cli import client
import urllib
from PIL import Image
from resizeimage import resizeimage
import os

py_pexels = PyPexels(api_key='563492ad6f91700001000001ed29a20a19ff4fe28cc40b6feb4ccbee')

photo_url = None
photo_photographer_name = None
photo_photographer_url = None
photo_id = None
random_photo = py_pexels.random(per_page=1)
for photo in random_photo.entries: 
  photo_url = str(photo.src['large'])
  photo_photographer_name = str(photo.photographer)
  photo_photographer_url = str(photo.photographer_url)
  photo_id = str(photo.id)
  import time
  #print(photo.src)
  #print dir(photo)

# print photo_url
# print photo_photographer_name
# print photo_photographer_url
# print photo_id



# f = open(photo_id, 'wb')
# f.write(urllib.urlopen(photo_url).read())
# f.close()

import requests
url = photo_url
r = requests.get(photo_url)
# print r.cookies
path = 'img_post/' + photo_id + '.jpg'
f = open(path, 'wb')
f.write(r.content)
f.close()

with open(path, 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [512, 512])
        os.remove(path)
        cover.save(path, image.format)


photo_path = 'img_post/'+ photo_id +'.jpg'
caption = "começamos aqui\n Créditos:" + photo_photographer_name + " \nlink: " + photo_photographer_url
# inst_api.uploadPhoto(photo_path, caption=caption, upload_id=None)

with client("edilson.w3g@gmail.com", "policia24horas") as cli:
  cli.upload(photo_path, caption=caption)
