from .base import BaseRepository
from src.models.service_model import Service


class ServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Service)


service_repository = ServiceRepository()
