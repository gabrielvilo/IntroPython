import platform
import subprocess

def nome_so():
    return platform.system()

def calcular_media_ping():
    so = nome_so()

    if so == "Windows":
        comando = ["ping", "-4", "-n", "10", "www.google.com.br"]
    else:
        comando = ["ping", "-4", "-c", "10", "www.google.com.br"]

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="latin-1"
    )

    linhas = resultado.stdout.split("\n")

    for linha in linhas[::-1]:

        if "=" in linha and "ms" in linha and "," in linha:
            partes = linha.split("=")
            return partes[-1].strip()

        elif "min/avg" in linha or "rtt" in linha:
            linha = linha.split("=")[1].strip()
            valores = linha.split(" ")[0]
            partes = valores.split("/")
            return partes[1] + " ms"

    return "Não encontrada"

def main():
    so = nome_so()
    media = calcular_media_ping()

    print("SO:", so)
    print("Média:", media)

if __name__ == "__main__":
    main()