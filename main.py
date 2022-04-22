true, false, null = True, False, None
{
    "nome": "Nome fictitious",
    "ficticio": true,
    "bens": ["casa", "carro", "cavalo"],
    "endereco": {
        "rua": "Luz do Sol",
        "referencia": "do lado do sol"
    },
    "idade": 99,
    "especie": null
}

src = ""
pos = 0


def loads(text) -> object:
    global src, pos
    src = text
    pos = 0
    return read_value()


def read_value():
    if src == "true":
        return True
    if src == "false":
        return False
    if src == "null":
        return None
    if src.isdigit():
        return read_number()
    if src[0] == '"':
        return read_string()


def read_string():
    pos_end = src.find('"', pos + 1)
    return src[pos + 1: pos_end]


def read_number():
    pos_end = pos
    while pos_end < len(src) and src[pos_end].isdigit():
        pos_end += 1
    return int(src[pos:pos_end])


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
