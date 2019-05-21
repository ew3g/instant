from InstagramAPI import InstagramAPI
from instantApi import InstantApi
import config2
import time
from utils import Utils

class Follower():
  def run(self):
    following = InstantApi.get_my_instagram_followings()
    followers = InstantApi.get_my_instagram_followings()
    followings_user_id = []
    for f in following:
      followings_user_id.append(f['pk'])

    for f in followers:
      follower_user_id = f['pk']
      follower_username = f['username']      
      if follower_user_id not in followings_user_id:
        InstantApi.follow(follower_user_id)
        print('followed ' + str(follower_username))    