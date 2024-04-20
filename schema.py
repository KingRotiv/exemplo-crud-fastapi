from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """
    Opções do status de uma task.
    """

    pending = "pending"
    finished = "finished"


class NewTask(BaseModel):
    """
    Esquema para uma nova task.
    """

    title: str = Field(min_length=1, max_length=20)


class NewTaskResult(BaseModel):
    """
    Esquema do retorno de uma nova task.
    """

    doc_id: int


class Task(BaseModel):
    """
    Esquema base de uma task.
    """

    doc_id: int
    title: str
    created_at: datetime
    updated_at: datetime
    status: str


class EditTask(NewTask):
    """
    Esquema para editar uma task.
    """

    status: TaskStatus
