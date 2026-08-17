class ProjectAssistant:

    def generate_summary(
        self,
        tasks,
        progress,
        risk
    ):

        total = len(tasks)

        completed = sum(
            1
            for task in tasks
            if task["status"].lower() == "completed"
        )

        delayed = sum(
            1
            for task in tasks
            if task["status"].lower() == "delayed"
        )

        pending = sum(
            1
            for task in tasks
            if task["status"].lower() == "pending"
        )

        if risk == "High":

            message = (
                "The project requires immediate attention. "
                "Several tasks may affect the project schedule."
            )

        elif risk == "Medium":

            message = (
                "The project is showing moderate risk. "
                "Delayed tasks should be monitored closely."
            )

        else:

            message = (
                "The project is progressing normally. "
                "Continue monitoring task deadlines."
            )

        return {
            "total_tasks": total,
            "completed_tasks": completed,
            "delayed_tasks": delayed,
            "pending_tasks": pending,
            "progress": round(progress, 2),
            "risk": risk,
            "message": message
        }

    def answer_question(
        self,
        question,
        tasks,
        risk
    ):

        question = question.lower()

        if "risk" in question:

            return f"The current predicted project risk is {risk}."

        if "progress" in question:

            completed = sum(
                1
                for task in tasks
                if task["status"].lower() == "completed"
            )

            progress = (
                completed / len(tasks) * 100
                if tasks
                else 0
            )

            return (
                f"Current project progress is "
                f"{round(progress, 2)}%."
            )

        if "delayed" in question:

            delayed = sum(
                1
                for task in tasks
                if task["status"].lower() == "delayed"
            )

            return f"There are {delayed} delayed task(s)."

        if "pending" in question:

            pending = sum(
                1
                for task in tasks
                if task["status"].lower() == "pending"
            )

            return f"There are {pending} pending task(s)."

        return (
            "I can provide information about "
            "project risk, progress, delayed tasks "
            "and pending tasks."
        )