import pytest
from selenium import webdriver
from config.config import Testdata
# from webdriver manager.chrome import ChromeDriverManager
# from webdriver manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
import platform, sys, selenium


def write_allure_environment(driver, base_url):
    browser = driver.capabilities['browserName']
    browser_version = driver.capabilities['browserVersion']
    with open("C:/self_automation_Swag_labs/allure_reports/environment.properties", "w") as f:
        f.write(f"os_platform={platform.system()}\n")
        f.write(f"os_version={platform.version()}\n")
        f.write(f"browser={browser}\n")
        f.write(f"browser_version={browser_version}\n")
        f.write(f"base_url={base_url}\n")
        f.write(f"python_version={sys.version}\n")
        f.write(f"selenium_version={selenium.__version__}\n")

# hooks
def pytest_addoption(parser):
    """To get browser form CLI"""
    parser.addoption(
        "--browser_name",
        action="store",
        default="all",  # "all" means run on both browsers
        help="Choose browser: chrome, firefox, or all"
    )

# @pytest.fixture(params=["chrome"], scope='function')
@pytest.fixture(params=["chrome", "firefox"], scope='function')
def init_driver(request):
    """if browser name all then run both else run one and else skip"""
    browser_name = request.config.getoption("browser_name")
    if browser_name != "all" and request.param != browser_name:
        pytest.skip(f"Skipping {request.param} as --browser_name={browser_name} was passed")

    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")  # Launch Chrome in incognito mode
        service = Service(executable_path=Testdata.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=service, options=options)
        # service = Service(executable_path=Testdata.CHROME_EXECUTABLE_PATH)
        # web_driver = webdriver.Chrome(service=service)
    elif request.param == "firefox":
        service = Service(executable_path=Testdata.FIREFOX_EXECUTABLE_PATH)
        web_driver = webdriver.Firefox(service=service)
        # web_driver.get(Testdata.BASE_URL)
    request.cls.driver = web_driver
    write_allure_environment(web_driver, Testdata.BASE_URL)  # create env report
    yield
    web_driver.close()


# hooks
def pytest_sessionstart(session):
    print("\n[Pytest Hook] Test session is starting...")


# hooks
def pytest_sessionfinish(session, exitstatus):
    print("\n[Pytest Hook] Test session finished!")
