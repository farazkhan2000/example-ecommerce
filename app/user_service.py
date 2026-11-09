from app.models import User


class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, email):
        user = User(
            id=len(self.users) + 1,
            email=email,
        )

        self.users.append(user)

        return user