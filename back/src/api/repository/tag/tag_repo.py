from ..base.base import BaseRepository
from src.models.tag.tag_model import Tag


class TagRepository(BaseRepository):
    def __init__(self):
        super().__init__(Tag)


tag_repository = TagRepository()
