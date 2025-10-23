from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def debug_cart():
    """Script para debuggear el problema del carrito"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        # Login
        driver.get("https://www.saucedemo.com")
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Esperar a que se cargue la página de inventario
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("/inventory.html"))
        
        print("Login exitoso")
        
        # Buscar todos los botones de "Add to cart"
        add_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        print(f"Se encontraron {len(add_buttons)} botones 'Add to cart'")
        
        if len(add_buttons) > 0:
            print("Primer botón encontrado, intentando hacer clic...")
            add_buttons[0].click()
            time.sleep(2)
            
            # Verificar el contador del carrito
            try:
                cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
                print(f"Contador del carrito: {cart_badge.text}")
            except:
                print("No se encontró el badge del carrito")
                
            # Verificar si hay elementos en el carrito
            cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
            print(f"Elementos en el carrito: {len(cart_items)}")
            
        else:
            print("No se encontraron botones 'Add to cart'")
            
        # Buscar otros selectores posibles
        print("\nBuscando otros selectores...")
        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Total de botones en la página: {len(all_buttons)}")
        
        for i, button in enumerate(all_buttons[:5]):  # Solo los primeros 5
            try:
                text = button.text
                classes = button.get_attribute("class")
                print(f"Botón {i}: texto='{text}', clases='{classes}'")
            except:
                pass
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_cart()

