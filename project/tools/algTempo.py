from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import json

class TempoEle:
    def __init__(self, cidadeNome, tempMin, tendenciaMin, tempMax, tendenciaMax, umidadeMax, umidadeMin, nascerDoSol,
                 porDoSol, manhaTexto, manhaDirecao, manhaVento, tardeTexto, tardeDirecao, tardeVento, noiteTexto,
                 noiteDirecao, noiteVento):
        self.cidadeNome = cidadeNome
        self.tendenciaMax = tendenciaMax
        self.umidadeMax = umidadeMax
        self.umidadeMin = umidadeMin
        self.nascerDoSol = nascerDoSol
        self.porDoSol = porDoSol
        self.manhaTexto = manhaTexto
        self.manhaDirecao = manhaDirecao
        self.manhaVento = manhaVento
        self.tardeTexto = tardeTexto
        self.tardeDirecao = tardeDirecao
        self.tardeVento = tardeVento
        self.noiteTexto = noiteTexto
        self.noiteDirecao = noiteDirecao
        self.noiteVento = noiteVento
        self.tempMax = tempMax
        self.tendenciaMin = tendenciaMin
        self.tempMin = tempMin

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')


def HolyMoly(body):
    #options = Options()
    #options.add_argument('--headless')
    inputed = body

    driver = webdriver.Firefox(executable_path='D:\geckodriver.exe')#, options=options)

    # entrar no site
    driver.get('http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias')

    # pegar a caixa de input
    search_field = driver.find_element_by_id("search-heather")
    search_field.clear()

    # colocar o texto la
    actionChains = webdriver.ActionChains(driver)
    actionChains.double_click(search_field).perform()
    search_field.send_keys(inputed)

    lista = driver.find_element_by_id('ui-id-1')

    driver.implicitly_wait(2)
    lil = lista.find_element_by_class_name('ui-menu-item')
    aa = lil.find_element_by_tag_name('a')

    aa.click()

    driver.implicitly_wait(2)

    driver.implicitly_wait(2)

    # pegar os valores

    divisaoMenor = driver.find_element_by_id('quadro1_interno_main')
    driver.implicitly_wait(2)
    cidade = driver.find_element_by_id('barra1_main').find_element_by_id('barra1_txt').find_element_by_tag_name(
        'p').text
    tempMin = divisaoMenor.find_elements_by_id('quadro1_interno_circulo_img')[0].find_element_by_tag_name(
        'div').find_element_by_class_name('knob').get_attribute(
        'value')
    tendenciaMin = divisaoMenor.find_element_by_id('quadro1_interno_circulo_tendencia_main').find_element_by_id(
        'quadro1_interno_circulo_tend_tit_tempmin').find_element_by_tag_name('b').text

    driver.implicitly_wait(2)
    tempMax = divisaoMenor.find_elements_by_id('quadro1_interno_circulo_img')[1].find_element_by_tag_name(
        'div').find_element_by_class_name('knob').get_attribute(
        'value')
    tendenciaMax = divisaoMenor.find_element_by_id('quadro1_interno_circulo_tendencia_main').find_element_by_id(
        'quadro1_interno_circulo_tend_tit_tempmax').find_element_by_tag_name('b').text

    quadroDados = divisaoMenor.find_element_by_id('quadro1_interno_quadro_dados')
    umidadeMax = quadroDados.find_element_by_id('quadro1_interno_dados_txt_umidade_max').find_element_by_tag_name(
        'p').text
    umidadeMin = quadroDados.find_element_by_id('quadro1_interno_dados_txt_umidade_min').find_element_by_tag_name(
        'p').text
    print("min")
    print(umidadeMin)
    print(umidadeMax)
    nascerDoSol = quadroDados.find_element_by_id('quadro1_interno_dados_txt_nascer_sol').find_element_by_tag_name(
        'p').text
    porDoSol = quadroDados.find_element_by_id('quadro1_interno_dados_txt_ocaso_sol').find_element_by_tag_name('p').text

    manhaTexto = divisaoMenor.find_element_by_id('quadro1_interno_manha_main').find_element_by_id(
        'quadro1_interno_manha_quadro').find_element_by_id('quadro1_interno_manha_quadro_txt').find_element_by_tag_name(
        'p').text
    manhaDirecao = divisaoMenor.find_element_by_id('quadro1_interno_manha_main').find_element_by_id(
        'quadro1_interno_manha_quadro_dirvento_main').find_element_by_id(
        'quadro1_interno_manha_quadro_dirvento').find_element_by_tag_name('p').find_element_by_tag_name('i').text
    manhaVento = divisaoMenor.find_element_by_id('quadro1_interno_manha_main').find_element_by_id(
        'quadro1_interno_manha_quadro_vento').find_element_by_tag_name('p').find_element_by_tag_name('i').text

    tardeTexto = divisaoMenor.find_element_by_id('quadro1_interno_tarde_main').find_element_by_id(
        'quadro1_interno_tarde_quadro').find_element_by_id(
        'quadro1_interno_tarde_quadro_txt2').find_element_by_tag_name('p').text
    tardeDirecao = divisaoMenor.find_element_by_id('quadro1_interno_tarde_main').find_element_by_id(
        'quadro1_interno_tarde_quadro_dirvento_main').find_element_by_id(
        'quadro1_interno_tarde_quadro_dirvento').find_element_by_tag_name('p').find_element_by_tag_name('i').text
    tardeVento = divisaoMenor.find_element_by_id('quadro1_interno_tarde_main').find_element_by_id(
        'quadro1_interno_tarde_quadro_vento_main').find_element_by_id(
        'quadro1_interno_tarde_quadro_vento').find_element_by_tag_name('p').find_element_by_tag_name('i').text

    noiteTexto = divisaoMenor.find_element_by_id('quadro1_interno_noite_main').find_element_by_id(
        'quadro1_interno_noite_quadro').find_element_by_id(
        'quadro1_interno_noite_quadro_txt3').find_element_by_tag_name('p').text
    noiteDirecao = divisaoMenor.find_element_by_id('quadro1_interno_noite_main').find_element_by_id(
        'quadro1_interno_noite_quadro_dirvento_main').find_element_by_id(
        'quadro1_interno_noite_quadro_dirvento').find_element_by_tag_name('p').find_element_by_tag_name('i').text
    noiteVento = divisaoMenor.find_element_by_id('quadro1_interno_noite_main').find_element_by_id(
        'quadro1_interno_noite_quadro_vento_main').find_element_by_id(
        'quadro1_interno_noite_quadro_vento').find_element_by_tag_name('i').text

    objTempo = TempoEle(cidade, tempMin, tendenciaMin, tempMax, tendenciaMax, umidadeMax, umidadeMin, nascerDoSol,
                        porDoSol, manhaTexto, manhaDirecao, manhaVento, tardeTexto, tardeDirecao, tardeVento,
                        noiteTexto, noiteDirecao, noiteVento)

    driver.quit()

    return (json.dumps(objTempo.__dict__, default=lambda o: o.__dict__, indent=4, sort_keys=True,
                       ensure_ascii=False)).replace("\n", "")