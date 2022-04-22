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
    global pos

    if src.startswith("true", pos):
        pos += 4
        return True
    if src.startswith("false", pos):
        pos += 5
        return False
    if src.startswith("null", pos):
        pos += 4
        return None
    if src[pos].isdigit():
        return read_number()
    if src[pos] == '"':
        return read_string()
    if src[pos] == '[':
        return read_array()
    if src[pos] == '{':
        return read_object()


def read_number():
    global pos
    pos_end = pos
    while pos_end < len(src) and src[pos_end].isdigit():
        pos_end += 1
    n = int(src[pos:pos_end])
    pos = pos_end
    return n


def read_string():
    global pos
    pos_end = src.find('"', pos + 1)
    st = src[pos + 1: pos_end]
    pos = pos_end + 1
    return st


def read_array():
    global pos

    pos += 1
    if src[pos] == ']':
        pos += 1
        return []

    elements = [read_value()]
    while True:
        if src[pos] == ']':
            pos += 1
            return elements
        read(',')
        elements.append(read_value())


def read(param):
    global pos
    if not src.startswith(param, pos):
        raise SyntaxError(f"erro: {param}")
    pos += len(param)


def read_pair():
    key = read_string()
    read(":")
    value = read_value()
    return key, value

def read_object():
    global pos

    pos +=1
    if src[pos] == "}":
        pos +=1
        return {}

    elements = [read_pair()]
    while True:
        if src[pos] == "}":
            pos += 1
            return dict(elements)
        read(",")
        elements.append(read_pair())
