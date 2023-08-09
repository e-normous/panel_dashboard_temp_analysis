import plotly.express as px

from color_scheme import colors

# in order to get a nice visualization, we need to do the following steps
# - filter / group the df for each day
# - create a median (or mean) value for each day for the temperature
# - display them in a line chart

def create_line_chart(df, x_axis_values, y_axis_values, title):
    """_summary_

        Args:
            df (pandas dataframe): the dataframe containing the needed information and values
            x_axis_values (str): a string indicating the exact column to use for the x axis values
            y_axis_values (str): a string indicating the exact column to use for the y axis values
            title (str): a string containing the exact title to use for the chart

        Returns:
            Plotly graph_objs Figure: Returning a plotly figure (line chart)
    """
    fig = px.line(df,
            x=x_axis_values,
            y=y_axis_values,
            text=y_axis_values,
            template="simple_white",
            title=title,
            width=1200,
            height=800
            )
    
    fig.update_traces(textposition="bottom right", line_color=colors["e-normous main blue"])
    return fig
