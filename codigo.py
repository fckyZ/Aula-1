# Passo a passo 
#pip install pyautogui  
import pyautogui
import time 
import pandas
# Comandos pyautogui; 
# clicar -> pyautogui.click
# escrever -> pyautogui.write 
# aperta uma tecla -> pyautogui.press
# apertar atalho -> pyautogui.hotkey("","")
# scroll (rolar) -> pyautogui.scroll()




# Etapa 1: Entrar no sistema da empresa. 
## 
# aperta a tecla do windows 
# escrever o nome do aplicativo 
# clicar no aplicativo 
# digitar o link
# apertar enter
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 1 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
# Etapa 2: Fazer login.
pyautogui.click(x=415, y=370)
# digitar o email
pyautogui.write("olabomdia")
# clicar no campo de senha
pyautogui.press("tab")
# colocar a senha
pyautogui.write("123456")
# campo de avançar
pyautogui.press("tab")
pyautogui.click(x=677, y=535)
## x=677, y=535 
time.sleep(3)
# Etapa 3: Importar base de dados.
## pip install pandas numpy openpyx 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # Etapa 4: Cadastrar um produto.
    pyautogui.click(x=462, y=258)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #  "1"
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(550)

# Etapa 5: Repetir isso até a base de dados acabar.


