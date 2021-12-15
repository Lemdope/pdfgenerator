class credential:
    def __init__(self):
        self._username = None
        self._password = None

# GETTER
    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

# SETTER
    @username.setter
    def username(self, value):
        self._username = value

    @password.setter
    def password(self, value):
        self._password = value
