class User:

    UserId = int()
    UserGroup = int()

    def __init__(self, _userId, _userGroup):
        self.UserId, self.UserGroup = _userId, _userGroup