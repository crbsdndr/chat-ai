from app.core import c_database

import uuid
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

class Bot(c_database.Base):
    __tablename__ = "bots"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False, unique=True)
    provider = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    messages = relationship("Message", back_populates="bot")