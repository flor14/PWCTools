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