from source.controllers.tasks_controllers import TaskController
from source.controllers.priorities_controllers import PrioritiesController
from source.services.task_service import TaskService
from source.services.priority_service import PriorityService

task_service = TaskService(None)
task_controller = TaskController(task_service)

priorities_service = PriorityService(None)
priority_controller = PrioritiesController(priorities_service)