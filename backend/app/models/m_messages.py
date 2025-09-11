from app.core import c_database


import enum
import uuid

from datetime import datetime
from sqlalchemy import Column, Text, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

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
