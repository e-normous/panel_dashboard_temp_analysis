import panel as pn
import pandas as pd
import datetime

# get today's date
today = datetime.datetime.today().strftime("%d.%m.%Y")

date_pane = pn.pane.Markdown(f"### Heute ist der {today}")
date_pane.servable()


