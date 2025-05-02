"""
This file contains the layout and callbacks for the CSF inputs.

The layout consists of an input group with a text input for each CSF metric.

The callbacks update the current values of the CSF metrics and recalculate the goals probabilities.

Functions:
- get_inputs: Returns the input group for the CSF metrics
- register_csf_inputs_callbacks: Registers the callbacks for the CSF inputs
"""

from data import config
from calculate import calculate_goals_probabilities

from dash import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd

def inputs_helper():
    inputs = []
    for index, csf in enumerate(config.csf_data):
        # Nur die zwei Zeilen
        inputs.append(
            dbc.Col([
        dbc.FormText(csf["Metric"]),
        dbc.Input(value= csf["Current"], type="number", id=f"csf-input-{index}", max=100, min=0, step=1),
        ], width="auto", className="mx-1")
        )
    return inputs

def get_inputs():
    return dbc.InputGroup(
                inputs_helper(),
                className="mb-3")

#ToDO : Update Input based on Store not config
def register_csf_inputs_callbacks(app):
    @app.callback(
        Output("csf-store", "data"),
        [Input(f"csf-input-{index}", "value") for index in range(len(config.csf_data))],
        prevent_initial_call=True
    )
    def update_csf_store(*csf_values):
        # Optional: Werte in Dict mit Namen, falls du die brauchst
        csf_keys = [item["Metric"] for item in config.csf_data]
        return [dict(Metric=key, Current=value,
                     Target=next((x["Target"] for x in config.csf_data if x["Metric"] == key), None))
                for key, value in zip(csf_keys, csf_values)]

    @app.callback(
        [Output("csf-bar-chart", "figure")],
        [Input("csf-store", "data")],
        prevent_initial_call=True)
    def save_csf_inputs(*values):
        for index, value in enumerate(values):
            #print(f"csf-input-{index}: {value}")
            config.csf_data[index]["Current"] = value
        calculate_goals_probabilities()
        fig = px.bar(
                    pd.DataFrame(config.csf_data),
                    x="Metric", y="Current",
                    title="Current vs. Target CSF",
                    color_discrete_sequence=["#636EFA"]
                ).add_bar(
                    x=pd.DataFrame(config.csf_data)["Metric"],
                    y=pd.DataFrame(config.csf_data)["Target"],
                    name="Target",
                    marker_color="#EF553B"
                ).update_layout(
                    barmode="group",
                    yaxis_title="Percentage",
                    xaxis_title="CSF"
                )
        return [fig]