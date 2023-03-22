"""
AAA - 3A - A3

Arrange - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_para_lowercase():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_para_retornar_um_erro_para_nota_inexistente():
    # Arrumar
    tonica = 'X'
    tonalidade = 'maior'
    mensagem_de_erro = f'Essa nota não existe, tente umas dessas {NOTAS}'

    # Act
    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    # Assert
    assert mensagem_de_erro == error.value.args[0]


def test_para_retornar_um_erro_para_escala_inexistente():
    # Arrumar
    tonica = 'c'
    tonalidade = 'tonalidade'
    mensagem_de_erro = (
        'Essa escala não existe ou nao foi implementada. '
        f'Tente umas dessas {list(ESCALAS.keys())}'
    )

    # Act
    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    # Assert
    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    # Arrumar
    'tonica,tonalidade,esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    # Act
    resultado = escala(tonica, tonalidade)

    # Assert
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
