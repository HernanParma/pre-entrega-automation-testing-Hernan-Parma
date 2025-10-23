import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_validation(login_in_driver):
    """
    Test para validar el login exitoso en saucedemo.com
    Verifica que se redirija a la página de inventario y que el título sea correcto
    """
    driver = login_in_driver
    
    # Verificar que se redirigió a la página de inventario
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    
    # Verificar que el título de la página sea correcto
    wait = WebDriverWait(driver, 10)
    title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    assert "Products" in title_element.text, "El título de la página no es correcto"
    
    # Verificar que aparezca "Swag Labs" en algún lugar de la página
    page_source = driver.page_source
    assert "Swag Labs" in page_source, "No se encontró 'Swag Labs' en la página"
    
    print("Login exitoso - Redireccion y titulo validados correctamente")        