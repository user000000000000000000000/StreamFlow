from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from app.utils.uuid import gen_uuid

class Theme(Base):
    __tablename__ = "theme"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class Usertheme(Base): 
    __tablename__ = "user_theme"
    
    def __init__(self, **kwargs):
        self.id = gen_uuid()
        super().__init__(id=self.id, **kwargs)

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    theme_id = Column(Integer, ForeignKey("theme.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class StreamTheme(Base):
    __tablename__ = "stream_theme"
    
    def __init__(self, **kwargs):
        self.id = gen_uuid()
        super().__init__(id=self.id, **kwargs)

    id = Column(UUID, primary_key=True)
    stream_id = Column(UUID, ForeignKey("streams.id", ondelete="CASCADE"), nullable=False)
    theme_id = Column(Integer, ForeignKey("theme.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())