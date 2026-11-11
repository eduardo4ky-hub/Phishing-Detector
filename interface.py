
import customtkinter as ctk
from analisador import analisar_url


# =====================================
# CONFIGURAÇÕES DA INTERFACE
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Phishing Detector | Segurança Digital")
janela.geometry("950x700")
janela.minsize(800, 600)
janela.configure(fg_color="#0B1120")


# =====================================
# FUNÇÃO DO BOTÃO ANALISAR
# =====================================

def executar_analise():

    url = campo_url.get().strip()

    caixa_resultado.configure(state="normal")
    caixa_resultado.delete("1.0", "end")

    if not url:
        status.configure(
            text="Digite uma URL para começar!",
            text_color="#F59E0B"
        )

        caixa_resultado.insert(
            "end",
            "Nenhuma URL foi informada."
        )

        caixa_resultado.configure(state="disabled")
        return

    # Chama a função que está no arquivo analisador.py
    pontuacao, resultados = analisar_url(url)

    # Verifica se a URL é inválida
    if pontuacao is None:

        status.configure(
            text="URL inválida",
            text_color="#F87171"
        )

        caixa_resultado.insert("end", resultados[0])
        caixa_resultado.configure(state="disabled")
        return

    # Exibe os resultados
    caixa_resultado.insert(
        "end",
        "RESULTADOS DA ANÁLISE\n"
    )

    caixa_resultado.insert(
        "end",
        "-" * 40 + "\n\n"
    )

    for item in resultados:
        caixa_resultado.insert(
            "end",
            "• " + item + "\n\n"
        )

    caixa_resultado.insert(
        "end",
        f"\nPontuação de risco: {pontuacao}\n"
    )

    # Define o status conforme a pontuação
    if pontuacao >= 3:

        status.configure(
            text="ALERTA: Muitos sinais suspeitos!",
            text_color="#F87171"
        )

    elif pontuacao >= 1:

        status.configure(
            text="ATENÇÃO: Sinais suspeitos encontrados.",
            text_color="#FBBF24"
        )

    else:

        status.configure(
            text="Nenhum sinal suspeito encontrado.",
            text_color="#4ADE80"
        )

    # Aviso de segurança
    caixa_resultado.insert(
        "end",
        "\nObservação: esta ferramenta identifica indícios, "
        "não confirma se um site é malicioso ou seguro."
    )

    caixa_resultado.configure(state="disabled")


# =====================================
# MONTAGEM DA INTERFACE
# =====================================

# Cabeçalho

titulo = ctk.CTkLabel(
    janela,
    text="🛡 PHISHING DETECTOR",
    font=("Arial", 30, "bold"),
    text_color="#FFFFFF"
)

titulo.pack(pady=(40, 5))


subtitulo = ctk.CTkLabel(
    janela,
    text="Analisador de URLs e possíveis ameaças digitais",
    font=("Arial", 14),
    text_color="#94A3B8"
)

subtitulo.pack(pady=(0, 30))


# =====================================
# CARTÃO PRINCIPAL
# =====================================

cartao = ctk.CTkFrame(
    janela,
    width=750,
    height=180,
    fg_color="#172238",
    corner_radius=18
)

cartao.pack(padx=40, fill="x")
cartao.pack_propagate(False)


texto_url = ctk.CTkLabel(
    cartao,
    text="DIGITE A URL QUE DESEJA ANALISAR",
    font=("Arial", 13, "bold"),
    text_color="#CBD5E1"
)

texto_url.pack(pady=(25, 10))


campo_url = ctk.CTkEntry(
    cartao,
    width=600,
    height=45,
    corner_radius=10,
    placeholder_text="Exemplo: https://www.exemplo.com",
    font=("Arial", 13)
)

campo_url.pack(pady=5)


botao = ctk.CTkButton(
    cartao,
    text="🔍 ANALISAR URL",
    width=220,
    height=42,
    corner_radius=10,
    font=("Arial", 13, "bold"),
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    command=executar_analise
)

botao.pack(pady=12)


# =====================================
# STATUS DA ANÁLISE
# =====================================

status = ctk.CTkLabel(
    janela,
    text="Aguardando análise...",
    font=("Arial", 17, "bold"),
    text_color="#94A3B8"
)

status.pack(pady=25)


# =====================================
# ÁREA DE RESULTADOS
# =====================================

painel_resultado = ctk.CTkFrame(
    janela,
    fg_color="#172238",
    corner_radius=15
)

painel_resultado.pack(
    padx=40,
    pady=5,
    fill="both",
    expand=True
)


titulo_resultado = ctk.CTkLabel(
    painel_resultado,
    text="RELATÓRIO DE SEGURANÇA",
    font=("Arial", 15, "bold"),
    text_color="#FFFFFF"
)

titulo_resultado.pack(pady=(20, 10))


caixa_resultado = ctk.CTkTextbox(
    painel_resultado,
    width=700,
    height=200,
    fg_color="#0F172A",
    text_color="#E2E8F0",
    corner_radius=10,
    font=("Consolas", 12),
    wrap="word"
)

caixa_resultado.pack(
    padx=20,
    pady=(0, 20),
    fill="both",
    expand=True
)


caixa_resultado.insert(
    "end",
    "Seu relatório aparecerá aqui após a análise."
)

caixa_resultado.configure(state="disabled")


# =====================================
# RODAPÉ
# =====================================

rodape = ctk.CTkLabel(
    janela,
    text="Projeto acadêmico de Python | Phishing Detector",
    font=("Arial", 10),
    text_color="#64748B"
)

rodape.pack(pady=12)


# =====================================
# INICIAR A APLICAÇÃO
# =====================================

if __name__ == "__main__":
    janela.mainloop()
