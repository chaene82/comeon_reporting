# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import sqlalchemy
import plotly.express as px

db_name = "test.db"
table_name = "eth_node_stats"

# Incorporate data
engine = sqlalchemy.create_engine("sqlite:///%s" % db_name, execution_options={"sqlite_raw_colnames": True})
df = pd.read_sql_table(table_name, engine)

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data and a Graph'),
   # dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='timestamp', y='performancetoday', histfunc='sum'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)