# KPI-Based Success Rate Simulator

This project provides a comprehensive dashboard to model, visualize, and analyze the success rate of goals based on Key Performance Indicators (KPIs), Critical Success Factors (CSFs), milestones, and team impact. The application is developed using **Dash**, **Plotly**, **Dash Bootstrap Components**, and **Python**.

- Wie soll berechnung funktionieren
- Welche Faktoren sind wichtig? (KPis, CSFs, milestones, team impact)
- Beeinflusst KPIs die CSFs? 
- Was beeinflusst was

## Features

- **KPI and CSF-Based Goal Success Calculation**:
  - Each goal specifies KPIs and CSFs with respective weights, where the sum of weights equals 1.
  - Example goal configuration:
    ```json
    {
      "Description": "Seamlessly integrate CoPilot into the team’s workflows.",
      "Factors": [
        { "Name": "Employee Acceptance", "Weight": 0.5 },
        { "Name": "Code Quality", "Weight": 0.3 },
        { "Name": "Data Privacy", "Weight": 0.2 }
      ]
    }
    ```

- **Success Rate Composition**:
  - Overall success rate is derived from:
    - **40%**: Goals rate (calculated using KPI-CSF weights, where CSFs and KPIs can be dynamically adjusted through user inputs to reflect specific scenarios).
    - **40%**: Achieved milestones.
    - **20%**: Team impact (low sensitivity; multiple configurations needed to observe noticeable changes).

- **Interactive Milestone Tracking**:
  - Milestones are evenly weighted and can be toggled to simulate progress.

- **Roadmap Visualization**:
  - Visual interface to modify iteration dates.
  - Potential future expansion to consider iteration lengths in success calculations.

- **User-Friendly Design**:
  - Developed with intuitive components for seamless interaction.

## Application

This project aligns with the **GenAI in Software Engineering** innovation case study, focusing on simulating the introduction and implementation of GitHub CoPilot in a software development department. The tool:
- Models critical success factors and team dynamics.
- Provides visual insights into the roadmap and milestones for implementation.
- Empowers decision-makers with data-driven predictions.

## Technology Stack

- **Python**: Core language.
- **Dash**: Framework for building the interactive web application.
- **Plotly**: For creating advanced visualizations.
- **Dash Bootstrap Components**: Enhancing the UI/UX design.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Clara1a2/GenAI-in-Software-Engineering.git
   cd GenAI-in-Software-Engineering
    ```
2. Create and activate a virtual environment:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
3. Install the required dependencies:
   ```bash
   pip install dash pandas dash_bootstrap_components
   ```
4. Run the app:
    ```bash
    python app.py
    ```


#### If you want to change the styling of the app, change the `dbc.themes.BOOTSTRAP` line in `app.py` to any of the following:

- [x] dbc.themes.BOOTSTRAP
- [x] dbc.themes.CERULEAN
- [x] dbc.themes.COSMO
- [x] dbc.themes.CYBORG
- [x] dbc.themes.DARKLY
- [x] dbc.themes.FLATLY
- [x] dbc.themes.JOURNAL
- [x] dbc.themes.LITERA
- [x] dbc.themes.LUMEN
- [x] dbc.themes.LUX
- [x] dbc.themes.MATERIA
- [x] dbc.themes.MINTY
- [x] dbc.themes.MORPH
- [x] dbc.themes.PULSE
- [x] dbc.themes.QUARTZ
- [x] dbc.themes.SANDSTONE
- [x] dbc.themes.SIMPLEX
