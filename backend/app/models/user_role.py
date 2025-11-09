from sqlalchemy import Column, Integer, String, DateTime, UUID, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, foreign
from app.database import Base
from app.utils.uuid import gen_uuid


class UserRole(Base):
    __tablename__ = "user_role"

    def __init__(self, **kwargs):
        self.id = gen_uuid()
        super().__init__(id=self.id, **kwargs)


    id = Column(UUID, primary_key=True)
