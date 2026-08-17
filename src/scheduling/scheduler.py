class TaskScheduler:

    PRIORITY_WEIGHT = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    def calculate_task_score(self, task):

        priority_score = self.PRIORITY_WEIGHT.get(
            task["priority"],
            1
        )

        status_score = 0

        if task["status"].lower() == "delayed":
            status_score = 3

        elif task["status"].lower() == "pending":
            status_score = 1

        return priority_score + status_score

    def prioritize_tasks(self, tasks):

        active_tasks = [
            task
            for task in tasks
            if task["status"].lower() != "completed"
        ]

        return sorted(
            active_tasks,
            key=self.calculate_task_score,
            reverse=True
        )

    def get_recommendations(self, tasks, risk):

        recommendations = []

        delayed_tasks = [
            task
            for task in tasks
            if task["status"].lower() == "delayed"
        ]

        pending_tasks = [
            task
            for task in tasks
            if task["status"].lower() == "pending"
        ]

        if risk == "High":

            recommendations.append(
                "Immediately prioritize delayed tasks."
            )

            recommendations.append(
                "Redistribute workload among team members."
            )

            recommendations.append(
                "Review project deadlines."
            )

        elif risk == "Medium":

            recommendations.append(
                "Monitor delayed tasks closely."
            )

            recommendations.append(
                "Increase priority of critical pending tasks."
            )

        else:

            recommendations.append(
                "Project is progressing normally."
            )

            recommendations.append(
                "Continue monitoring task deadlines."
            )

        if delayed_tasks:

            recommendations.append(
                f"{len(delayed_tasks)} delayed task(s) require attention."
            )

        if pending_tasks:

            recommendations.append(
                f"{len(pending_tasks)} pending task(s) remain."
            )

        return recommendations