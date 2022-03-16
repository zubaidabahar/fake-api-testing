import requests
from assertpy import assert_that

from support.headers import headers
from support.url import BASE_URI


def test_01_list_all_categories():
    list = requests.get(url=BASE_URI+"/products/categories", headers=headers, verify=False)

    assert list.status_code == 200

def test_02_list_products_specific_category():
    category = "jewelery"
    list = requests.get(url=BASE_URI+"/products/categories"+category, headers=headers, verify=False)
    assert list.status_code == 200

    ''' Verifying if the category on the response
         is the same as the one specified   
    '''
    assert_that(list.json()['category']).is_equal_to(category)