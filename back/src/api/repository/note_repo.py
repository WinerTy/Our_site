
from .base import BaseRepository
from src.models.note_model import Note


class NoteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Note)

    # async def create(self, db: AsyncSession, data: dict) -> Note:
    #     db_obj = self.model(**data)
    #     db.add(db_obj)
    #     await db.commit()
    #     await db.refresh(db_obj)
    #     return db_obj


note_repository = NoteRepository()
