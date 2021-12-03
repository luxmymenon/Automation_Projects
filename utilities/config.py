class Config:
    def __init__(self, env):

        self.base.url = {
            "dev": "http://devport123.abc.com",
            "qa": "http://qaport123.abc.com"
        }[env]
