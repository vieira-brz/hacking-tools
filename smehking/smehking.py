from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


def open_new_tab(driver):
    # Recomeçando do 0 se o google pedir verificação humana
    if "Nossos sistemas detectaram tráfego incomum na sua rede" in driver.page_source:
        time.sleep(45)
    else:
        # Abrir uma nova aba
        driver.execute_script("window.open('', '_blank');")

        time.sleep(2)

        # Fechar aba antiga se não tiver resultados
        if "Aproximadamente 0 resultados" in driver.page_source:
            driver.close()

        # Mudar para a nova aba
        driver.switch_to.window(driver.window_handles[-1])


def main(fullname, username):
    #
    # Inicializar o driver do navegador Firefox
    #
    options = Options()
    options.set_preference("network.http.phishy-userpass-length", 255)
    options.set_preference("network.automatic-ntlm-auth.trusted-uris", "localhost")
    options.set_preference("network.negotiate-auth.delegation-uris", "localhost")
    options.set_preference("network.negotiate-auth.trusted-uris", "localhost")
    options.set_preference("dom.disable_window_open_feature.location", True)
    driver = webdriver.Firefox()

    #
    # Aba Facebook
    #
    query = f"site%3Afacebook.com+\"{fullname}\"+and+\"Profiles\""
    driver.get(f"https://www.google.com/search?q={query}")
    open_new_tab(driver)

    #
    # Perfil Facebook
    #
    if username.strip() != '':
        query = f"site%3Afacebook.com+inurl%3A{username}+intext%3A\"is+on+Facebook\""
        driver.get(f"https://www.google.com/search?q={query}")
        open_new_tab(driver)

    #
    # Perfil Instagram
    #
    if username.strip() != '':
        query = f"site%3Ainstagram.com+intext%3A\"{username}\"+OR+inurl%3A{username}"
        driver.get(f"https://www.google.com/search?q={query}")
        open_new_tab(driver)

    #
    # Perfis do Instagram relacionados
    #
    query = f"site%3Ainstagram.com+intext%3A\"{fullname}\""
    driver.get(f"https://www.google.com/search?q={query}")
    open_new_tab(driver)

    #
    # Perfil Twitter
    #
    if username.strip() != '':
        query = f"site%3Atwitter.com+inurl%3A{username}"
        driver.get(f"https://www.google.com/search?q={query}")
        open_new_tab(driver)

    #
    # Perfis do Twitter relacionados
    #
    query = f"site%3Atwitter.com+intext%3A{fullname}"
    driver.get(f"https://www.google.com/search?q={query}")
    open_new_tab(driver)

    #
    # Perfil TikTok
    #
    if username.strip() != '':
        query = f"site%3Atiktok.com+inurl%3A{username}"
        driver.get(f"https://www.google.com/search?q={query}")
        open_new_tab(driver)

    #
    # Perfil Linkedin
    #
    if username.strip() != '':
        query = f"site%3Alinkedin.com+inurl%3A%2Fin%2F{username}"
        driver.get(f"https://www.google.com/search?q={query}")
        open_new_tab(driver)

    #
    # Perfis do Linkedin relacionados
    #
    query = f"site%3Alinkedin.com+intext%3A{fullname}"
    driver.get(f"https://www.google.com/search?q={query}")
    if "Aproximadamente 0 resultados" in driver.page_source:
        driver.close()

    # Encerrando código
    time.sleep(3600)
    driver.quit()


if __name__ == "__main__":
    #
    # Get Infos
    #
    fullname = input("Name to search: ")
    fullname = "+".join(fullname.split())
    username = input("Username: ")
    main(fullname, username)