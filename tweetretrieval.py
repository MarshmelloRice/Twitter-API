import sys


class TweetRetrieval:
    def __init__(self, auth):
        self.auth = auth

    def get_user(self, screen_name):
        try:
            if self.auth.get_user(screen_name=screen_name):
                return True
        except Exception:
            print(sys.exc_info()[0], "occurred.")
            return False

    def get_tweet(self, screen_name, count):
        if self.get_user(screen_name):
            tweets = self.auth.user_timeline(screen_name=screen_name, count=count)
            return tweets
