# Estudos de Python — 2026

Repositório criado para reunir pequenos projetos desenvolvidos durante meus estudos de Python.

Atualmente, estou acompanhando o curso de Python do Curso em Vídeo, ministrado por Gustavo Guanabara, e utilizando este espaço para praticar lógica de programação, organização de código e bibliotecas do Python.

## Projetos

- Calculadora
- Calendário
- Hipotenusa
- MP3
- QR Code
- Gerador de senhas
- Gerenciador de Senhas Simples
- Tabuada
- Trigonometria

## 🚀 Projetos em Destaque

Uma seleção dos projetos mais completos e visuais deste repositório.

### 🔐 Gerenciador de Senhas Simples
Sistema de criação e confirmação de senha no terminal, com PIN de segurança: a senha é digitada de forma mascarada (`pwinput`) e só é revelada na tela se o usuário informar corretamente o PIN de 4 dígitos criado no início. Inclui banner ASCII (`pyfiglet`) e tratamento de interrupção do usuário (`KeyboardInterrupt`).
**Tecnologias:** `pyfiglet`, `pwinput`, `time.sleep`, tratamento de exceções

### 🔑 Gerador de Senhas Seguras
Gerador de senhas aleatórias e criptograficamente seguras usando `secrets.token_hex()`, que produz uma sequência hexadecimal de 16 caracteres.
**Tecnologias:** `secrets`, `time.sleep`

### 🧮 Calculadora
Calculadora de terminal com 7 operações (soma, subtração, multiplicação, divisão, potenciação, divisão inteira e módulo), usando `match/case` para selecionar a operação. Trata erros de entrada inválida, divisão por zero e interrupção pelo usuário.
**Tecnologias:** `pyfiglet`, `match/case`, tratamento de exceções (`ValueError`, `ZeroDivisionError`, `KeyboardInterrupt`)

### 📱 QR Code
Gera uma imagem de QR Code a partir de um link digitado pelo usuário, salva o arquivo como PNG e abre automaticamente no visualizador padrão do sistema.
**Tecnologias:** `qrcode`

### 🎵 Player de MP3
Player de áudio de terminal com controle interativo em tempo real: carrega um arquivo de música e permite pausar, retomar e parar a reprodução via comandos digitados, com tratamento de erro para arquivos inválidos.
**Tecnologias:** `pygame.mixer`

---

*Cada projeto está disponível na pasta `/projetos` deste repositório, com o código-fonte comentado.*

## Tecnologias e conceitos praticados

- Python
- Variáveis e tipos de dados
- Estruturas condicionais: `if`, `elif` e `else`
- Laços de repetição: `while`
- Tratamento de exceções: `try` e `except`
- Funções e módulos
- Bibliotecas como `pygame`, `pyfiglet`, `pwinput` e `secrets`

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/tturwcode/python-estudos-2026.git
```


2. Instale as dependências:
```
pip install -r requirements.txt
```


3. Entre na pasta de um projeto:
```
cd projetos/nome_do_projeto
```


4. Execute o arquivo desejado:
```
python nome_do_projeto.py
```

## Objetivo

Este repositório registra minha evolução nos estudos de programação. Novos exercícios e projetos serão adicionados conforme eu avanço no curso e desenvolvo minhas habilidades.
