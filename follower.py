# -*- encoding: utf-8 -*-
from InstagramAPI import InstagramAPI
import config2

user=config2.CONFIG['instagram_login']
password=config2.CONFIG['instagram_password']

def getTotalFollowers(api, user_id):
  followers = []
  next_max_id = True
  while next_max_id:
      # first iteration hack
      if next_max_id is True:
          next_max_id = ''

      _ = api.getUserFollowers(user_id, maxid=next_max_id)
      followers.extend(api.LastJson.get('users', []))
      next_max_id = api.LastJson.get('next_max_id', '')
  return followers

def getTotalFollowings(api, user_id):
  api.getUsernameInfo(user_id)
  api.LastJson
  following = []
  next_max_id = True
  while next_max_id:
      print next_max_id
      # first iteration hack
      if next_max_id is True:
          next_max_id = ''
      _ = api.getUserFollowings(user_id, maxid=next_max_id)
      following.extend(api.LastJson.get('users', []))
  next_max_id = api.LastJson.get('next_max_id', '')
  return following



class Follower():  
  def run(self):
    api = InstagramAPI(user,password)
    api.login()
    mid = 2140753331
    followers = getTotalFollowers(api, mid)
    followings = getTotalFollowings(api, mid)
    followers_id = []
    followings_id = []
    for f in followers:
      follower_id = f['pk']
      followers_id.append(follower_id)

    for f in followings:
      following_id = f['pk']
      followings_id.append(following_id)

    #follower
    for f_id in followers_id:
      if f_id not in followings_id:
        api.follow(f_id)
        print('followed: ' + str(f_id))

    #unfollower
    for f_id in followings_id:
      if f_id not in followers_id:
        api.unfollow(f_id)
        print('unfollowed: ' + str(f_id))

    print('followers: ' + str(len(followers_id)))
    print('following: ' + str(len(followings_id)))