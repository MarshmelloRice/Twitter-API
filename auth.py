import tweepy


class Authentication:
    def __init__(self, config):
        self.config = config
        self.api_key = self.config.api_key
        self.api_secret = self.config.api_secret
        self.access_token = self.config.access_token
        self.access_token_secret = self.config.access_token_secret

    def authentication(self):
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api
