import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from flask import Flask, render_template_string, request

from task_management.task_manager import TaskManager
from risk_prediction.risk_model import RiskPredictionModel
from scheduling.scheduler import TaskScheduler
from ai.assistant import ProjectAssistant


app = Flask(__name__)

# -----------------------------------------
# CREATE PROJECT COMPONENTS
# -----------------------------------------

manager = TaskManager()
risk_model = RiskPredictionModel()
scheduler = TaskScheduler()
assistant = ProjectAssistant()


# -----------------------------------------
# TRAIN AI MODEL
# -----------------------------------------

risk_model.train()


# -----------------------------------------
# SAMPLE PROJECT TASKS
# -----------------------------------------

manager.add_task(
    "Develop Login Module",
    priority="High",
    deadline="2026-08-25"
)

manager.add_task(
    "Create Database",
    priority="Medium",
    deadline="2026-08-27"
)

manager.add_task(
    "Develop Dashboard",
    priority="High",
    deadline="2026-08-28"
)

manager.add_task(
    "Testing",
    priority="Medium",
    deadline="2026-08-30"
)

manager.update_status(1, "Completed")
manager.update_status(2, "Delayed")


# -----------------------------------------
# DASHBOARD
# -----------------------------------------

@app.route("/")
def dashboard():

    tasks = manager.get_tasks()

    progress = manager.calculate_progress()

    risk = risk_model.predict_from_tasks(
        tasks,
        team_size=5
    )

    prioritized_tasks = scheduler.prioritize_tasks(
        tasks
    )

    # Calculate priority scores
    for task in prioritized_tasks:

        task["score"] = scheduler.calculate_task_score(
            task
        )

    recommendations = scheduler.get_recommendations(
        tasks,
        risk
    )

    summary = assistant.generate_summary(
        tasks,
        progress,
        risk
    )

    return render_template_string(
        HTML,
        tasks=tasks,
        prioritized_tasks=prioritized_tasks,
        recommendations=recommendations,
        summary=summary
    )


# -----------------------------------------
# ADD TASK
# -----------------------------------------

@app.route("/add", methods=["POST"])
def add_task():

    name = request.form.get("name")
    priority = request.form.get("priority")
    deadline = request.form.get("deadline")

    if name:

        manager.add_task(
            name=name,
            priority=priority,
            deadline=deadline
        )

    return dashboard()


# -----------------------------------------
# UPDATE TASK
# -----------------------------------------

@app.route("/update/<int:task_id>/<status>")
def update_task(task_id, status):

    status = status.capitalize()

    manager.update_status(
        task_id,
        status
    )

    return dashboard()


# -----------------------------------------
# DASHBOARD HTML
# -----------------------------------------

HTML = """

<!DOCTYPE html>

<html>

<head>

<title>
AI-Driven Adaptive Software Engineering
</title>

<style>

body {

    font-family: Arial, sans-serif;

    background: #f4f6f8;

    margin: 0;

    padding: 30px;

}

.container {

    max-width: 1200px;

    margin: auto;

}

h1 {

    color: #222;

}

.card {

    background: white;

    padding: 20px;

    margin: 15px 0;

    border-radius: 10px;

}

.stats {

    display: flex;

    gap: 20px;

    flex-wrap: wrap;

}

.stat {

    flex: 1;

    min-width: 150px;

    background: white;

    padding: 20px;

    border-radius: 10px;

    text-align: center;

}

table {

    width: 100%;

    border-collapse: collapse;

}

th,
td {

    padding: 12px;

    border-bottom: 1px solid #ddd;

    text-align: left;

}

input,
select,
button {

    padding: 10px;

    margin: 5px;

}

button {

    cursor: pointer;

}

a {

    text-decoration: none;

    margin-right: 5px;

}

</style>

</head>


<body>


<div class="container">


<h1>

AI-DRIVEN ADAPTIVE SOFTWARE ENGINEERING

</h1>


<p>

Intelligent Project Management System

</p>


<!-- PROJECT STATISTICS -->

<div class="stats">


<div class="stat">

<h3>Total Tasks</h3>

<h2>
{{ summary.total_tasks }}
</h2>

</div>


<div class="stat">

<h3>Completed</h3>

<h2>
{{ summary.completed_tasks }}
</h2>

</div>


<div class="stat">

<h3>Delayed</h3>

<h2>
{{ summary.delayed_tasks }}
</h2>

</div>


<div class="stat">

<h3>Pending</h3>

<h2>
{{ summary.pending_tasks }}
</h2>

</div>


<div class="stat">

<h3>Progress</h3>

<h2>
{{ summary.progress }}%
</h2>

</div>


<div class="stat">

<h3>Risk</h3>

<h2>
{{ summary.risk }}
</h2>

</div>


</div>


<!-- PROJECT STATUS -->

<div class="card">

<h2>

Project Status

</h2>

<p>

{{ summary.message }}

</p>

</div>


<!-- ADD TASK -->

<div class="card">

<h2>

Add New Task

</h2>


<form method="POST" action="/add">


<input

type="text"

name="name"

placeholder="Task name"

required

>


<select name="priority">


<option value="High">

High

</option>


<option value="Medium" selected>

Medium

</option>


<option value="Low">

Low

</option>


</select>


<input

type="date"

name="deadline"

>


<button type="submit">

Add Task

</button>


</form>

</div>


<!-- TASK TABLE -->

<div class="card">


<h2>

Tasks

</h2>


<table>


<tr>

<th>ID</th>

<th>Task</th>

<th>Priority</th>

<th>Deadline</th>

<th>Status</th>

<th>Action</th>

</tr>


{% for task in tasks %}


<tr>


<td>

{{ task.id }}

</td>


<td>

{{ task.name }}

</td>


<td>

{{ task.priority }}

</td>


<td>

{{ task.deadline }}

</td>


<td>

{{ task.status }}

</td>


<td>


<a href="/update/{{ task.id }}/completed">

Complete

</a>


<a href="/update/{{ task.id }}/delayed">

Delay

</a>


<a href="/update/{{ task.id }}/pending">

Pending

</a>


</td>


</tr>


{% endfor %}


</table>


</div>


<!-- ADAPTIVE PRIORITY -->

<div class="card">


<h2>

Adaptive Task Priority

</h2>


<ol>


{% for task in prioritized_tasks %}


<li>


<strong>

{{ task.name }}

</strong>


|

Priority:

{{ task.priority }}


|

Status:

{{ task.status }}


|

Score:

{{ task.score }}


</li>


{% endfor %}


</ol>


</div>


<!-- AI RECOMMENDATIONS -->

<div class="card">


<h2>

AI Recommendations

</h2>


<ul>


{% for recommendation in recommendations %}


<li>

{{ recommendation }}

</li>


{% endfor %}


</ul>


</div>


</div>


</body>


</html>

"""


# -----------------------------------------
# START FLASK SERVER
# -----------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )