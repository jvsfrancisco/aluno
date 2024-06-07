from aluno import *

# TODO converter pra unit tests

inicializar()

resultado, id = add_aluno('João', 'Centro', [8, 12])
print(resultado, id)
print(get_aluno(id))
print(set_horario(id, 10, 12))
print(get_aluno(id))

finalizar()
