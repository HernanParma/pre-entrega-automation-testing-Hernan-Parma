import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_first_product_info

def test_inventory_navigation_and_verification(login_in_driver):
    """
    Test para verificar la navegación y el catálogo de productos
    Valida título, presencia de productos y obtiene información del primer producto
    """
    driver = login_in_driver
    
    # Verificar que estamos en la página de inventario
    assert "/inventory.html" in driver.current_url, "No estamos en la página de inventario"
    
    # Verificar el título de la página
    wait = WebDriverWait(driver, 10)
    title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    assert "Products" in title_element.text, "El título de la página no es correcto"
    
    # Verificar que existan productos visibles
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No se encontraron productos en la página"
    print(f"Se encontraron {len(products)} productos en el catalogo")
    
    # Verificar elementos importantes de la interfaz
    # Menú hamburguesa
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_button.is_displayed(), "El botón del menú no está visible"
    
    # Filtros
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filter_dropdown.is_displayed(), "El filtro de productos no está visible"
    
    # Carrito de compras
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert cart_link.is_displayed(), "El enlace del carrito no está visible"
    
    # Obtener información del primer producto
    product_name, product_price = get_first_product_info(driver)
    print(f"Primer producto: {product_name} - Precio: {product_price}")
    
    # Verificar que el nombre y precio no estén vacíos
    assert product_name.strip() != "", "El nombre del primer producto está vacío"
    assert product_price.strip() != "", "El precio del primer producto está vacío"
    
    print("Navegacion y verificacion del catalogo completada exitosamente")        