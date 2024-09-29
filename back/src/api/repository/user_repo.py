from .base import BaseRepository
from src.models.user_model import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)


user_repository = UserRepository()
