__all__ = [ 'inicializar', 'finalizar', 'get_aluno', 'add_aluno', 'set_horario' ]

import json

# Aluno:
#   id: int,
#   nome: str,
#   filial_pref: int,
#   horario_pref: list[ini: int, fim: int]

alunos = []
PATH = 'data/aluno.json'

# Códigos de erro
OPERACAO_REALIZADA_COM_SUCESSO = 0

ARQUIVO_NAO_ENCONTRADO = 1
ARQUIVO_EM_FORMATO_INVALIDO = 2
ERRO_NA_ESCRITA_DO_ARQUIVO = 3

ALUNO_NAO_ENCONTRADO = 4

def inicializar() -> int:
    global alunos

    try:
        with open(PATH, 'r') as arquivo:
            try:
                alunos = json.load(arquivo)
            except json.JSONDecodeError: return ARQUIVO_EM_FORMATO_INVALIDO
    except FileNotFoundError: return ARQUIVO_NAO_ENCONTRADO

    return OPERACAO_REALIZADA_COM_SUCESSO

def finalizar() -> int:
    try:
        with open(PATH, 'w') as arquivo:
            json.dump(obj = alunos, fp = arquivo, indent = 4)
    except OSError: return ERRO_NA_ESCRITA_DO_ARQUIVO

    return OPERACAO_REALIZADA_COM_SUCESSO

def get_aluno(id_aluno: int) -> tuple[int, dict]:
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            return OPERACAO_REALIZADA_COM_SUCESSO, aluno

    return ALUNO_NAO_ENCONTRADO, {} # Aluno não encontrado

def add_aluno(nome: str, bairro: str, horario: list[int]) -> tuple[int, int]:
    id = len(alunos)

    alunos.append({
        'id': id,
        'nome': nome,
        'filial_pref': bairro,  # FIXME descobrir a filial a partir do bairro
        'horario': horario,
    })

    return OPERACAO_REALIZADA_COM_SUCESSO, id

def set_horario(id_aluno: int, horario_ini: int, horario_fim: int) -> int:
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            aluno['horario'] = [horario_ini, horario_fim]
            return OPERACAO_REALIZADA_COM_SUCESSO

    return ALUNO_NAO_ENCONTRADO
