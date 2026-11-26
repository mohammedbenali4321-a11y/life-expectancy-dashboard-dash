from dash import Dash, html, dcc, callback, Output, Input, dash_table

import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\moham\OneDrive\Desktop\Yassine\Pycharm\gapminder_unfiltered.csv")
app = Dash(__name__)

app.layout = [
    html.H1(
        children="My first dash",
        style={
            "textAlign": "center",
            "color": "green",
            "border": "2px solid red",
            "width": 300,
            "justifySelf": "center",
        },
    ),
    dcc.Dropdown(
        df["country"].unique(),
        "Canada",
        id="dropdown-selection",
        style={"width": 200},
    ),
    dcc.Graph(id="graph-content"),
]


@callback(
    Output("graph-content", "figure"),
    Input("dropdown-selection", "value"),
)
def update_graph(value):
    dff = df[df["country"] == value]
    return px.line(dff, x="year", y="lifeExp")


if __name__ == "__main__":
    app.run(debug=True)

dash_table.DataTable(df.to_dict('records'),
                     page_size=10,
                     columns =[{"name": col, "id": col} for col in df.columns],
                     filter_action = 'native'
                     )

# # code 2

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\moham\OneDrive\Desktop\Yassine\Pycharm\gapminder_unfiltered.csv")
app = Dash(__name__)

app.layout = [
    html.H1(
        children="My first dash",
        style={
            "textAlign": "center",
            "color": "green",
            "border": "2px solid red",
            "width": 300,
            "justifySelf": "center",
        },
    ),
    # # Mot "Evolution" juste au-dessus des deux cadres
    # html.Div(
    #     "Evolution",
    #     style={
    #         "textAlign": "center",
    #         "fontWeight": "bold",
    #         "marginBottom": "8px",
    #     },
    # ),
    # Cadre extérieur VERT
    html.Div(
        style={
            "border": "2px solid green",
            "padding": "10px",
        },
        children=[
            # Cadre intérieur ROUGE
            html.Div(
                style={
                    "border": "2px solid red",
                    "padding": "15px",
                },
                children=[
                    dcc.Dropdown(
                        df["country"].unique(),
                        "Canada",
                        id="dropdown-selection",
                        style={"width": 200, "margin": "0 auto 15px auto"},
                    ),
                    dcc.Graph(id="graph-content"),
                ],
            )
        ],
    ),
]


@callback(
    Output("graph-content", "figure"),
    Input("dropdown-selection", "value"),
)
def update_graph(value):
    dff = df[df["country"] == value]
    return px.line(dff, x="year", y="lifeExp")


if __name__ == "__main__":
    app.run(debug=True)


# # code 3

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\moham\OneDrive\Desktop\Yassine\Pycharm\gapminder_unfiltered.csv")
app = Dash(__name__)

app.layout = [
    html.H1(
        children="My first dash",
        style={
            "textAlign": "center",
            "color": "green",
            "border": "2px solid red",
            "width": 300,
            "justifySelf": "center",
        },
    ),
    # Cadre extérieur VERT
    html.Div(
        style={
            "border": "2px solid green",
            "padding": "10px",
        },
        children=[
            # Cadre intérieur ROUGE
            html.Div(
                style={
                    "border": "2px solid red",
                    "padding": "15px",
                },
                children=[
                    # Dropdown centré en haut
                    dcc.Dropdown(
                        df["country"].unique(),
                        "Canada",
                        id="dropdown-selection",
                        style={"width": "220px", "margin": "0 auto 15px auto"},
                    ),
                    # Ligne commune : courbe à gauche + tableau à droite
                    html.Div(
                        style={
                            "display": "flex",
                            "alignItems": "flex-start",
                            "gap": "20px",
                            "width": "100%",
                        },
                        children=[
                            # Colonne gauche : courbe
                            html.Div(
                                style={
                                    "flex": "1",
                                    "minWidth": "0",
                                },
                                children=[
                                    dcc.Graph(id="graph-content"),
                                ],
                            ),
                            # Colonne droite : tableau
                            html.Div(
                                style={
                                    "flex": "1",
                                    "minWidth": "0",
                                    "overflowX": "auto",
                                },
                                children=[
                                    dash_table.DataTable(
                                        data=df.to_dict("records"),
                                        page_size=10,
                                        columns=[{"name": col, "id": col} for col in df.columns],
                                        filter_action="native",
                                        sort_action="native",
                                        style_table={
                                            "width": "100%",
                                            "overflowX": "auto",
                                        },
                                        style_header={
                                            "textAlign": "center",
                                            "fontWeight": "bold",
                                        },
                                        style_cell={
                                            "textAlign": "center",
                                            "padding": "6px",
                                        },
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    ),
]


@callback(
    Output("graph-content", "figure"),
    Input("dropdown-selection", "value"),
)
def update_graph(value):
    dff = df[df["country"] == value]
    return px.line(dff, x="year", y="lifeExp")


if __name__ == "__main__":
    app.run(debug=True)