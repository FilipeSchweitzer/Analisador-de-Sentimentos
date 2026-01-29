import pytest
from process import ProcessadorTexto

@pytest.fixture
def processador():
    """Fixture para inicializar o processador uma única vez para os testes."""
    return ProcessadorTexto()

def test_conversao_minusculas(processador):
    texto = "PRODUTO EXCELENTE"
    esperado = "produto excelente" # Note: 'excelente' pode mudar se houver lemmatização
    assert "produto" in processador.limpar(texto)

def test_remocao_urls(processador):
    texto = "Confira em http://site.com o meu comentário"
    resultado = processador.limpar(texto)
    assert "http" not in resultado
    assert "site" not in resultado

def test_remocao_mencoes(processador):
    texto = "Olá @usuario, gostei muito!"
    resultado = processador.limpar(texto)
    assert "@usuario" not in resultado

def test_remocao_stopwords(processador):
    # 'o', 'a', 'de' são stopwords e devem sumir
    texto = "O produto de qualidade"
    resultado = processador.limpar(texto)
    assert "produto" in resultado
    assert " de " not in f" {resultado} "

def test_texto_vazio(processador):
    assert processador.limpar("") == ""

def test_caracteres_especiais(processador):
    texto = "Bom!!! Incrível... 123"
    resultado = processador.limpar(texto)
    # Deve sobrar apenas as palavras
    assert "bom" in resultado
    assert "incrível" in resultado
    assert "123" not in resultado

def test_limpar_lote_consistencia(processador):
    """Verifica se o resultado do lote é igual ao individual."""
    frases = [
        "O produto é excelente!",
        "Chegou muito rápido @vendedor",
        "Amei o atendimento 😊"
    ]
    
    # Processa individualmente
    esperados = [processador.limpar(f) for f in frases]
    # Processa em lote
    resultados = processador.limpar_lote(frases)
    
    assert resultados == esperados
    assert len(resultados) == 3

def test_limpar_lote_vazio_e_nulo(processador):
    """Testa como o lote lida com listas vazias ou entradas estranhas."""
    lista_complicada = ["", " ", "!!!", "12345"]
    resultados = processador.limpar_lote(lista_complicada)
    
    # Esperamos uma lista de strings vazias (já que os tokens foram filtrados)
    for r in resultados:
        assert r == ""

def test_limpar_lote_preservacao_ordem(processador):
    """Garante que o pipe não embaralhou as frases."""
    lista = ["Primeira frase", "Segunda frase", "Terceira frase"]
    resultados = processador.limpar_lote(lista)
    
    assert "primeiro" in resultados[0] or "primeira" in resultados[0]
    assert "segundo" in resultados[1] or "segunda" in resultados[1]
    assert "terceiro" in resultados[2] or "terceira" in resultados[2]

def test_limpar_lote_grande_volume(processador):
    """Verifica se o lote aguenta uma carga maior de dados."""
    grande_lista = ["Produto bom"] * 100
    resultados = processador.limpar_lote(grande_lista)
    
    assert len(resultados) == 100
    assert all(r == "produto bom" or "bom" in r for r in resultados)