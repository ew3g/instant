import time

from pypexelapi import Photo

class Utils:

  @staticmethod
  def sleep(start, end, increment):
    for i in xrange(start, end, increment):
      time.sleep(1)
      print i

  @staticmethod
  def parse_config_to_photo(session, config):
    photo = None
    if config is not None:
      photo_url = config.get(session, 'photo_url')
      photographer_name = config.get(session, 'photo_photographer_name')
      photographer_url = config.get(session, 'photo_photographer_url')
      photo_id = config.get(session, 'photo_id')
      photo = Photo(photo_url, photographer_name, photographer_url, photo_id)
    
    return photo

  @staticmethod
  def current_time_milliseconds():
    return int(round(time.time() * 1000))

    