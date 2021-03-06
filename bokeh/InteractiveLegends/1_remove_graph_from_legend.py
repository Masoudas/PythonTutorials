"""
Sometimes it is desirable to be able to hide glyphs by clicking on an entry in a Legend. In Bokeh this can be accomplished by setting the legend click_policy property to "hide" as shown in the example below.

Me: The whole catch is to add a click policy, which is simply:
p.legend.click_policy="hide"
and that's it.
"""
import pandas as pd

from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

p = figure(width=1600, height=500, x_axis_type="datetime")
p.title.text = 'Click on legend entries to hide the corresponding lines'

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(df['date'], df['close'], line_width=2,
           color=color, alpha=0.8, legend_label=name)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

output_file("interactive_legend.html", title="interactive_legend.py example")

show(p)
