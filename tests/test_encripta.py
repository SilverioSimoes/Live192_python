from cesar.cesar import encripta


def test_encripta_silverio_retorna_fvyirevb():
    assert encripta('silverio') == 'fvyirevb'


def test_encripta_fvyirevb_retorna_silverio():
    assert encripta('fvyirevb') == 'silverio'


def test_encripta_deve_retornar_minusculas():
    assert encripta('A').islower()


def test_encripta_deve_preservar_os_espacos():
    resultado = encripta('e a')
    assert resultado[1] == ' '
