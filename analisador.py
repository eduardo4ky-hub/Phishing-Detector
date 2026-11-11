
import ipaddress
from urllib.parse import urlparse


def normalizar_url(url):
    url = url.strip().lower()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def verificar_palavras(url):
    palavras_suspeitas = [
        "login",
        "senha",
        "banco",
        "premio",
        "premiação",
        "verificar",
        "seguranca",
        "atualizar",
        "urgente"
    ]

    encontradas = []

    for palavra in palavras_suspeitas:
        if palavra in url:
            encontradas.append(palavra)

    return encontradas


def verificar_tamanho(url):
    return len(url) > 100


def verificar_ip(host):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def analisar_url(url):
    url = normalizar_url(url)

    pontuacao = 0
    resultados = []

    partes = urlparse(url)
    host = partes.hostname

    if not host:
        return None, ["URL inválida ou sem domínio válido."]

    if verificar_palavras(url):
        palavras = verificar_palavras(url)
        pontuacao += 1
        resultados.append(
            "Palavras suspeitas: " + ", ".join(palavras)
        )

    if verificar_tamanho(url):
        pontuacao += 1
        resultados.append("URL muito longa.")

    if verificar_ip(host):
        pontuacao += 1
        resultados.append("Endereço IP utilizado diretamente.")

    if partes.scheme == "http":
        pontuacao += 1
        resultados.append("Utiliza HTTP em vez de HTTPS.")

    if "@" in partes.netloc:
        pontuacao += 1
        resultados.append("Caractere @ encontrado no endereço.")

    if not resultados:
        resultados.append("Nenhum sinal suspeito encontrado.")

    return pontuacao, resultados
