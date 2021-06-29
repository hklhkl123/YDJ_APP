import pytest
from base.base_driver import init_driver

params= ['honor_v8','Moto','koobee']
# params=['koobee']

@pytest.fixture(params=params)
def login_common_driver(request):
    driver = init_driver(device = request.param)
    yield driver
    # driver.close_app()
    driver.quit()