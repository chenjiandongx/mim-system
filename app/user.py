
class User:

    def __init__(self, username):
        self.id = username

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id
