import pandas as pd
input_data = {'date': ["01/01/81", "02/01/81", "03/01/81", "04/01/81", "05/01/81", "06/01/81", "07/01/81", "08/01/81"],

                    'precip_cm': [0.00, 0.10, 0.00, 0.00, 0.00, 0.10, 0.00, 0.00],
                    'pevp_cm': [0.30, 0.21, 0.28, 0.28, 0.31, 0.01, 0.28, 0.28],
                    'temp_celsius': [9.5, 6.3, 3.5, 5, 9.5, 6.3, 3.5, 5],
                    'ws10_cm_s': [501.6, 368.0, 488.3, 404.5, 501.6, 368.0, 488.3, 404.5],
                    'solr_lang': [240.3, 244.3, 303.0, 288.5, 240.3, 244.3, 303.0, 288.5]}

input_data = pd.DataFrame(input_data)

import altair as alt


def plot_density(var):
    fig = alt.Chart(
    input_data
    ).transform_density(
    var,
    as_=[var, 'density'],
    ).mark_area().encode(
    x= var + ":Q",
    y='density:Q',
    )
    return fig