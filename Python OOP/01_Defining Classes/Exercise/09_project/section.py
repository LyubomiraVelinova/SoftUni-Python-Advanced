from project.task import Task


class Section:
    name: str
    tasks: list

    def __init__(self, name: str):
        self.name = name
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, new_task: Task):
        collection = [task.name for task in self.tasks]
        if new_task.name in collection:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        collection = [task.name for task in self.tasks]
        if task_name in collection:
            task_index = collection.index(task_name)
            current_task = self.tasks[task_index]
            current_task.completed = True
            self.completed_tasks.append(current_task)
            return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for completed_task in self.completed_tasks:
            self.tasks.pop(self.tasks.index(completed_task))
            removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        tasks_print = [task.details() for task in self.tasks]
        return f"Section {self.name}:" + "\n" + "\n".join(tasks_print)
