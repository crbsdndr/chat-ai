from app.core import c_database

import enum
import uuid 
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB, CITEXT
from sqlalchemy import Column, Text, DateTime, ForeignKey, Enum


class Conversation(c_database.Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")

class Bot(c_database.Base):
    __tablename__ = "bots"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False, unique=True)
    provider = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    messages = relationship("Message", back_populates="bot")

class MsgRole(enum.Enum):
    user = "user"
    model = "model"
    system = "system"


class Message(c_database.Base): 
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True),
                             ForeignKey("conversations.id", ondelete="CASCADE"),
                             nullable=False)
    bot_id = Column(UUID(as_uuid=True), ForeignKey("bots.id", ondelete="SET NULL"))
    role = Column(Enum(MsgRole, name="msg_role"), nullable=False)
    text = Column(Text, nullable=False)
    gen_params = Column(JSONB, default=dict, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    conversation = relationship("Conversation", back_populates="messages")
    bot = relationship("Bot", back_populates="messages")

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
