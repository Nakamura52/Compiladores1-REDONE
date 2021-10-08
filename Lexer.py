from Syntax_Tabela import *

palavraReservada = ('var', 'integer', 'real', 'if', 'then')
terminais = (' ', '\t', '\n', ',', ':', ':=', '+', ',', ';', '=')
delimitador = (',', ':', ';')
operador = ('+', '-', ':=', '=')


class Token:
    def __init__(self, _value, _type, _index):
        self.type = _type
        self.value = _value
        self.index = _index

    def __str__(self):
        return "'{}' {} linha {}".format(self.value, self.type, self.index)

    __repr__ = __str__

def peek(l, ch):
    if len(l) - 1 > l.index(ch):
        return  l[l.index(ch)+1]
    return ch

def tokenizer(l, i):
    buf = ''
    tokens = []
    for ch in l:
        if ch in terminais:
            if buf:
                if buf == ':=':
                    tokens.append(Token(buf, "operador", i))
                    buf = ''
                    continue
                if buf in palavraReservada:
                   tokens.append(Token(buf, "reservada" , i))
                elif buf in delimitador:
                    tokens.append(Token(buf, "delimitador", i))
                elif buf in operador:
                    tokens.append(Token(buf, "operador", i))
                elif buf.isalpha():
                    tokens.append(Token(buf, 'identificador', i))
                else:
                    tokens.append(Token(buf, 'invalido', i))

                buf = ''
            if ch == ':' and peek(l, ch) == '=':
                buf = ':='
            elif ch in delimitador:
                tokens.append(Token(ch, 'delimitador', i))
            elif ch in operador:
                tokens.append(Token(ch, 'operador', i))
        else:
            buf+= ch
    else:
        if buf in palavraReservada:
            tokens.append(Token(buf, "reservada", i))
        elif buf in delimitador:
            tokens.append(Token(buf, "delimitador", i))
        elif buf in operador:
            tokens.append(Token(buf, "operador", i))
        elif buf.isalpha():
            tokens.append(Token(buf, 'identificador', i))
        elif buf:
            tokens.append(Token(buf, 'invalido', i))

        buf = ''
    return tokens

if __name__ == '__main__':
    with open('archivetest.txt','r') as arq:
        tokens = []
        for i, l in enumerate(arq):
            tokens.append(tokenizer(l, i))
        for x in range(len(tokens)):
            print (tokens[x])
        juntalinha = []
        for linha in tokens:
            juntalinha += linha
            #print('TESTE', juntalinha)
        Z(juntalinha)
        print(' \n Cadeia aceita')