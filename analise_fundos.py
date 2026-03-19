# =============================================================
# Análise de Fundos de Investimento — Dados Públicos CVM
# Autor: Ronaldo Nerozzi
# GitHub: github.com/ronaldo-nerozzi
# Descrição: Análise exploratória com Python e Pandas
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações visuais
sns.set_theme(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.family"] = "sans-serif"

# =============================================================
# 1. CARREGAR DADOS
# Fonte: Dados públicos CVM — https://dados.cvm.gov.br
# =============================================================

# Simulação de dados para demonstração
dados = {
    "tipo_fundo": ["Renda Fixa", "Ações", "Multimercado", "Cambial", "FII"],
    "total_fundos": [4520, 1830, 3210, 420, 980],
    "patrimonio_bilhoes": [1850.5, 420.3, 980.7, 85.2, 310.4],
    "media_cotistas": [1200, 850, 2100, 320, 4500],
}

df = pd.DataFrame(dados)

# =============================================================
# 2. VISÃO GERAL DOS DADOS
# =============================================================
print("=" * 55)
print("VISÃO GERAL — Fundos de Investimento Brasileiros")
print("=" * 55)
print(df.to_string(index=False))
print()
print(f"Total de tipos analisados : {len(df)}")
print(f"Total de fundos           : {df['total_fundos'].sum():,}")
print(f"Patrimônio total (R$ bi)  : {df['patrimonio_bilhoes'].sum():,.1f}")

# =============================================================
# 3. GRÁFICO 1 — Total de fundos por tipo
# =============================================================
fig, ax = plt.subplots()
bars = ax.barh(
    df["tipo_fundo"],
    df["total_fundos"],
    color=sns.color_palette("Blues_r", len(df))
)
ax.set_title("Total de Fundos por Tipo", fontsize=14, fontweight="bold")
ax.set_xlabel("Quantidade de Fundos")
ax.bar_label(bars, fmt="{:,.0f}", padding=4)
plt.tight_layout()
plt.savefig("01_total_fundos_por_tipo.png", dpi=150)
plt.show()
print("Gráfico salvo: 01_total_fundos_por_tipo.png")

# =============================================================
# 4. GRÁFICO 2 — Patrimônio líquido por tipo de fundo
# =============================================================
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    df["patrimonio_bilhoes"],
    labels=df["tipo_fundo"],
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2"),
    startangle=140
)
ax.set_title("Distribuição do Patrimônio Líquido por Tipo", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("02_patrimonio_por_tipo.png", dpi=150)
plt.show()
print("Gráfico salvo: 02_patrimonio_por_tipo.png")

# =============================================================
# 5. GRÁFICO 3 — Média de cotistas por tipo de fundo
# =============================================================
fig, ax = plt.subplots()
sns.barplot(
    data=df,
    x="tipo_fundo",
    y="media_cotistas",
    palette="muted",
    ax=ax
)
ax.set_title("Média de Cotistas por Tipo de Fundo", fontsize=14, fontweight="bold")
ax.set_xlabel("Tipo de Fundo")
ax.set_ylabel("Média de Cotistas")
plt.tight_layout()
plt.savefig("03_media_cotistas.png", dpi=150)
plt.show()
print("Gráfico salvo: 03_media_cotistas.png")

# =============================================================
# 6. ESTATÍSTICAS DESCRITIVAS
# =============================================================
print()
print("=" * 55)
print("ESTATÍSTICAS DESCRITIVAS")
print("=" * 55)
print(df[["total_fundos", "patrimonio_bilhoes", "media_cotistas"]].describe().round(2))
