import os
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

HIST_FILE_PATH = os.getenv("HIST_FILE")


def carregar_dados():
    if not HIST_FILE_PATH:
        print("Erro: Variavel HIST_FILE nao definida no arquivo .env")
        return None

    caminho = Path(HIST_FILE_PATH)
    if not caminho.exists():
        print(f"Erro: Arquivo nao encontrado em '{caminho}'")
        return None

    lines = []
    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            cmd = (
                line.partition(";")[2].strip() if line.startswith(":") else line.strip()
            )
            if cmd:
                lines.append(cmd)

    df = pd.DataFrame(lines, columns=["comando_completo"])
    df["binario"] = df["comando_completo"].str.split().str[0]

    mask_sudo = df["binario"].isin(["sudo", "doas"]) & (
        df["comando_completo"].str.split().str.len() > 1
    )
    df.loc[mask_sudo, "binario"] = df["comando_completo"].str.split().str[1]

    return df


def analisar(df):
    total = len(df)
    top_binarios = df["binario"].value_counts().head(10)

    print(f"Total de comandos analisados: {total}")
    print("\nComandos mais utilizados:")
    for binario, count in top_binarios.items():
        pct = (count / total) * 100
        print(f"  {binario:<12} -> {count:>5} ({pct:>4.1f}%)")

    plt.style.use("ggplot")
    ax = top_binarios.plot(kind="barh", color="skyblue", edgecolor="black")
    ax.invert_yaxis()
    plt.title("\nComandos mais utilizados")
    plt.xlabel("Quantidade de Usos")
    plt.ylabel("Comando")
    plt.tight_layout()

    output_png = "uso_terminal.png"
    plt.savefig(output_png, dpi=300)
    print(f"\nGrafico salvo em: {output_png}")


if __name__ == "__main__":
    df = carregar_dados()
    if df is not None:
        analisar(df)
