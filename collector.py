# -*- encoding: utf-8 -*-

#collector for images to post on instagram

import config2
import os
import requests
from pypexelapi import PyPexelApi
from PIL import Image
from resizeimage import resizeimage
import configparser
import time
from utils import Utils

class Collector:
  def run(self):    
    try:
      pypexel_api = PyPexelApi(config2.CONFIG['pypexels_api_key'])
      random_photo = pypexel_api.get_single_random_photo()      
      r = requests.get(random_photo.photo_url)
      filename = random_photo.photo_id + '.jpg'
      path = 'img_post/' + filename
      f = open(path, 'wb')
      f.write(r.content)
      f.close()

      config = configparser.ConfigParser()
      config.read('data_img.cfg')

      with open(path, 'r+b') as f:
        with Image.open(f) as image:
          cover = resizeimage.resize_cover(
            image, 
            [
              config2.CONFIG['instagram_ratio_photo'],
              config2.CONFIG['instagram_ratio_photo']
            ]
          )
          os.remove(path)
          cover.save(path, image.format)        
          config.remove_section(filename)
          config.add_section(filename)
          config.set(filename, 'photo_url', random_photo.photo_url)
          config.set(filename, 'photo_photographer_name', random_photo.photographer_name)
          config.set(filename, 'photo_photographer_url', random_photo.photographer_url)
          config.set(filename, 'photo_id', random_photo.photo_id)

          with open('data_img.cfg', 'w') as config_file:
            config.write(config_file)
          
          print('Adicionado à biblioteca: ' + path)
    except Exception as e:
      print('erro: ' + str(e))    