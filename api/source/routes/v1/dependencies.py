from api.source.controllers.tasks_controllers import TaskController
from api.source.services.task_service import TaskService


task_service = TaskService()
task_controller = TaskController(task_service)
