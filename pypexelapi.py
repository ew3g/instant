# -*- encoding: utf-8 -*-

from pypexels import PyPexels

class PyPexelApi:
  pypexels = None

  def __init__(self, pypexels_api_key=None):
    self.pypexels = PyPexels(
      api_key = pypexels_api_key
    )

  def get_single_random_photo(self):    
    random_photo =  self.pypexels.random(per_page=1)
    for photo in random_photo.entries: 
      photo_url = str(photo.src['large'])
      photo_photographer_name = photo.photographer.encode('utf-8')
      photo_photographer_url = str(photo.photographer_url)
      photo_id = str(photo.id)
      photo = Photo(photo_url, photo_photographer_name, photo_photographer_url, photo_id)
    
    return photo

  def get_photos_by_search(self, search_term=None, limit=None):
    list_photos = []
    search_results_page = self.pypexels.search(query=search_term, per_page=limit)
    for pexel_photo in search_results_page.entries:
      photo_url = str(pexel_photo.src['large'])
      photo_photographer_name = str(pexel_photo.photographer)
      photo_photographer_url = str(pexel_photo.photographer_url)
      photo_id = str(pexel_photo.id)
      photo = Photo(photo_url, photo_photographer_name, photo_photographer_url, photo_id)
      list.append(photo)
    
    return list_photos

  def get_popular_photos(self, limit=None):
    list_photos = []
    popular_photos_page = self.pypexels.popular(per_page=limit)
    for pexel_photo in popular_photos_page.entries:
        photo_url = str(pexel_photo.src['large'])
        photo_photographer_name = str(pexel_photo.photographer)
        photo_photographer_url = str(pexel_photo.photographer_url)
        photo_id = str(pexel_photo.id)
        photo = Photo(photo_url, photo_photographer_name, photo_photographer_url, photo_id)
        list_photos.append(photo)
      
    return list_photos





class Photo:
  photo_url = None
  photographer_name = None
  photographer_url = None
  photo_id = None

  def __init__(self, photo_url, photographer_name, photographer_url, photo_id):
    self.photo_url = photo_url
    self.photographer_name = photographer_name
    self.photographer_url = photographer_url
    self.photo_id = photo_id