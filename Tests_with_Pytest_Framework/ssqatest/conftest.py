

import pytest
import os
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'firefox','ff']
    browser = os.environ.get('BROWSER', None)

    if not browser:
        raise Exception("The enviroment variables 'BROWSER' must be set. ")

    browser=browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provide browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome','ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox','ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        #Check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")

                screen_shot_path = os.path.join(results_dir, item.name + ".png")
                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screen_shot_path)
                extra.append(pytest_html.extras.image(screen_shot_path))
            # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
        report.extra = extra