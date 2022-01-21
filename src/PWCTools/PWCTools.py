import pandas as pd
import numpy as np

def PWC_fg(data, date, start, end, format_date, temp_celsius, precip_cm, ws10_cm_s, pevp_cm, solr_lang):
    """Subset the initial dataset and rearrange the columns"""
    if not isinstance(data, pd.DataFrame):  
        raise TypeError("'word_counts' should be of type 'Counter'.")
    # Convert to dates
    data.date = pd.to_datetime(data[date], format = format_date)

    # Subset the dataframe in the period selected by the user
    data[(data.date >= pd.to_datetime(start, format = format_date)) & (data.date <= pd.to_datetime(end, format = format_date))]

    # Split dates in days, months and years
    data['day'] = pd.DatetimeIndex(data[date]).day
    data['month'] = pd.DatetimeIndex(data[date]).month
    data['year'] = pd.DatetimeIndex(data[date]).year


    # Reorder the dataframe in the way it is read by PWC
    pwc_data = {
        'empty': " ",
        'X1': data['day'],
        'X2': data['month'],
        'X3': data['year'],
        'precip_cm': data[precip_cm],
        'pevp_cm':  data[pevp_cm],
        'temp_celsius': data[temp_celsius],
        'ws10_cm_s':  data[ws10_cm_s],
        'solr_lang':  data[solr_lang]
       }

    pwc_data = pd.DataFrame(pwc_data)
    return pwc_data

    
def PWC_years(pwc_data):    
    """Reemplace the years starting in 1961"""    # Override years starting in 1961
    index = pwc_data.index
    number_of_rows = len(index)
    pwc_data['X3'] = pd.date_range(start = pd.to_datetime("01/01/61", format = "%d/%m/%y"), periods = number_of_rows)
    pwc_data['X3'] = pwc_data.X3.dt.strftime('%y')
    pwc_data['X3'] = pwc_data['X3'].astype(int)
    return pwc_data


def PWC_complete(pwc_data):
    """Handle missing values and round numbers"""
    # Replace missing values
    pwc_data['precip_cm'] = pwc_data['precip_cm'].fillna(0)
    pwc_data['pevp_cm'] = pwc_data['pevp_cm'].fillna(pwc_data['pevp_cm'].mean())
    pwc_data['temp_celsius'] = pwc_data['temp_celsius'].fillna(pwc_data['temp_celsius'].mean())
    pwc_data['ws10_cm_s'] = pwc_data['ws10_cm_s'].fillna(pwc_data['ws10_cm_s'].mean())
    pwc_data['solr_lang'] = pwc_data['solr_lang'].fillna(pwc_data['solr_lang'].mean())

    # Round numbers
    pwc_data['precip_cm'] = pwc_data['precip_cm'].round(2)
    pwc_data['pevp_cm'] = pwc_data['pevp_cm'].round(2)
    pwc_data['temp_celsius'] = pwc_data['temp_celsius'].round(1)
    pwc_data['ws10_cm_s'] = pwc_data['ws10_cm_s'].round(1)
    pwc_data['solr_lang'] = pwc_data['solr_lang'].round(1)
    return pwc_data

# pwc_data['X1'].apply(lambda x: '{0:0>2}'.format(x))
# pwc_data['X2'].apply(lambda x: '{0:0>2}'.format(x))

def PWC_save(pwc_data, save_in):
    """
    Save final in FORTRAN format 1X,3I2,5F10.0
    Extension .dvf
    """
    # FORTRAN format 1X,3I2,5F10.0
    ofile = save_in
    #w tells python we are opening the file to write into it
    fmt = "%s %02d %02d %02d %10.1f %10.1f %10.1f %10.1f %10.1f"
    np.savetxt(ofile, pwc_data.values, fmt=fmt)
 