import json

import requests
from assertpy import assert_that

from support.headers import headers
from support.url import BASE_URI
from support.product_data import new_product


def test_01_create_new_product():
    create_product = requests.post(url=BASE_URI+"/products", headers=headers, json=new_product, verify=False)
    assert create_product.status_code == 200
    assert_that(create_product.json()['title']).is_equal_to(new_product['title'])
    assert_that(create_product.json()['price']).is_equal_to(new_product['price'])
    assert_that(create_product.json()['description']).is_equal_to(new_product['description'])
    assert_that(create_product.json()['image']).is_equal_to(new_product['image'])
    assert_that(create_product.json()['category']).is_equal_to(new_product['category'])


def test_02_list_all_products():
    list = requests.get(url=BASE_URI+"/products", headers=headers, verify=False)
    assert list.status_code == 200

def test_03_list_one_product():
    list_one_product = requests.get(url=BASE_URI+"/products/1", headers=headers, verify=False)
    assert list_one_product.status_code == 200

    '''Verifying the id of the response, to confirm that
        the response is exactly from the product with the id
        specified on the request
    '''
    assert_that(list_one_product.json()['id']).is_equal_to(1)

def test_04_list_products_with_limit_8():

    list = requests.get(url=BASE_URI+"/products", params={"limit": 8}, headers=headers, verify=False)
    assert list.status_code == 200

    # Verifying the length of the response
    assert_that(list.json()).is_length(8)

def test_05_delete_product():
    # First create one new product
    create = requests.post(url=BASE_URI+"/products", headers=headers, json=new_product, verify=False)

    # Get the id from the product created
    product_id = str(create.json()['id'])

    # Delete the product
    delete = requests.delete(url=BASE_URI+"/products/"+product_id, headers=headers, verify=False)
    assert delete.status_code == 200