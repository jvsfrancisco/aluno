# Como utilizar

No diretório imediatamente acima do seu módulo, execute:

`git clone https://github.com/jvsfrancisco/aluno`

Depois você pode utilizar as funções de turma com o import:

```Python
from .. import aluno

turma.get_aluno(12)
```

**OBS:** Para utilizar imports relativos, seu módulo também precisa fazer parte de um package, ou seja, o diretório do módulo deve possuir um arquivo `__init__.py` assim como o nosso.

Alternativamente, se o diretório acima do seu módulo também for um repositório, como o principal, você pode adicionar turma como submódulo:

`git submodule add https://github.com/jvsfrancisco/aluno`

## Dependências

Python 3.9+

# Documentação adicional

## add_aluno

Fução chamada para cadastrar um novo aluno na plataforma, dados a lista de horários de preferência do aluno, nome e o bairro;

```Python
aluno.add_aluno(
    "João",
    "Centro",
    [8,12]
)

```

## get_aluno

Função chamada para obter informações de um aluno a partir de um aluno_id

```Python
aluno.get_aluno(12)

#Retorno
{
    "nome": "João",
    "bairro": "Centro",
    "horarios": [8,12]
}

```

## set_horario

Função chamada para definir o horário de preferencia de um aluno

```Python
aluno.set_horario(12, [8,12])

```