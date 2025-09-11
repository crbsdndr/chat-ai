from app.core import c_database

import enum
import uuid
from datetime import datetime

from sqlalchemy import Column, Text, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID, CITEXT
from sqlalchemy.orm import relationship


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"
    superadmin = "superadmin"


class User(c_database.Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(Text, nullable=False, unique=True)
    email = Column(CITEXT, nullable=False, unique=True)
    password_hash = Column(Text, nullable=False)
    full_name = Column(Text)
    role = Column(Enum(UserRole, name="user_role"), nullable=False, default=UserRole.user)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_login = Column(DateTime)

    conversations = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")
