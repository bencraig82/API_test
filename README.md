# API_test
This repository was created for the TE Assignment.  

This project is designed to run with Python 3.8

Packages required for this project are contained in `requirements.txt`.  
To install the required python packages, run:  
`pip install -r requirements.txt`

The test is contained in:  
`tests/test_api.py`  

To run the test, execute the following from the root folder:  
`pytest tests/test_api.py`

To display logging, add the following option:  
`pytest tests/test_api.py --log-cli-level info`

This test requires a working internet connection to retrieve the API data from the url.
To run the test offline using local copy of the API data, use the `--mock` option, i.e.  
`pytest tests/test_api.py --mock`
