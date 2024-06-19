import unittest
from aluno import *

# Códigos de erro
OPERACAO_REALIZADA_COM_SUCESSO = 0

ARQUIVO_NAO_ENCONTRADO = 30
ARQUIVO_EM_FORMATO_INVALIDO = 31
ERRO_NA_ESCRITA_DO_ARQUIVO = 32

ALUNO_NAO_ENCONTRADO = 16

class TesteFuncoesAluno(unittest.TestCase):
    def teste_add_aluno(self):
        resultado, id = add_aluno('Joao', 'Gavea', [8, 12])
        self.assertEqual(resultado, 0)
        self.assertEqual(
            get_aluno(id),
            (OPERACAO_REALIZADA_COM_SUCESSO, {'id': id, 'nome': 'Joao', 'filial_pref': 2, 'horario': [8, 12]})
        )

    def teste_get_aluno(self):
        resultado, id = add_aluno('Maria', 'Gavea', [10, 14])
        self.assertEqual(resultado, 0)
        self.assertEqual(
            get_aluno(id),
            (OPERACAO_REALIZADA_COM_SUCESSO, {'id': id, 'nome': 'Maria', 'filial_pref': 2, 'horario': [10, 14]})
        )

    def teste_get_aluno_nao_encontrado(self):
        resultado, aluno = get_aluno(-1)
        self.assertEqual(resultado, ALUNO_NAO_ENCONTRADO)

    def teste_set_horario(self):
        resultado, id = add_aluno('Jose', 'Gavea', [8, 12])
        set_horario(id, 10, 12)
        self.assertEqual(
            get_aluno(id),
            (OPERACAO_REALIZADA_COM_SUCESSO,{'id': id, 'nome': 'Jose', 'filial_pref': 2, 'horario': [10, 12]})
        )

    def teste_set_horario_aluno_nao_encontrado(self):
        resultado = set_horario(-1, 10, 12)
        self.assertEqual(resultado, ALUNO_NAO_ENCONTRADO)

if __name__ == '__main__':
    unittest.main()
