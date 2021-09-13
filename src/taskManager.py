from fuzzywuzzy import fuzz, process
from .tasks import tasks


class TaskManager:
    """[summary]
        provides interfaces to work with tasks
    """

    def __init__(self):
        self.tasks = tasks

    def task_compare(self, task: str, text: str) -> int:
        return fuzz.partial_ratio(task, text)

    def get_actual_task(self, task: str) -> str:
        return process.extractOne(task, self.tasks.keys())
