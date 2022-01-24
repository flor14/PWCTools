from src.pwctools.pwctools import PWC_fg, PWC_years, PWC_complete, PWC_save
import pandas as pd
from pandas._testing import assert_frame_equal
import filecmp
import pytest

def test_PWC_fg():
    """Test that the initial dataset is subseted and rearranged"""
    test_data = pd.read_csv("tests/data.csv")
    test_data_pwc_fg = pd.read_csv("tests/data_pwc_fg.csv")
    result = PWC_fg(data = test_data,
       date = "date", 
       start = "02/01/81",
       end = "03/01/81" ,
       format_date = "%d/%m/%y",
       temp_celsius = 'temp_celsius',
       precip_cm = 'precip_cm' , 
       ws10_cm_s = 'ws10_cm_s',
       pevp_cm = 'pevp_cm',
       solr_lang = 'solr_lang')
    assert_frame_equal(result, test_data_pwc_fg)

def test_PWC_years():
    test_data_pwc_fg = pd.read_csv("tests/data_pwc_fg.csv")
    result = PWC_years(pwc_data = test_data_pwc_fg)
    assert_frame_equal(result, test_data_pwc_fg)

def test_PWC_complete():
    test_data_pwc_years = pd.read_csv("tests/data_pwc_years.csv")
    result = PWC_complete(pwc_data = test_data_pwc_years)
    assert_frame_equal(result, test_data_pwc_years)

def test_pwc_save():
    test_data_pwc_complete = pd.read_csv("tests/data_pwc_complete.csv")
    PWC_save(pwc_data = test_data_pwc_complete, save_in ="test.dvf" )
    filecmp.cmp('wf.dvf', 'test.dvf')
    
def test_PWC_fg_warning():
    with pytest.raises(TypeError):
        data = 2
        PWC_fg(data = data,
        date = "date", 
        start = "02/01/81",
        end = "03/01/81" ,
        format_date = "%d/%m/%y",
        temp_celsius = 'temp_celsius',
        precip_cm = 'precip_cm' , 
        ws10_cm_s = 'ws10_cm_s',
        pevp_cm = 'pevp_cm',
        solr_lang = 'solr_lang')
