import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="class")
def LunchDriver(request):
    driver = webdriver.Chrome()
    driver.get("https://xpertbotacademy.online/nova/login")
    request.cls.driver = driver
    yield driver
    driver.quit()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    test_item = item._nodeid.split("[")[1].split("]")[0].split("-")[-1].strip()

    # Set the test description by formatting the docstring with the label
   
    # Preserve the test name while removing the label and additional information
    test_name_parts = report.nodeid.split("[")[0].split("-")
    test_name = "-".join(test_name_parts[:-1]) if len(test_name_parts) > 1 else test_name_parts[0]
    test_data_number = report.nodeid.split("[")[1].split("]")[0] if "[" in report.nodeid else ""
    report.nodeid = f"{test_name}[{test_data_number}]"
    extra = getattr(report, "extra", [])


    if report.when == "call":
        # Always add URL to report
        extra.append(pytest_html.extras.url("https://xpertbotacademy.online/nova/login"))
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            # Only add additional HTML on failure
            report_directory = os.path.dirname(item.config.option.htmlpath) 
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver = item.cls.driver
            driver.save_screenshot(destination_file)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;" ' 'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))

        report.extra = extra


def pytest_html_report_title(report):
    report.title = 'QA Automation Test'



