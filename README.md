# PWCTools

The goal of the function `PWC_fg()` is to convert a weather dataset to the input file format needed to run the models Pesticide in Water Calculator (PWC) v1.52 and Pesticide Root Zone Model (PRZM5) v5.02.

PWC and PRZM5 are mathematical models used for pesticide fate modelling and are free to download from the [USEPA website](https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/models-pesticide-risk-assessment).  These models are applied for regulatory purposes as part of surface water exposure characterization during pesticide risk assessment.

Although PWC has a simple and intuitive interface, the weather files required to run the model are only available for North America, making it difficult for users lacking programming skills to run the model in other countries.  The package `PWCfilegenerator` facilitates the construction of weather files in PWC format from common databases.

# Installation

```bash
$ pip install PWCTools
```
# Usage

```python
import pandas as pd

input_data = {'date': ["01/01/81", "02/01/81", "03/01/81", "04/01/81"],

                    'precip_cm': [0.00, 0.10, 0.00, 0.00],
                    'pevp_cm': [0.30, 0.21, 0.28, 0.28],
                    'temp_celsius': [9.5, 6.3, 3.5, 5],
                    'ws10_cm_s': [501.6, 368.0, 488.3, 404.5],
                    'solr_lang': [240.3, 244.3, 303.0, 288.5]}

input_data = pd.DataFrame(input_data)



PWC_fg(data = input_data,
       date = "date", 
       start = "02/01/81",
       end = "03/01/81" ,
       format_date = "%d/%m/%y",
       temp_celsius = 'temp_celsius',
       precip_cm = 'precip_cm' , 
       ws10_cm_s = 'ws10_cm_s',
       pevp_cm = 'pevp_cm',
       solr_lang = 'solr_lang')

PWC_years(pwc_data = pwc_data)
PWC_complete(pwc_data = pwc_data)
PWC_save(pwc_data = pwc_data,
         save_in ="wf.dvf" )

```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`PWCTools` was created by Florencia D'Andrea. It is licensed under the terms of the GNU General Public License v3.0 license.

## Credits

`PWCTools` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
