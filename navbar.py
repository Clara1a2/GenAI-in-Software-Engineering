from dash import html, dcc
import dash_bootstrap_components as dbc

from modal import get_modal

def get_navbar(success_rate=31.0, status="Needs Improvement"):
    return dbc.Navbar(
        dbc.Container([
            dcc.Store(id="goals-card-visibility", data=False),
            # App Title
            dbc.NavbarBrand("GitHub Copilot Implementation Simulator", style={"fontWeight": "bold"}),

            # Links statt Buttons (mittig)
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Configure Team Members", href="#", id="open-modal-link", className="me-3")),
                get_modal(),
                dbc.NavItem(dbc.NavLink("README", href="#", id="readme-link", className="me-3")),
                dbc.DropdownMenu(
                    label="Config Options",
                    nav=True,
                    in_navbar=True,
                    children=[
                        dbc.DropdownMenuItem("Load Base Config", id="load-base-config"),
                        dbc.DropdownMenuItem("Load Best Config", id="load-best-config"),
                        dcc.Upload(
                            id='upload-data',
                            children=dbc.DropdownMenuItem("Upload config.json", style={"cursor": "pointer"}),
                            multiple=False
                        ),
                    ],
                    className="me-3"
                ),
            ], className="me-auto", navbar=True, pills=True),

            # Rechts: Erfolgskomponente
            dbc.Nav([
                html.Div([
                    html.Small(f"Success Rate: {success_rate:.1f}%", style={"fontWeight": "bold"}),
                    dbc.Progress(value=success_rate, color="info", striped=True, animated=True, style={"height": "15px", "width": "150px"}),
                    html.Small(f"Status: {status}", style={"fontSize": "0.75rem"})
                ], style={"textAlign": "right", "marginRight": "15px"}),

                # Optional: Button zum Ein-/Ausklappen von Details
                dbc.Button("Details", id="toggle-collapse-goals", color="primary", size="sm", n_clicks=0)
            ], className="ms-auto", style={"alignItems": "center"})
        ]),
        sticky="top",
        className="mb-4",
        color="primary",
    )
