from selenium import webdriver
import json
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Acao:
    def __init__(self, preco, mudanca, classeMudanca, nome):
        self.nome = nome
        self.preco = preco
        self.mudanca = mudanca
        self.classeMudanca = classeMudanca

    def toJSON(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')


class BolsaAcao(object):
    def __init__(self, bolsa: [Acao]):
        self.bolsa = bolsa


def PegarAcao(body1):
    listaAcao = []
    options = Options()
    options.add_argument('--headless')
    inputed = body1
    driver = webdriver.Firefox(executable_path='C:\geckodriver.exe', options=options)
    # entrar no site
    driver.get(
        'http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Nome=AAAAAAAAA&idioma=pt-br'.replace(
            'AAAAAAAAA', inputed))

    driver.implicitly_wait(2)

    driver.find_element_by_xpath("//*[@class='GridRow_SiteBmfBovespa GridBovespaItemStyle']").find_element_by_tag_name(
        'td').find_element_by_tag_name('a').click()
    print("antes")
    driver.implicitly_wait(5)
    driver.switch_to.frame('ctl00_contentPlaceHolderConteudo_iframeCarregadorPaginaExterna')
    auxiliarPegar = driver.find_elements_by_xpath("html/body/div[2]/div[1]/ul/li[1]/div/table/tbody/tr[2]/td[2]/a")

    lista = []
    for x in auxiliarPegar:
        lista.append(x.text)

    lista.pop(0)
    print(lista)

    driver.switch_to.default_content()
    for x in lista:

        driver.implicitly_wait(2)

        driver.get(
            'http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/?symbol=YAREYAREDAZE'.replace(
                'YAREYAREDAZE', x))

        try:
            driver.implicitly_wait(1)

            myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//iframe[1]')))

            driver.switch_to.frame(myElem)

            driver.implicitly_wait(1)

            preco = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[1]")))
            while (preco.text == ""):
                preco = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                       "html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[1]")))
            driver.implicitly_wait(1)

            mudanca = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[3]")))
            while (mudanca.text == ""):
                mudanca = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[3]")))

            varMuClass = mudanca.get_attribute('class')

            driver.implicitly_wait(1)

            varMudanca = mudanca.text

            driver.implicitly_wait(1)

            varPreco = preco.text

            driver.implicitly_wait(1)

            listaAcao.append(Acao(varPreco, varMudanca, varMuClass, x))

            driver.implicitly_wait(1)


        except TimeoutException:
            print ("Ta demorando")

    BolsaAcao1 = BolsaAcao(listaAcao)
    print(json.dumps(BolsaAcao1.__dict__, default=lambda o: o.__dict__, indent=4, sort_keys=True, ensure_ascii=False))
    driver.quit()
    print("\\")
    return (json.dumps(BolsaAcao1.__dict__, default=lambda o: o.__dict__, indent=4, sort_keys=True,
                       ensure_ascii=False)).replace("\n", "")