import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import add_first_product_to_cart, get_cart_count, go_to_cart, get_first_product_info

def test_cart_interaction(login_in_driver):
    """
    Test para verificar la interacción con el carrito de compras
    Añade un producto al carrito, verifica el contador y navega al carrito
    """
    driver = login_in_driver
    
    # Obtener información del primer producto antes de añadirlo
    product_name, product_price = get_first_product_info(driver)
    print(f"Producto seleccionado: {product_name} - Precio: {product_price}")
    
    # Verificar que el carrito esté vacío inicialmente
    initial_cart_count = get_cart_count(driver)
    print(f"Contador inicial del carrito: {initial_cart_count}")
    
    # Buscar y hacer clic en el primer botón "Add to cart" directamente
    wait = WebDriverWait(driver, 10)
    add_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
    assert len(add_buttons) > 0, "No se encontraron botones 'Add to cart'"
    
    print(f"Se encontraron {len(add_buttons)} botones 'Add to cart'")
    add_buttons[0].click()
    print("Producto anadido al carrito")
    
    # Esperar un momento para que se actualice el contador
    import time
    time.sleep(2)
    
    # Verificar que el contador del carrito se incremente
    new_cart_count = get_cart_count(driver)
    print(f"Contador después de añadir: {new_cart_count}")
    
    assert new_cart_count > initial_cart_count, f"El contador del carrito no se incrementó. Inicial: {initial_cart_count}, Actual: {new_cart_count}"
    print(f"Contador del carrito actualizado: {new_cart_count}")
    
    # Navegar al carrito de compras
    go_to_cart(driver)
    print("Navegacion al carrito completada")
    
    # Verificar que estamos en la página del carrito
    assert "/cart.html" in driver.current_url, "No se navegó correctamente al carrito"
    
    # Verificar que el producto añadido aparezca en el carrito
    wait = WebDriverWait(driver, 10)
    cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    assert len(cart_items) > 0, "No se encontraron productos en el carrito"
    print(f"Se encontraron {len(cart_items)} productos en el carrito")
    
    # Verificar que el primer producto en el carrito sea el que añadimos
    first_cart_item = cart_items[0]
    cart_item_name = first_cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    cart_item_price = first_cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    assert cart_item_name == product_name, f"El nombre del producto en el carrito no coincide. Esperado: {product_name}, Actual: {cart_item_name}"
    assert cart_item_price == product_price, f"El precio del producto en el carrito no coincide. Esperado: {product_price}, Actual: {cart_item_price}"
    
    print(f"Producto verificado en el carrito: {cart_item_name} - {cart_item_price}")
    print("Interaccion con el carrito completada exitosamente")
