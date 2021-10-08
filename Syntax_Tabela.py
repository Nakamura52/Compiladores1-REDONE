tabela_TS={}
lista_token=[]
tipo_esperado =""

def inserir_TS(token):
    global tabela_TS
    insert_ts = {token.value: {"Token": token.type}}
    busca_ts = get_ts(token)
    if busca_ts == None:
        tabela_TS.update(insert_ts)
    else:
        print("Variável já declarada:", (token.value))
        exit()

def get_ts(token):
    global tabela_TS
    get_dict = tabela_TS.get(token.value)
    #print('TESTEEEEEEEE', get_dict)
    return get_dict

def check(tokens):
    if not tokens:
        print("Cadeia incompleta")
        exit()

def Z(tokens):
    I(tokens)
    S(tokens)
    print('\nTabela de Simbolos:')
    for x in tabela_TS:
        print ('Nome:',x)
        for y in tabela_TS[x]:
            print (y,':',tabela_TS[x][y])

def erro(token, esperado):
    print("Erro de sintaxe: Linha {} | Esperado: {} | Entrada: {}"
          "".format(token.index,esperado, token.value))
    exit()
def I(tokens):
    check(tokens)
    token = tokens.pop(0)
    if token.value != "var":
        erro(token, "var")
    D(tokens)

def D(tokens):
    check(tokens)
    L(tokens)
    token = tokens.pop(0)
    if token.value != ":":
        erro(token, "delimitador")
        exit()
    K(tokens)
    O(tokens)

def K(tokens):
    check(tokens)
    token = tokens.pop(0)
    #print(token)
    if token.value not in ("real", "integer"):
        erro(token, 'Palavra Reservada')
    for elemento in lista_token:
        busca_TS = get_ts(elemento)
        busca_TS.update({"Tipo": token.value})
    lista_token.clear()

def O(tokens):
    check(tokens)
    if not tokens:
        print("ERRO: cadeia incompleta")
        exit()
    token = tokens[0]
    #print(token)
    if token.value != ";":
        return
    tokens.pop(0)
    D(tokens)

def L(tokens):
    check(tokens)
    token = tokens.pop(0)
    #print(token)
    if token.type != "identificador":
        erro(token, 'identificador')
    inserir_TS(token)
    lista_token.append(token)
    X(tokens)

def X(tokens):
    check(tokens)
    token = tokens[0]
    #print(token)
    if token.value != ",":
        return
    tokens.pop(0)
    L(tokens)

def S(tokens):
    if not tokens:
        print("ERROR: Esperava-se 'id' ou 'if'")
        exit()
    token = tokens.pop(0)
    if token.type != 'identificador' and token.value != 'if':
        erro(token, 'erro idenficador')
    if token.type == 'identificador':

        busca=get_ts(token)
        tipo_esperado = busca.get("Tipo")
        token = tokens.pop(0)
        if busca == None:
            print("Erro:variável não declarada")
            exit()
        if token.value != ':=':
            erro(token, ':=')
        E(tokens)
    elif token.value == 'if':
        #print(token)
        E(tokens)

        if not tokens:
            print("Erro de sintaxe: linha {} | Esperado: then | Entrada: {}".format(token.index, ''))
            exit()
        token = tokens.pop(0)
        if token.value != 'then':
            erro(token, 'Palavra reservada')
        tipo_esperado=""
        S(tokens)

def E(tokens):
    check(tokens)
    T(tokens)
    R(tokens)

def T(tokens):
    global tipo_esperado
    check(tokens)
    token = tokens.pop(0)
    if token.type != 'identificador':
        erro(token, 'idenficador')
    busca = get_ts(token)

    if busca == None:
        print("Erro:variável não declarada")
        exit()
    if (tipo_esperado == ""):
        tipo_esperado = busca.get("Tipo")
    else:
        tipo_atual = busca.get("Tipo")
        if (not tipo_esperado == tipo_atual):
            print("Tipo de varíavel incompatível, esperava-se tipo: %s, variavel: %s" \
                            % (tipo_esperado,token.value))
            exit()


def R(tokens):
    if not tokens:
        return
    token = tokens[0]

    if token.value != '+':
        return

    token = tokens.pop(0)
    T(tokens)
    R(tokens)