from main import *


def test_loads_true():
    assert loads("true") == True


def test_loads_false():
    assert loads("false") == False


def test_loads_null():
    assert loads("null") == None


def test_loads_number():
    assert loads("1") == 1


def test_loads_string():
    assert loads('"opa, isso é um teste"') == 'opa, isso é um teste'


def test_loads_list():
    expected = [True, False, None, [1, 2, 3]]
    assert loads("[true,false,null,[1,2,3]]") == expected


def test_loads_object():
    expected = {
        "teste": [1, 2, [], "abc"],
        "outroteste": "valor teste"
    }
    assert loads('{"teste":[1,2,[],"abc"],"outroteste":"valor teste"}') == expected
