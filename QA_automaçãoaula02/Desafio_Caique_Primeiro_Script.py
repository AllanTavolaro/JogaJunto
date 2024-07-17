from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def main() -> None:
    browser = Firefox()
    browser.get("https://www.google.com")
    
    input_area = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    input_area.send_keys('Instituto Joga Junto')
    input_area.send_keys(Keys.ENTER)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )
    
    result_search = browser.find_elements(By.CSS_SELECTOR, "h3")
    
    check = any('Instituto Joga Junto' in result.text for result in result_search)
    
    if check:
        print("O resultado desejado foi encontrado!")
    else:
        print("O resultado desejado não foi encontrado.")
    
    for result in result_search:
        if 'Instituto Joga Junto' in result.text:
            result.click()
            print("Link encontrado e clicado!")
            break
    
    WebDriverWait(browser, 10).until(
        EC.title_contains("Instituto Joga Junto")
    )
    
    assert 'Instituto Joga Junto' in browser.title, "Página incorreta na busca"
    
    input_nome = browser.find_element(By.ID, "nome")
    input_nome.send_keys('Allan Tavolaro')
    
    input_email = browser.find_element(By.ID, "email")
    input_email.send_keys('allantavolaro@hotmail.com')
    
    input_assunto = browser.find_element(By.ID, "assunto")
    select = Select(input_assunto)
    select.select_by_index(5)
    
    input_msg = browser.find_element(By.ID, "mensagem")
    input_msg.send_keys('Minha primeira automação')
    
    button_enviar = browser.find_element(By.XPATH, "//button[@type='submit']")
    button_enviar.click()
    
    time.sleep(10)
    
    browser.quit()

if __name__ == "__main__":
    main()
