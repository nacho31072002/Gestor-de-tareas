from api.source.controllers.tasks_controllers import TaskController
from api.source.controllers.priorities_controllers import PrioritiesController
from api.source.services.task_service import TaskService
from api.source.services.priority_service import PriorityService

task_service = TaskService(None)
task_controller = TaskController(task_service)

priorities_service = PriorityService(None)
priority_controller = PrioritiesController(priorities_service)