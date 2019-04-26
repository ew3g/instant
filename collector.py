# -*- encoding: utf-8 -*-

#collector for images to post on instagram

import config
import os
import requests
from pypexels import PyPexels
from PIL import Image
from resizeimage import resizeimage
import ConfigParser
import time

photo_url = None
photo_photographer_name = None
photo_photographer_url = None
photo_id = None


pypexels = PyPexels(
  api_key=config.CONFIG['pypexels_api_key']
)

random_photo = pypexels.random(per_page=1)
for photo in random_photo.entries: 
  photo_url = str(photo.src['large'])
  photo_photographer_name = str(photo.photographer)
  photo_photographer_url = str(photo.photographer_url)
  photo_id = str(photo.id)

r = requests.get(photo_url)
path = 'img_post/' + photo_id + '.jpg'
f = open(path, 'wb')
f.write(r.content)
f.close()


config_parser = ConfigParser.RawConfigParser()

with open(path, 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(
          image, 
          [
            config.CONFIG['instagram_ratio_photo'],
            config.CONFIG['instagram_ratio_photo']
          ]
        )
        os.remove(path)
        cover.save(path, image.format)        
        config_parser.add_section(path)
        config_parser.set(path, 'photo_url', photo_url)
        config_parser.set(path, 'photo_photographer_name', photo_photographer_name)
        config_parser.set(path, 'photo_photographer_url', photo_photographer_url)
        config_parser.set(path, 'photo_id', photo_id)

        with open('img_post/data_img.cfg', 'a+') as config_file:
          config_parser.write(config_file)