
from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc

import calculate
from data import config

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
        Output("goals-card", "style", allow_duplicate=True),
        [Input("goals-card-visibility", "data"),
         Input("goals-data-store", "data")],
        prevent_initial_call=True
    )
    def update_card_display(is_visible, data):
        # Ziele berechnen
        result = calculate.calculate_goals_probabilities(data["goals"], data["probabilities"])
        calculate.calculate_overall_success(data["probabilities"])

        # Inhalte (z. B. Tabelle)
        children = dbc.CardBody([
            dbc.Table.from_dataframe(result, striped=True, bordered=True, hover=True)
        ])

        # Sichtbarkeitsstil setzen
        style = {
            "position": "fixed",
            "top": "80px",
            "right": "10px",
            "width": "400px",
            "padding": "10px",
            "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "zIndex": 1000,
            "display": "block" if is_visible else "none"
        }

        return children, style

    # Simulation Callback für Meilensteine
    @app.callback(
        [
            Output("milestone-store", "data", allow_duplicate=True),
        Output("kpi-store", "data", allow_duplicate=True),
        Output("csf-store", "data", allow_duplicate=True),
        ],
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
        # -------------------Meilensteine und Slider-Werte aus den Inputs extrahieren-----------------------
        num_iterations = len(config.iteration_milestone)
        num_sliders = len(config.kpi_data)
        # Extraction from GUI
        milestones_achieved = inputs[:num_iterations]  # Erste Inputs sind Meilenstein-Werte
        slider_values = inputs[num_iterations:num_iterations + num_sliders]  # Danach kommen die Slider-Werte

        # Calculation Milestones
        calculate.calculate_milestones_achieved(milestones_achieved)

        # Aktualisiere Slider-Werte in config.kpi_data
        slider_keys = list(config.kpi_data.keys())
        for key, value in zip(slider_keys, slider_values):
            config.kpi_data[key] = value

        # Rückgabe des aktualisierten Goals-Card-Inhalts
        return()
