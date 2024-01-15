import pytest
import selene
from selene import browser, be, have

@pytest.fixture(autouse=True)
def settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_invalid_request():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('lkdfmfkdlfsdkflfjdk456432dfsdfds').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))


