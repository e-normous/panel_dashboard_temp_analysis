import plotly.express as px

# in order to get a nice visualization, we need to do the following steps
# - filter / group the df for each day
# - create a median (or mean) value for each day for the temperature
# - display them in a line chart

def create_line_chart(df, x_axis_values, y_axis_values, title):
    fig = px.line(df,
            x=x_axis_values,
            y=y_axis_values,
            text=y_axis_values,
            template="simple_white",
            title=title,
            width=1200,
            height=800)
    
    fig.update_traces(textposition="bottom right")
    
    return fig
