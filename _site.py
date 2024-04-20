import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import schema as sc
import filter as ft


full_path = os.path.realpath(__file__)
path = os.path.dirname(full_path)

router = APIRouter(tags=["Task"], include_in_schema=False)
templates = Jinja2Templates(directory=os.path.join(path, "templates"))
templates.env.filters["format_task_status"] = ft.format_task_status


@router.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    data = {"request": request, "status": sc.TaskStatus}
    return templates.TemplateResponse(name="index.html", context=data)
