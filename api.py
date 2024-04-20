from fastapi import APIRouter

import schema as sc
import repository as rp


router = APIRouter(prefix="/task", tags=["Task"])


@router.get("/", response_model=list[sc.Task], name="get_tasks")
def get_tasks() -> list[sc.Task]:
    """
    Retorna todas as tasks no banco de dados.
    """
    return rp.get_tasks()


@router.get("/{doc_id}", response_model=sc.Task, name="get_task")
def get_task(doc_id: int) -> sc.Task:
    """
    Retorna uma task pelo doc_id.
    """
    return rp.get_task(doc_id)


@router.post("/", response_model=sc.NewTaskResult, name="create_task")
def create_task(task: sc.NewTask) -> sc.NewTaskResult:
    """
    Cria uma nova task.
    """
    return rp.create_task(task)


@router.put("/{doc_id}", response_model=sc.Task, name="edit_task")
def edit_task(doc_id: int, task: sc.EditTask) -> sc.Task:
    """
    Edita uma task.
    """
    return rp.edit_task(doc_id, task)


@router.delete("/{doc_id}", response_model=sc.Task, name="delete_task")
def delete_task(doc_id: int) -> sc.Task:
    """
    Deleta uma task pelo doc_id.
    """
    return rp.delete_task(doc_id)
