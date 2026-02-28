"""
Script para testar conexão com o navegador
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("🔍 Testando conexão com o navegador...\n")

try:
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    
    # Usa webdriver-manager para baixar a versão correta
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    print("✅ CONEXÃO ESTABELECIDA!")
    print(f"📄 Página atual: {driver.title}")
    print(f"🔗 URL: {driver.current_url}\n")
    
    # Testa se é o jogo PokeChill
    if "pokechill" in driver.current_url.lower():
        print("✅ Está no jogo PokeChill!")
    else:
        print("⚠️ Não está no jogo PokeChill")
        print("   Navegue para: https://play-pokechill.github.io")
    
    driver.quit()
    
except Exception as e:
    print("❌ ERRO NA CONEXÃO!")
    print(f"   Detalhes: {e}\n")
    print("📝 SOLUÇÃO:")
    print("   1. Execute: abrir_brave.bat")
    print("   2. OU manualmente:")
    print('      "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --remote-debugging-port=9222')
    print()
