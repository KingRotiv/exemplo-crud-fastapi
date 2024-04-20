from fastapi.exceptions import HTTPException

import model as md
import schema as sc
from db import db


def get_tasks() -> list[sc.Task]:
    """
    Retorna todas as task no banco de dados.
    """
    results = db.all()
    return [sc.Task(**r, doc_id=r.doc_id) for r in results]


def get_task(doc_id: int) -> sc.Task:
    """
    Retorna uma task pelo ID.
    """
    result = db.get(doc_id=doc_id)
    if result:
        return sc.Task(**result, doc_id=result.doc_id)
    raise HTTPException(status_code=404, detail="Task not found")


def create_task(task: sc.NewTask) -> sc.NewTaskResult:
    """
    Cria uma nova task.
    """
    new_task = md.NewTask(title=task.title)
    new_task_dump = new_task.model_dump(mode="json")
    doc_id = db.insert(new_task_dump)
    return sc.NewTaskResult(doc_id=doc_id)


def edit_task(doc_id: int, task: sc.EditTask) -> sc.Task:
    """
    Edita uma task.
    """
    get_task(doc_id)
    edited_task_dump = md.EditTask(**task.model_dump()).model_dump(mode="json")
    db.update(edited_task_dump, doc_ids=[doc_id])
    return get_task(doc_id)


def delete_task(doc_id: int) -> sc.Task:
    """
    Deleta uma task pelo doc_id.
    """
    task = get_task(doc_id)
    db.remove(doc_ids=[doc_id])
    return task
