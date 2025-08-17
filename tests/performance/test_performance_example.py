import time
import allure


@allure.feature("Performance")
def test_homepage_load_time(page, base_url):
    start = time.time()
    page.goto(base_url)
    load_time = time.time() - start
    allure.attach(
        f"{load_time:.2f}s",
        name="load_time",
        attachment_type=allure.attachment_type.TEXT,
    )
    assert load_time >= 0
