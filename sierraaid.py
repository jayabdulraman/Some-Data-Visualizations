import csv
import pygal
from datetime import datetime

# Get dates and high temperatures from file.
filename = "List of Sierra Foreign Aid Projects.csv.csv"

# Get dates, high, and low temperatures from file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows, names = [], [], [], []
    for row in reader:
        try:
            name = row[0]
            current_date = datetime.strptime(row[2], "%Y").date()
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            # Get the maximum temperature row
            highs.append(high)
            # Get the minimum temperature row
            lows.append(low)
            names.append(name)


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 18
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1200

# Plot data.
line_chart = pygal.Bar(my_config)
line_chart.title = "Foreign Aid poured into Sierra Leone for the last decade"
# line_chart.title(title, fontsize=20)
line_chart.x_labels = names
# line_chart.y_labels = highs

# plt.show()
line_chart.add('Aid Received($)', highs)
line_chart.add('Aid Remain($)', lows)
line_chart.render_to_file('sierraaid.svg')
