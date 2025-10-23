import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import login

@pytest.fixture
def driver():
    """Fixture para crear y configurar el driver de Chrome"""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Usar el nuevo modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    """Fixture que realiza login y retorna el driver autenticado"""
    login(driver)
    return driver