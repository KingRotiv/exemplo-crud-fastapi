import schema as sc


def format_task_status(status: str) -> str:
    """
    Formata o status da task.
    """
    if status == sc.TaskStatus.pending:
        return "Pendente"
    else:
        return "Finalizada"
