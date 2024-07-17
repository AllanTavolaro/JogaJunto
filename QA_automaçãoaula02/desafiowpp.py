#Escreva uma automação para acessar o Whatsapp web.
#Envie uma mensagem para o grupo de estudos do IJJ com a mensagem: Automação do WhatsApp - Squad 6

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def delay_teclas(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

browser = Firefox()
browser.get('https://web.whatsapp.com')

print("Escaneie o QR Code com seu celular para acessar o WhatsApp Web.")
time.sleep(20)

contato = "[TA 1/2024] QA MÓDULO AVANÇADO"
mensagem = "Automação do WhatsApp"

barra_busca = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
barra_busca.click()
delay_teclas(barra_busca, contato)
barra_busca.send_keys(Keys.ENTER)

time.sleep(3)

caixa_texto = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
caixa_texto.click()
delay_teclas(caixa_texto, mensagem)
caixa_texto.send_keys(Keys.ENTER)

print("Mensagem enviada com sucesso!")

time.sleep(10)

browser.quit()

# from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# browser = Firefox()
# browser.get('https://web.whatsapp.com')

# print("Escaneie o QR Code com seu celular para acessar o WhatsApp Web.")
# time.sleep(20)

# contato = "[TA 1/2024] QA MÓDULO AVANÇADO"
# mensagem = "Automação do WhatsApp - Squad 6."

# search_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
# search_box.click()
# search_box.send_keys(contato)
# search_box.send_keys(Keys.ENTER)

# time.sleep(3)

# message_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
# message_box.click()
# message_box.send_keys(mensagem)
# message_box.send_keys(Keys.ENTER)

# print("Mensagem enviada com sucesso!")

# time.sleep(10)

# browser.quit()