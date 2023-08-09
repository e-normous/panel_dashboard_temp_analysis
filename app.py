import panel as pn
import pandas as pd
import datetime

from visualization import create_line_chart


# the path to the e-normous logo (not in the repo due to it being in the gitignore)
logo_enormous = "assets\logo_e-normous.png"
enormous_pane = pn.pane.Image(logo_enormous, alt_text="Logo e-normous", link_url="https://e-normous.net", width=250)

# get today's date
today = datetime.datetime.today().strftime("%Y-%m-%d")
today_localized = datetime.datetime.today().strftime("%d.%m.%Y")

# preparing this for the panel app
pane_date = pn.pane.Markdown(f"# Heute ist der {today_localized}")


# we have values for time, temperature and humidity (german words are used here:
# "Zeit", "Temperatur" and "Luftfeuchtigkeit")
df = pd.read_csv("temp_hum.csv")

last_temp = df["Temperatur"].iloc[-1]
last_measurement = df["Zeit"].iloc[-1]

# transforming the time column to a datetime object and extracting only the Y, m and d from it (no time)
df["Zeit"] = pd.to_datetime(df["Zeit"])
df["Tag"] = df["Zeit"].dt.strftime("%Y-%m-%d")

# checking whether we have all the columns specified as we need them
print(df.info())

# creating a chart for the specific day (today)
# therefore, we first of all filter out all the values we have for today
df_today = df.loc[df["Tag"] == today]
print(df_today.head())
line_chart_temp_today = create_line_chart(df_today, "Zeit", "Temperatur", "Temperatur (in °C) im Tagesverlauf")

# preparing the line chart for the panel app
pane_line_chart_temp_today = pn.pane.Plotly(line_chart_temp_today)

# creating an alternative df where we have the mean temp value for each day
mean_temp_df = df.groupby(["Tag"], as_index=False).mean()
mean_temp_df[["Temperatur", "Luftfeuchtigkeit"]] = mean_temp_df[["Temperatur", "Luftfeuchtigkeit"]].round(2)
pane_daily_temp_df = pn.pane.DataFrame(mean_temp_df[["Tag", "Temperatur", "Luftfeuchtigkeit"]], index=False)

line_chart_temp_daily_mean = create_line_chart(mean_temp_df, "Tag", "Temperatur", "Durchschnitts-Temperatur pro Tag")

#preparing the line chart for the panel app
pane_line_chart_temp_daily_mean = pn.pane.Plotly(line_chart_temp_daily_mean)

first_page = pn.Column(enormous_pane,
          pane_date,
          pn.pane.Markdown(f"### Letzte Messung ({last_measurement}): {last_temp.round(2)}°C"),
          pane_line_chart_temp_today,
          pane_line_chart_temp_daily_mean,
          pn.pane.Markdown("### Tägliche Durchschnittswerte"),
          pane_daily_temp_df
          )

first_page.servable()
first_page.save("mvp.html")

