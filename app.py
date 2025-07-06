import dash
from dash import html
import os

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    style={"textAlign": "center", "padding": "50px"},
    children=[
        html.H1("📊 Options Strategy Assistant", style={"color": "#2c3e50"}),
        html.P("✅ Deployed successfully on Render!", style={"fontSize": "20px"})
    ]
)

# Main entry point
if __name__ == "__main__":
    # Use the PORT provided by Render, or default to 8050 for local testing
    port = int(os.environ.get("PORT", 8050))
    # Run the Dash server on 0.0.0.0 to accept external traffic
    app.run(host="0.0.0.0", port=port)
