import configparser


class Config:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    @property
    def api_key(self):
        return self.config.get("Twitter", "api_key")

    @property
    def api_secret(self):
        return self.config.get("Twitter", "api_secret")

    @property
    def access_token(self):
        return self.config.get("Twitter", "access_token")

    @property
    def access_token_secret(self):
        return self.config.get("Twitter", "access_token_secret")
