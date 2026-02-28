"""
Script para descobrir IDs e elementos do jogo PokeChill
Use este script para descobrir os seletores corretos para o bot
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

print("="*60)
print("🔍 DESCOBRIDOR DE IDS - POKECHILL")
print("="*60)
print("\nEste script vai te ajudar a descobrir os IDs dos elementos")
print("do jogo para configurar o bot corretamente.\n")
print("="*60)

# Pergunta como conectar
print("\nComo você quer abrir o navegador?")
print("1. Chrome (script abre automaticamente)")
print("2. Brave (script abre automaticamente)")
print("3. Conectar ao navegador já aberto (debug mode)")

escolha = input("\nEscolha (1/2/3): ").strip()

driver = None

try:
    if escolha == "3":
        print("\n⚠️ Certifique-se que o navegador foi aberto com:")
        print("   chrome.exe --remote-debugging-port=9222")
        print("   OU")
        print('   "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --remote-debugging-port=9222')
        print()
        input("Aperte ENTER para continuar...")
        
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=chrome_options)
        print("✅ Conectado ao navegador!")
    elif escolha == "2":
        print("\n🚀 Abrindo Brave...")
        brave_options = Options()
        brave_paths = [
            "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
        ]
        
        brave_path = None
        for path in brave_paths:
            if os.path.exists(path):
                brave_path = path
                break
        
        if brave_path:
            brave_options.binary_location = brave_path
            driver = webdriver.Chrome(options=brave_options)
        else:
            print("⚠️ Brave não encontrado, usando Chrome...")
            driver = webdriver.Chrome()
        
        driver.maximize_window()
        driver.get("https://play-pokechill.github.io")
        print("✅ Navegador aberto!")
        print("\n⏳ Faça login se necessário...")
        input("Aperte ENTER quando estiver no jogo...")
    else:
        print("\n🚀 Abrindo Chrome...")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://play-pokechill.github.io")
        print("✅ Chrome aberto!")
        print("\n⏳ Faça login se necessário...")
        input("Aperte ENTER quando estiver no jogo...")

    print("\n" + "="*60)
    print("📋 INSTRUÇÕES:")
    print("="*60)
    print("1. Navegue até a tela que você quer investigar")
    print("2. Aperte ENTER aqui para ver todos os elementos")
    print("3. Anote os IDs que você precisa")
    print("="*60)
    input("\nAPERTE ENTER quando estiver pronto... ")

    print("\n" + "="*60)
    print("🔍 PROCURANDO ELEMENTOS...")
    print("="*60)

    # Botões
    print("\n📍 BOTÕES ENCONTRADOS:")
    print("-"*60)
    botoes = driver.find_elements(By.TAG_NAME, "button")
    for i, btn in enumerate(botoes[:30], 1):  # Limita a 30 para não poluir
        try:
            txt = btn.text[:30] if btn.text else "(sem texto)"
            id_btn = btn.get_attribute("id") or "(sem id)"
            class_btn = btn.get_attribute("class") or "(sem class)"
            visible = btn.is_displayed()
            print(f"{i}. Texto: '{txt}' | ID: '{id_btn}' | Class: '{class_btn}' | Visível: {visible}")
        except:
            pass

    # Divs importantes
    print("\n\n📍 DIVS IMPORTANTES:")
    print("-"*60)
    divs = driver.find_elements(By.TAG_NAME, "div")
    divs_com_id = [d for d in divs if d.get_attribute("id")][:20]
    for i, div in enumerate(divs_com_id, 1):
        try:
            id_div = div.get_attribute("id")
            class_div = div.get_attribute("class") or "(sem class)"
            visible = div.is_displayed()
            print(f"{i}. ID: '{id_div}' | Class: '{class_div}' | Visível: {visible}")
        except:
            pass

    # Imagens
    print("\n\n📍 IMAGENS (Pokémon, sprites, etc):")
    print("-"*60)
    imgs = driver.find_elements(By.TAG_NAME, "img")
    for i, img in enumerate(imgs[:15], 1):
        try:
            id_img = img.get_attribute("id") or "(sem id)"
            src = img.get_attribute("src") or ""
            alt = img.get_attribute("alt") or "(sem alt)"
            visible = img.is_displayed()
            print(f"{i}. ID: '{id_img}' | Alt: '{alt}' | Src: ...{src[-30:]} | Visível: {visible}")
        except:
            pass

    # Procura por preview teams especificamente
    print("\n\n📍 PROCURANDO TIMES (preview1 a preview30):")
    print("-"*60)
    times_encontrados = []
    for i in range(1, 31):
        try:
            preview_id = f"preview{i}"
            element = driver.find_element(By.ID, preview_id)
            times_encontrados.append(i)
            print(f"✅ Time {i} encontrado (ID: {preview_id})")
        except:
            try:
                # Tenta outras variações
                element = driver.find_element(By.XPATH, f"//div[contains(@id, 'preview{i}')]")
                times_encontrados.append(i)
                print(f"✅ Time {i} encontrado (XPATH)")
            except:
                pass
    
    if not times_encontrados:
        print("⚠️ Nenhum time encontrado. Pode estar em outra tela.")
    else:
        print(f"\n📊 Total de times encontrados: {len(times_encontrados)}")

    # Procura por botões de batalha
    print("\n\n📍 PROCURANDO BOTÕES DE BATALHA:")
    print("-"*60)
    battle_keywords = ["battle", "fight", "start", "play", "luta", "batalha"]
    for keyword in battle_keywords:
        try:
            elements = driver.find_elements(By.XPATH, f"//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{keyword}')]")
            if elements:
                for elem in elements[:3]:
                    id_elem = elem.get_attribute("id") or "(sem id)"
                    txt = elem.text[:30] if elem.text else "(sem texto)"
                    print(f"✅ '{keyword}': ID='{id_elem}', Texto='{txt}'")
        except:
            pass

    print("\n" + "="*60)
    print("✅ ANÁLISE COMPLETA!")
    print("="*60)
    print("\nUse estas informações para atualizar o config.py")

except Exception as e:
    print(f"\n❌ Erro: {e}")
    import traceback
    traceback.print_exc()

finally:
    if driver:
        print("\n\nDeseja fechar o navegador? (s/n): ")
        try:
            if input().strip().lower() == 's':
                driver.quit()
                print("👋 Navegador fechado!")
            else:
                print("💡 Navegador mantido aberto. Feche manualmente quando terminar.")
        except:
            print("💡 Fechando navegador...")
            driver.quit()

print("\n" + "="*60)
print("Obrigado por usar o descobridor de IDs!")
print("="*60)
