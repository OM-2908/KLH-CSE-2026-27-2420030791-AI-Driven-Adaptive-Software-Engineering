class TaskManager:

    def __init__(self):
        self.tasks = []
        self.task_id = 1

    def add_task(self, name, priority="Medium", deadline=None):
        task = {
            "id": self.task_id,
            "name": name,
            "priority": priority,
            "deadline": deadline,
            "status": "Pending"
        }

        self.tasks.append(task)
        self.task_id += 1

        return task

    def update_status(self, task_id, status):

        valid_statuses = [
            "Pending",
            "Completed",
            "Delayed"
        ]

        if status not in valid_statuses:
            return False

        for task in self.tasks:

            if task["id"] == task_id:
                task["status"] = status
                return True

        return False

    def get_tasks(self):
        return self.tasks

    def calculate_progress(self):

        if not self.tasks:
            return 0

        completed = sum(
            1
            for task in self.tasks
            if task["status"].lower() == "completed"
        )

        return (completed / len(self.tasks)) * 100