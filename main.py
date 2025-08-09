import os
import time

# Comandos para cada opção
pakpage = {
    1: ("Instalar requests", "pip install requests"),
    2: ("Instalar pacotes básicos de build", "pkg install git clang perl wget curl -y"),
    3: ("Instalar virtualenv", "pip install virtualenv"),
    4: ("Instalar pacotes básicos pequenos", "pkg install nano clang curl wget python -y"),
    5: ("Instalar tudo + requirements.txt", "pkg install git clang perl wget curl -y && pip install -r requirements.txt"),
    0: ("Sair", None)
}

# Função para desenhar painel ASCII
def painel():
    os.system("clear")
    print("=" * 50)
    print("     🚀 INSTALADOR DE PACOTES - TERMINAL ASCII 🚀")
    print("=" * 50)
    for num, (desc, _) in pakpage.items():
        print(f" [{num}] {desc}")
    print("=" * 50)

# Loop principal
while True:
    painel()
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha not in pakpage:
            print("⚠ Opção inválida!")
            time.sleep(1.5)
            continue

        if escolha == 0:
            print("Saindo... 👋")
            break

        comando = pakpage[escolha][1]
        print(f"\n📦 Executando: {comando}\n")
        os.system(comando)
        input("\n✅ Pressione ENTER para voltar ao menu...")
    except ValueError:
        print("⚠ Digite apenas números!")
        time.sleep(1.5)
