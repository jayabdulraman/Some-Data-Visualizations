"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    nested_dict = {}
    with open(filename, 'r', newline='') as csv_dict:
        csv_writer = csv.DictReader(csv_dict,  delimiter=separator, quotechar=quote)
        for row in csv_writer:
            col = row[keyfield]
            nested_dict[col] = row
    return nested_dict


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    table = []
    gdpdat_v2 = {}
    for key, value in gdpdata.items():
        try:
            gdpdat_v2[int(key)] = float(value)
        except ValueError:
            pass

    min_max = [year for year in range(gdpinfo['min_year'], gdpinfo['max_year'] + 1)]

    for key in min_max:
        if key in gdpdat_v2:
            table.append((key, gdpdat_v2[key]))
    return table


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    read = read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_name'],
                                   gdpinfo['separator'], gdpinfo['quote'])
    country_name = [name for name in read]
    plot_dict = {}
    for country in country_list:
        # if country in country_name:
        try:
            plot_dict[country] = build_plot_values(gdpinfo, read[country])
        except KeyError:
            plot_dict[country] = []

    return plot_dict


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    read = read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_name'],
                                   gdpinfo['separator'], gdpinfo['quote'])

    plot_dict = build_plot_dict(gdpinfo, country_list)
    # values = build_plot_values(gdpinfo, plot_dict)
    country_name = [name for name in read]
    # Plot to XY data on svg file
    xy_chart = pygal.XY()
    xy_chart.title = 'Gross Domestic Product Data for Countries 1960 - 2015'
    xy_chart.y_title = 'GDP in current US dollars'
    for name in plot_dict:
        if name in country_list:
            xy_chart.add(name, plot_dict.get(name))
    else:
        xy_chart.add(None, None)

    xy_chart.render_to_file(plot_file)


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # return render_xy_plot(gdpinfo, [], "isp_gdp_xy_no_data.svg")
    # render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["Sierra Leone", "Guinea", "Liberia"],
                   "isp_gdp_xy_sl+gn+li.svg")
    # return read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_name'],
    #                                 gdpinfo['separator'], gdpinfo['quote'])

    # gdp_data = {'2000': '1', '2001': '2', '2002': '3', '2003': '4', '2004': '5', '2005': '6', '2006': ''}
    
    # value = build_plot_values(gdpinfo, gdp_data)
    # return value
    # country = ['Country1']
    # value = build_plot_dict(gdpinfo, country)
    # return value

# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.


test_render_xy_plot()
