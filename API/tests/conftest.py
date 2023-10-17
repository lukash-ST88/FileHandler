import pytest
from pytest_factoryboy import register
from .factories import FileFactory
from rest_framework.test import APIClient

register(FileFactory)


@pytest.fixture(scope='session', autouse=True)
def simple_yield_fixture():
    print('tests start')
    yield
    print('test finish')


@pytest.fixture(scope='session')
def api_client():
    return APIClient()

