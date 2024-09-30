from src.models.site.type_model import SiteType
from .base import BaseRepository


class SiteTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(SiteType)


site_type_repository = SiteTypeRepository()
