from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver):
    """Función para realizar login en saucedemo.com"""
    driver.get("https://www.saucedemo.com")
    
    # Esperar a que aparezcan los campos de login
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    # Ingresar credenciales
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    
    # Esperar a que se complete el login
    wait.until(EC.url_contains("/inventory.html"))

def get_first_product_info(driver):
    """Obtiene información del primer producto en la página"""
    wait = WebDriverWait(driver, 10)
    first_product = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    
    product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    return product_name, product_price

def add_first_product_to_cart(driver):
    """Añade el primer producto al carrito"""
    wait = WebDriverWait(driver, 10)
    # Buscar el primer botón "Add to cart" en la página
    first_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
    first_add_button.click()
    return True

def get_cart_count(driver):
    """Obtiene el número de items en el carrito"""
    try:
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
    except:
        return 0

def go_to_cart(driver):
    """Navega al carrito de compras"""
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    
    # Esperar a que se cargue la página del carrito
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/cart.html"))