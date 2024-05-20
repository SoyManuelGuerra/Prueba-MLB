# Prueba-MLB
#Youtube_Prueba_busqueda
# Aca almacenamos todas las librerias importadas
from selenium.webdriver.common.by import By
from selenium import webdriver
import time 

# Aca instanciamos el driver de chrome
driver=webdriver.Chrome()

# aca le indicamos al driver que se dirija a la pagina de youtube
driver.get("https://www.youtube.com")

# Aca maximizamos la ventana del navegador
driver.maximize_window()
# Aca buscamos el elemento por el nombre de la clase
driver.find_element(By.NAME, "search_query").click()
driver.find_element(By.NAME, "search_query").send_keys("MLB")
driver.find_element(By.ID, "search-icon-legacy").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "yt-spec-touch-feedback-shape__fill").click()

# Aca le indicamos al driver que espere 5 segundos
time.sleep(120)

# Aca cerramos el navegador
driver.quit()