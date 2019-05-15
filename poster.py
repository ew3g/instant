# -*- encoding: utf-8 -*-

from os import walk
from pypexelapi import Photo
import configparser
import ConfigParser
import random
import config2
from instapy_cli import client
import os
import time

def parse_config_to_photo(session,config):
  photo = None
  if config is not None:
    photo_url = config.get(session, 'photo_url')
    photographer_name = config.get(session, 'photo_photographer_name')
    photographer_url = config.get(session, 'photo_photographer_url')
    photo_id = config.get(session, 'photo_id')
    photo = Photo(photo_url, photographer_name, photographer_url, photo_id)
  
  return photo
  

library = []
popular_tags = ['#instagood', '#photooftheday', '#beautiful', '#happy', '#picoftheday', '#instadaily', '#style', '#instalike', '#life', '#beauty', '#amazing', '#photography', '#photo', '#cool', '#instapic', '#inspiration', '#instacool', '#blessed', '#happiness', '#awesome', '#nice', '#love']

while True:
  try:
    img = os.listdir('img_post')[0]
  except IndexError:
    img = None



  config = configparser.ConfigParser()
  config.read('data_img.cfg')
  if img is not None:
    if config.has_section(img):
      photo = parse_config_to_photo(img, config)  
      if photo is not None:
        cap = ''
        for tag in random.sample(popular_tags, 5):
          cap += tag + ' '

        cap += '\npor/by: ' + photo.photographer_name + " / " + photo.photographer_url

        photo_path = 'img_post/' + photo.photo_id + '.jpg'
        photo_path = str(photo_path)

        login = config2.CONFIG['instagram_login']
        password = config2.CONFIG['instagram_password']

        with client(login, password) as cli:
          
          cli.upload(photo_path, caption=cap)
          os.remove(photo_path)
          config.remove_section(img)
          with open('data_img.cfg', 'w') as config_file:
            config.write(config_file)        
    else:
      os.remove(photo_path)
  else:
    print 'Não há fotos na biblioteca'
  
  time.sleep(3600)
