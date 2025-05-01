"""
This file contains the layout and callbacks for the goals display.

The layout consists of a card that displays the overall success rate and a table with the goals and their probabilities.

The callbacks update the goals probabilities based on the user input.

Functions:
- get_goals_card_body: Returns the card layout with the goals and probabilities.
- register_goals_display_callbacks: Registers the callbacks for the goals display.
"""

from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc

import calculate
import data
from data import config

is_shown = False

def get_goals_card_body():
    # Tabellarische Daten
    data = calculate.calculate_goals_probabilities()
    calculate.calculate_overall_success()

    # Layout
    return dbc.Card([
                dbc.CardBody([
                        dbc.Table.from_dataframe(data, striped=True, bordered=True, hover=True),
                ])
            ], id="goals-card",
        style={
            "position": "fixed",
            "top": "80px",
            "right": "10px",
            "width": "400px",
            "padding": "10px",
            "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "zIndex": 1000,
            "display": "none"
        }
    )
def register_goals_display_callbacks(app):
    @app.callback(
        Output("goals-card-visibility", "data"),
        Input("toggle-collapse-goals", "n_clicks"),
        State("goals-card-visibility", "data"),
        prevent_initial_call=True
    )
    def toggle_visibility(n_clicks, current_state):
        return not current_state

    @app.callback(
        Output("goals-card", "children", allow_duplicate=True),
        Input("goals-card-visibility", "data"),
        prevent_initial_call=True
    )
    def update_card_display(is_visible):
        return [get_goals_card_body()]

    # Simulation Callback für Meilensteine
    @app.callback(
        [Output("goals-card", "children", allow_duplicate=True)],
        [
            Input(f"milestones-checklist-{index}", "value")
            for index in range(len(config.iteration_milestone))
        ]+
        [
            Input(f"{key.replace(' ', '-').lower()}-slider", "value")
            for key in config.kpi_data.keys()
        ]+
        [
            Input(f"csf-input-{index}", "value") for index in range(len(config.csf_data))
        ],
        prevent_initial_call=True
    )
    def update_simulation(*inputs):
        # Meilensteine und Slider-Werte aus den Inputs extrahieren
        num_iterations = len(config.iteration_milestone)
        num_sliders = len(config.kpi_data)
        milestones_achieved = inputs[:num_iterations]  # Erste Inputs sind Meilenstein-Werte
        slider_values = inputs[num_iterations:num_iterations + num_sliders]  # Danach kommen die Slider-Werte

        # Aktualisiere die Meilenstein-Konfiguration
        calculate.calculate_milestones_achieved(milestones_achieved)

        # Aktualisiere Slider-Werte in config.kpi_data
        slider_keys = list(config.kpi_data.keys())
        for key, value in zip(slider_keys, slider_values):
            config.kpi_data[key] = value

        # Rückgabe des aktualisierten Goals-Card-Inhalts
        return [get_goals_card_body()]
