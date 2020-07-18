from covid_mx_data import CovidMxData


def test_url_reciente():
    covid = CovidMxData()
    assert covid.urlRec != ""


def test_url_diccionario():
    covid = CovidMxData()
    assert covid.urlDicc != ""


def test_url_historico():
    covid = CovidMxData()
    assert covid.urlHist != ""


def test_download_reciente():
    covid = CovidMxData()
    res = covid.reciente()
    assert len(res) > 0


def test_download_reciente_unzipped():
    covid = CovidMxData()
    res = covid.reciente(unzip=False)
    assert len(res) > 0


def test_download_diccionario():
    covid = CovidMxData()
    res = covid.diccionario_covid()
    assert len(res) > 0


def test_download_diccionario_unzipped():
    covid = CovidMxData()
    res = covid.diccionario_covid(unzip=False)
    assert len(res) > 0


# Long time running...
def test_download_historico():
    covid = CovidMxData()
    res = covid.historico_covid()
    assert len(res) > 0


def test_download_historico_unzipped():
    covid = CovidMxData()
    res = covid.historico_covid(unzip=False)
    assert len(res) > 0
