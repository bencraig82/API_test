import pytest
import requests
from pprint import pformat
from logging import info, error
import json

mock_file_path = 'data/mock_api_response.json'
URL = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'


@pytest.fixture(scope="session")
def mock(pytestconfig):
    return pytestconfig.getoption("mock")


def test_api(mock):
    """
    Test to verify specific fields within the API return from the provided URL
    :param mock (bool): True if '--mock' option is passed at runtime. Uses a
        local mock copy of the API response to test with.
    :return: none
    """
    try:
        response = requests.get(URL)
        resp_dict = response.json()
    except requests.exceptions.ConnectionError as e:
        error(f"Unable to make a connection to the API. \n"
              f"Run test locally with mock data by using --mock option.\n"
              f"Exception details\n"
              f"{e}")
        if mock:
            with open(mock_file_path, 'r') as f:
                resp_dict = json.load(f)
        else:
            raise

    info(f'\nResponse received: \n{pformat(resp_dict)}')

    def get_promo(promotions, name):
        """
        Helper function to find a return a promotion with a given name
        :param promotions (list): list of dictionaries, one per promotion
        :param name (string): string to match in the Name field
        :return: None
        """
        for promo in promotions:
            if promo['Name'] == name:
                return promo

    if not mock:
        assert(response.status_code == 200)
    assert(resp_dict['Name'] == 'Carbon credits')
    assert(resp_dict['CanRelist'] is True)
    gallery = get_promo(resp_dict['Promotions'], 'Gallery')
    assert('Good position in category' in gallery['Description'])
