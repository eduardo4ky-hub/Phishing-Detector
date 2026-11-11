
# 🛡️ Phishing Detector

Aplicação desenvolvida em Python para analisar URLs e identificar possíveis sinais de phishing, contribuindo para a conscientização sobre segurança digital.

## 📌 Sobre o projeto

O Phishing Detector é uma ferramenta que recebe uma URL informada pelo usuário e realiza uma análise baseada em características que podem indicar uma tentativa de phishing.

O sistema apresenta os resultados em uma interface gráfica, exibindo os possíveis sinais suspeitos encontrados e uma pontuação de risco.

**Importante:** a ferramenta identifica indícios suspeitos. Ela não confirma se um site é malicioso ou seguro.

## ⚙️ Funcionalidades

- Análise de URLs informadas pelo usuário.
- Identificação de palavras suspeitas.
- Verificação do tamanho da URL.
- Identificação de endereços IP utilizados diretamente.
- Verificação do uso de HTTP em vez de HTTPS.
- Identificação do caractere especial `@`.
- Sistema de pontuação de risco.
- Interface gráfica com apresentação dos resultados.

## 🧰 Tecnologias utilizadas

- Python
- CustomTkinter
- Biblioteca ipaddress
- Biblioteca urllib.parse

## 📂 Estrutura do projeto

```text
Phishing-Detector/
│
├── main.py
├── interface.py
├── analisador.py
├── teste.py
└── README.md
```

## ▶️ Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Visual Studio Code (opcional).
- Pip para instalação de bibliotecas.

### 2. Instalação da dependência

No terminal, execute:

```bash
py -m pip install customtkinter
```

### 3. Executar a aplicação

Entre na pasta do projeto e execute:

```bash
py main.py
```

## 🎯 Objetivo de aprendizado

Este projeto foi desenvolvido com o objetivo de praticar conceitos de programação em Python, incluindo:

- Variáveis e estruturas condicionais.
- Funções e modularização.
- Manipulação de strings.
- Tratamento de informações.
- Bibliotecas nativas do Python.
- Desenvolvimento de interfaces gráficas.

## 👨‍💻 Autor

Projeto desenvolvido por Eduardo Alves, parte dos meus estudos em Sistemas de Informação, com foco em Python e Segurança da Informação.
