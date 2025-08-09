# tgit
Tgit is a github repository that comes with the promise of installing all the basic termux dependency packages to facilitate its installation, only needing to install git and cmake and clang
ex:
pkg install git clang cmake make -y

git clone https://github.com/pedromarsan06/tgit.git

cd tgit

chmod +x install.sh or bash install.sh
#If you used bash you don't necessarily have to use ./install.sh it will give an error

./install.sh 

python3 main.py

###"main.py Description

This script provides a simple, user-friendly ASCII terminal menu for installing essential packages on Termux or similar Linux environments. It uses only Python’s built-in libraries (no external dependencies), making it lightweight and easy to run.

Key features:

Interactive ASCII menu:
Presents a clean, text-based menu listing installation options such as installing requests, basic build tools (git, clang, perl, wget, curl), virtualenv, and more.

User input handling:
Accepts numeric input to select options and validates entries, prompting again if invalid.

Runs shell commands:
Executes system package manager commands (pkg install ...) and Python package installs (pip install ...) directly through Python’s os.system().

Loop until exit:
The menu repeats after each action, allowing multiple installations in one session, with an option to quit gracefully.

Clear screen and formatting:
Clears the terminal before showing the menu to keep the interface clean and uses simple ASCII formatting for readability.
---

How to Use

When you run the script (python main.py), you will see a menu with options numbered from 0 to 5 (or more).

To select an option:
Type the number corresponding to the desired action and press Enter.

Options and their functions:


Option	What to type	What it does

1	1	Installs the Python package requests via pip.
2	2	Installs basic build tools (git, clang, perl, wget, curl) using pkg. These are needed to compile some Python packages.
3	3	Installs virtualenv via pip, useful for creating isolated Python environments.
4	4	Installs a small set of basic packages (nano, clang, curl, wget, python) for editing and downloading files.
5	5	Installs all build tools and Python dependencies listed in requirements.txt by running pkg install commands and pip install -r requirements.txt.
0	0	Exits the script gracefully.


If you type an invalid number or a non-numeric input, the script will notify you and prompt again.
---
Purpose:
The script simplifies environment setup by grouping common installation commands into an easy menu, especially useful for Termux users who want to quickly install essential Python packages and development tools without manually typing commands.



---

Purpose:
The script simplifies environment setup by grouping common installation commands into an easy menu, especially useful for Termux users who want to quickly install essential Python packages and development tools without manually typing commands.



---

How to Use

When you run the script (python main.py), you will see a menu with options numbered from 0 to 5 (or more).

To select an option:
Type the number corresponding to the desired action and press Enter.

Options and their functions:


Option	What to type	What it does

1	1	Installs the Python package requests via pip.
2	2	Installs basic build tools (git, clang, perl, wget, curl) using pkg. These are needed to compile some Python packages.
3	3	Installs virtualenv via pip, useful for creating isolated Python environments.
4	4	Installs a small set of basic packages (nano, clang, curl, wget, python) for editing and downloading files.
5	5	Installs all build tools and Python dependencies listed in requirements.txt by running pkg install commands and pip install -r requirements.txt.
0	0	Exits the script gracefully.


If you type an invalid number or a non-numeric input, the script will notify you and prompt again.



---

Purpose:
The script simplifies environment setup by grouping common installation commands into an easy menu, especially useful for Termux users who want to quickly install essential Python packages and development tools without manually typing commands.


#Portugues:
# tgit
O Tgit é um repositório do GitHub que vem com a promessa de instalar todos os pacotes básicos de dependências do Termux para facilitar sua instalação, sendo necessário apenas instalar o Git, o CMake e o Clang.
ex:
##pkg install git clang cmake make -y

##git clone https://github.com/pedromarsan06/tgit.git

##cd tgit

##chmod +x install.sh ou bash install.sh

#Se você usou o bash, não precisa necessariamente usar ./install.sh, pois isso dará um erro pois não foi feito o chmod +x install.sh 

##./install.sh
python3 main.py


---

Descrição do main.py

Este script fornece um menu simples e amigável em ASCII para terminal, que facilita a instalação de pacotes essenciais no Termux ou ambientes Linux semelhantes. Ele utiliza apenas bibliotecas internas do Python (sem dependências externas), tornando-o leve e fácil de executar.

Principais funcionalidades:

Menu ASCII interativo:
Exibe um menu limpo em texto, listando opções de instalação como o pacote requests, ferramentas básicas de compilação (git, clang, perl, wget, curl), virtualenv e outras.

Tratamento de entrada do usuário:
Aceita entrada numérica para seleção de opções, valida a entrada e pede para tentar novamente caso o valor seja inválido.

Execução de comandos no shell:
Executa comandos do gerenciador de pacotes do sistema (pkg install ...) e instala pacotes Python via pip (pip install ...) usando o os.system() do Python.

Loop até sair:
O menu repete após cada ação, permitindo instalar várias coisas numa mesma sessão, com opção de sair de forma limpa.

Limpa a tela e formata a saída:
O terminal é limpo antes de mostrar o menu para manter a interface organizada, e a formatação ASCII simples melhora a legibilidade.



---

Como usar

Ao rodar o script (python main.py), você verá um menu com opções numeradas de 0 a 5 (ou mais).

Para escolher uma opção:
Digite o número da ação desejada e pressione Enter.

Opções e o que fazem:


Opção	O que digitar	O que faz

1	1	Instala o pacote Python requests via pip.
2	2	Instala ferramentas básicas de compilação (git, clang, perl, wget, curl) usando o pkg. Necessárias para compilar alguns pacotes Python.
3	3	Instala o virtualenv via pip, útil para criar ambientes Python isolados.
4	4	Instala um conjunto pequeno de pacotes básicos (nano, clang, curl, wget, python) para edição e download de arquivos.
5	5	Instala todas as ferramentas de build e dependências Python listadas no requirements.txt, executando os comandos pkg install e pip install -r requirements.txt.
0	0	Sai do script de forma limpa.


Se você digitar um número inválido ou algo que não seja número, o script vai avisar e pedir para tentar novamente.



---

Objetivo:
Este script simplifica a configuração do ambiente ao agrupar comandos comuns de instalação em um menu fácil de usar, especialmente para usuários do Termux que querem instalar rapidamente pacotes Python essenciais e ferramentas de desenvolvimento sem precisar digitar tudo manualmente.


---


