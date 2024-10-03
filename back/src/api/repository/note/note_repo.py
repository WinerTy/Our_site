from ..base.base import BaseRepository
from src.models.note.note_model import Note


class NoteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Note)


note_repository = NoteRepository()
