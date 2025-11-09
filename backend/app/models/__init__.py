from app.models.user import User
from app.models.stream import Stream
from app.models.role import Role
from app.models.user_role import UserRole
from app.models.theme import Theme, Usertheme, StreamTheme

# Инициализируем relationships после всех импортов
from sqlalchemy.orm import relationship

# User relationships
User.user_theme = relationship("Usertheme", back_populates="user", cascade="all, delete-orphan")
User.streams = relationship("Stream", back_populates="author")

# Stream relationships
Stream.author = relationship("User", back_populates="streams")
Stream.stream_theme = relationship("StreamTheme", back_populates="stream", cascade="all, delete-orphan")

# Theme relationships  
Theme.user_theme = relationship("Usertheme", back_populates="theme", cascade="all, delete-orphan")
Theme.stream_theme = relationship("StreamTheme", back_populates="theme", cascade="all, delete-orphan")

# Usertheme relationships
Usertheme.user = relationship("User", back_populates="user_theme")
Usertheme.theme = relationship("Theme", back_populates="user_theme")

# StreamTheme relationships
StreamTheme.stream = relationship("Stream", back_populates="stream_theme")
StreamTheme.theme = relationship("Theme", back_populates="stream_theme")

__all__ = ["User", "Stream", "Role", "UserRole", "Theme", "Usertheme", "StreamTheme"]