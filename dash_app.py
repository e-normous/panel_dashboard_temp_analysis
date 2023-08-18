import pandas as pd
import datetime
from dash import Dash, html, dcc, dash_table

from visualization import create_line_chart

app = Dash(__name__)
app.title = "Dashboard Temperaturanalyse"

# the path to the e-normous logo (not in the repo due to it being in the gitignore)
logo_enormous = "assets\logo_e-normous.png"

# get today's date
today = datetime.datetime.today().strftime("%Y-%m-%d")
today_localized = datetime.datetime.today().strftime("%d.%m.%Y")

# we have values for time, temperature and humidity (german words are used here:
# "Zeit", "Temperatur" and "Luftfeuchtigkeit")
df = pd.read_csv("temp_hum.csv")

last_temp = df["Temperatur"].iloc[-1]
last_measurement = df["Zeit"].iloc[-1]

# transforming the time column to a datetime object and extracting only the Y, m and d from it (no time)
df["Zeit"] = pd.to_datetime(df["Zeit"])
df["Tag"] = df["Zeit"].dt.strftime("%Y-%m-%d")

# checking whether we have all the columns specified as we need them
#print(df.info())

# creating a chart for the specific day (today)
# therefore, we first of all filter out all the values we have for today
df_today = df.loc[df["Tag"] == today]

line_chart_temp_today = create_line_chart(df_today, "Zeit", "Temperatur", "Temperatur (in °C) im Tagesverlauf")


# creating an alternative df where we have the mean temp value for each day
mean_temp_df = df.groupby(["Tag"], as_index=False).mean()
mean_temp_df[["Temperatur", "Luftfeuchtigkeit"]] = mean_temp_df[["Temperatur", "Luftfeuchtigkeit"]].round(2)

# plotting the line chart for the daily means
line_chart_temp_daily_mean = create_line_chart(mean_temp_df, "Tag", "Temperatur", "Durchschnitts-Temperatur pro Tag")





#----------------THE APP LAYOUT----------------
app.layout = html.Div(style={"margin-left": "25px", "margin-right": "25px"},
    children=[
    html.A(href="https://www.e-normous.net", target="_blank", children=[
    html.Img(src=logo_enormous, alt="Logo e-normous", height=100)]),
    html.H1(children=f"Heute ist der {today_localized}"),
    #html.Br(),
    html.H4(children=f"Letzte Messung ({last_measurement}): {last_temp.round(2)}°C"),
    dcc.Graph(figure=line_chart_temp_today),
    dcc.Graph(figure=line_chart_temp_daily_mean),
    html.H4(children="Messtabelle:"),
    dash_table.DataTable(mean_temp_df.to_dict("records"), columns=[{"name": i, "id": i} for i in mean_temp_df[["Tag", "Temperatur", "Luftfeuchtigkeit"]]]) #[{"name": i, "id": i} for i in mean_temp_df.columns])
])







# run the app
if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.7")

