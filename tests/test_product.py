import json

import requests
from assertpy import assert_that

from support.headers import headers
from support.url import BASE_URI


def test_01_list_all_products():
    list = requests.get(url=BASE_URI+"/products", headers=headers, verify=False)
    assert list.status_code == 200

def test_02_list_one_product():
    list_one_product = requests.get(url=BASE_URI+"/products/1", headers=headers, verify=False)
    assert list_one_product.status_code == 200

    '''Verifying the id of the response, to confirm that
        the response is exactly from the product with the id
        specified on the request
    '''
    assert_that(list_one_product.json()['id']).is_equal_to(1)

def test_03_list_products_with_limit_8():

    list = requests.get(url=BASE_URI+"/products", params={"limit": 8}, headers=headers, verify=False)
    assert list.status_code == 200

    # Verifying the length of the response
    assert_that(list.json()).is_length(8)

