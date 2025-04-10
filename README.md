# ️ Automação de Cadastro de Produtos com PyAutoGUI

Este projeto é um teste de automação com Python usando a biblioteca [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/), com o objetivo de simular o cadastro automático de produtos em um formulário web.

> ⚠️ **Atenção:** O site utilizado neste projeto é apenas para fins de aprendizado/teste. Qualquer e-mail e senha podem ser utilizados para simular o login.

---

##  O que o script faz

1.  Abre o navegador (Chrome).
2.  Acessa a página de login da [Hashtag Treinamentos (Intensivão)](https://dlp.hashtagtreinamentos.com/python/intensivao/login).
3.  Faz o login com e-mail e senha fictícios.
4.  Lê uma base de dados `produtos.csv`.
5.  Preenche e envia o formulário de cadastro de produtos automaticamente.

---

##  Pré-requisitos

-   Python 3.10+ instalado
-   Instale os pacotes necessários:

    ```bash
    pip install pyautogui pandas
    ```

## Estrutura esperada

```bash
.
├── main.py       # Arquivo principal de automação
├── auxiliar.py    # Arquivo auxiliar para testes de métodos
└── produtos.csv   # Base de dados fictícia
Dicas importantes
Segurança
Use pyautogui.FAILSAFE = True para poder interromper a automação se algo der errado (basta mover o mouse para o canto da tela).

⏱️ Pausas
Adicione pausas automáticas com pyautogui.PAUSE = 0.5 para evitar cliques rápidos demais.

Posicionamento
Use pyautogui.click(x, y) para posicionar o foco corretamente no início do formulário.

Logs
Adicione logs para saber em qual linha a automação está:

Python

print(f"Cadastrando produto {linha + 1}/{len(tabela)}: {codigo}")
❗ Tratamento de Erros
Adicione try/except para capturar erros durante o preenchimento:

Python

try:
    # código de preenchimento
except Exception as e:
    print(f"Erro na linha {linha}: {e}")
✅ Resultado
A automação preenche todo o formulário com os dados da planilha .csv e envia os cadastros um por um, voltando para o topo da página a cada cadastro.
