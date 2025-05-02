"""
This file contains the Config class which is used to store the data from the params.json file.

The Config class is used to store the data from the params.json file. It contains the roadmap data,
iteration milestones, KPIs, CSFs, goals, team members, goal probabilities list, milestones achieved, success rate,
milestone multiplicator, goals multiplicator, and team multiplicator.
"""

import pandas as pd
import json

class Config:
    def __init__(self):
        with open('params.json', 'r') as file:
            data = json.load(file)

        self.roadmap_data = pd.DataFrame(data['iterations'])
        self.roadmap_data["Start"] = pd.to_datetime(self.roadmap_data["Start"])
        self.roadmap_data["End"] = pd.to_datetime(self.roadmap_data["End"])

        self.iteration_milestone = [
            {
                "iteration": row["Iteration"],
                "milestones": row["Milestones"]
            }
            for _, row in self.roadmap_data.iterrows()
        ]

        self.kpi_data = data['kpis']
        self.csf_data = data['csfs']
        self.goals = data['goals']
        self.team_members = data['team_members']
        self.goal_probabilities_list = init_goal_probabilities_list(self.goals)
        self.milestones_achieved = []

        self.success_rate = 0
        self.milestone_multiplicator = 0
        self.goals_multiplicator = 0.4
        self.team_multiplicator = 0.2
    def get_success_rate(self):
        return round((self.success_rate + self.milestone_multiplicator + self.goals_multiplicator + self.team_multiplicator)*100,2)

def init_goal_probabilities_list(goals):
    goal_probabilities_list = []
    for goal in goals:
            goal_probabilities_list.append(
                {
                    "Goal": goal["Description"],
                    "Probability": 0.22  # Placeholder
                }
            )
    return goal_probabilities_list

# Initialize the config object for first state
config = Config()

def load_initial_data():
    return {
        "milestone-store": config.iteration_milestone,
        "kpi-store": config.kpi_data,
        "csf-store": config.csf_data,
        "goals-data-store": {"goals":config.goals, "probabilities": config.goal_probabilities_list},
        "team-store": config.team_members,
    }
