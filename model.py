from datetime import datetime

from pydantic import BaseModel, Field

import schema as sc


class NewTask(BaseModel):
    """
    Modelo para uma nova task.
    """

    title: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    status: sc.TaskStatus = sc.TaskStatus.pending


class EditTask(BaseModel):
    """
    Modelo para editar uma task.
    """

    updated_at: datetime = Field(default_factory=datetime.now)
    status: sc.TaskStatus
