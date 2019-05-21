from InstagramAPI import InstagramAPI
import config2

class InstantApi:
  @staticmethod
  def get_my_instagram_followers():
    api = InstagramAPI(
      config2.CONFIG['instagram_login'],
      config2.CONFIG['instagram_password']
    )

    api.login()
    user_id = api.username_id
    followers = []
    next_max_id = True
    while next_max_id:
      if next_max_id is True:
        next_max_id = ''
      
      _ = api.getUserFollowers(user_id, maxid = next_max_id)
      followers.extend(api.LastJson.get('users',[]))
      next_max_id = api.LastJson.get('next_max_id', '')
    return followers

  @staticmethod
  def get_my_instagram_followings():
    api = InstagramAPI(
      config2.CONFIG['instagram_login'],
      config2.CONFIG['instagram_password']
    )

    api.login()
    user_id = api.username_id
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

  @staticmethod
  def follow(username_id):
    api = InstagramAPI(
      config2.CONFIG['instagram_login'],
      config2.CONFIG['instagram_password']
    )

    api.login()
    api.follow(username_id)

  @staticmethod
  def unfollow(username_id):
    api = InstagramAPI(
      config2.CONFIG['instagram_login'],
      config2.CONFIG['instagram_password']
    )

    api.login()
    api.unfollow(username_id)