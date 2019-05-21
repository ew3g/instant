from InstagramAPI import InstagramAPI
from instantApi import InstantApi
from utils import Utils
import config2
import time

class Unfollower:  
  def run(self):
    following = InstantApi.get_my_instagram_followings()
    followers = InstantApi.get_my_instagram_followers()
    followers_user_id = []

    for f in followers:
      followers_user_id.append(f['pk'])

    for f in following:
      following_user_id = f['pk']
      following_username = f['username']
      if(following_user_id not in followers_user_id):
        InstantApi.unfollow(following_user_id)
        print('unfollowed ' + str(following_username))