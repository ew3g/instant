from InstagramAPI import InstagramAPI
import config2
import time

def mysleep(start, end, increment):
  for i in xrange(start, end, increment):
    time.sleep(1)
    print i

def get_followers(api, user_id):
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

def get_followings(api, user_id):
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

while True:
  api = InstagramAPI(config2.CONFIG['instagram_login'], config2.CONFIG['instagram_password'])
  api.login()

  user_id = api.username_id
  following = get_followings(api, user_id)
  followers = get_followers(api, user_id)
  followings_user_id = []
  for f in following:
    followings_user_id.append(f['pk'])

  for f in followers:
    follower_user_id = f['pk']
    if follower_user_id not in followings_user_id:
      api.follow(follower_user_id)
  
  mysleep(3600,0,-1)






