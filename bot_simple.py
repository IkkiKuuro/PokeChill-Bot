"""
Bot PokeChill - Versão Simplificada
Baseado no código fonte do jogo
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


class PokeChillBot:
    def __init__(self, team_number=1):
        """
        Inicializa o bot
        
        Args:
            team_number: Número do time (1 a 30)
        """
        self.driver = None
        self.team_number = team_number
        self.battles_count = 0
        
    def log(self, message):
        """Log com timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
        
    def connect_to_browser(self):
        """Conecta ao navegador (Chrome ou Brave)"""
        print("\n" + "="*60)
        print("🌐 COMO USAR:")
        print("="*60)
        print("1. Abra o jogo no navegador (Chrome ou Brave)")
        print("2. Faça login se necessário")
        print("3. ENTRE EM UMA ÁREA/BATALHA no jogo")
        print("4. Deixe o jogo rodando")
        print("="*60)
        input("\n✅ Depois que entrar na batalha, APERTE ENTER aqui... ")
        
        print("\n🔍 Tentando conectar ao navegador...")
        
        # Tenta conectar ao navegador com debug
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            
            # Usa webdriver-manager para baixar a versão correta do ChromeDriver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            print("✅ Conectado!")
            return True
        except:
            print("\n⚠️ Não conseguiu conectar ao navegador.")
            print("\n📝 INSTRUÇÕES:")
            print("\n1. Feche TODOS os navegadores")
            print("2. Abra o cmd/terminal")
            print("3. Execute um destes comandos:\n")
            print("   BRAVE:")
            print('   "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --remote-debugging-port=9222\n')
            print("   CHROME:")
            print('   chrome.exe --remote-debugging-port=9222\n')
            print("4. Navegue para o jogo: https://play-pokechill.github.io")
            print("5. ENTRE EM UMA BATALHA")
            print("6. Execute o bot novamente")
            return False
    
    def execute_js(self, script):
        """Executa JavaScript no contexto do jogo"""
        return self.driver.execute_script(script)
    
    def is_in_combat(self):
        """Verifica se está em combate"""
        script = """
        const combatDiv = document.getElementById('explore-combat');
        return combatDiv && combatDiv.style.display !== 'none';
        """
        return self.execute_js(script)
    
    def has_lost_battle(self):
        """Verifica se perdeu (saiu do combate)"""
        return not self.is_in_combat()
    
    def click_rejoin(self):
        """Clica no botão area-rejoin para recomeçar"""
        try:
            # Usa JavaScript direto para clicar (mais confiável)
            script = """
            const btn = document.getElementById('area-rejoin');
            if (btn) {
                btn.click();
                return true;
            }
            return false;
            """
            clicked = self.execute_js(script)
            
            if clicked:
                self.log("✅ Clicou em 'Fight Again'")
                self.battles_count += 1
                return True
            else:
                # Fallback: tenta pelo Selenium
                element = self.driver.find_element(By.ID, "area-rejoin")
                element.click()
                self.log("✅ Clicou em 'Fight Again' (fallback)")
                self.battles_count += 1
                return True
        except Exception as e:
            self.log(f"❌ Erro ao clicar: {e}")
            return False
    
    def select_team(self):
        """Seleciona o time através do dropdown"""
        try:
            script = f"""
            const dropdown = document.getElementById('team-slot-selector');
            if (dropdown) {{
                dropdown.value = 'preview{self.team_number}';
                dropdown.dispatchEvent(new Event('change'));
                // Salva e sai do menu
                const exitBtn = document.getElementById('preview-team-exit');
                if (exitBtn) exitBtn.click();
                return true;
            }}
            return false;
            """
            
            result = self.execute_js(script)
            if result:
                self.log(f"✅ Time {self.team_number} selecionado!")
            return result
        except Exception as e:
            self.log(f"⚠️ Erro ao selecionar time: {e}")
            return False
    
    def print_stats(self):
        """Mostra estatísticas"""
        print("\n" + "="*50)
        print(f"📊 ESTATÍSTICAS")
        print(f"   Total de batalhas: {self.battles_count}")
        print(f"   Time usado: {self.team_number}")
        print("="*50 + "\n")
    
    def run(self):
        """Loop principal do bot"""
        try:
            if not self.connect_to_browser():
                self.log("❌ Não foi possível conectar!")
                return
            
            self.log("🤖 Bot iniciado!")
            self.log(f"🎯 Usando time: {self.team_number}")
            self.log("💡 Pressione Ctrl+C para parar\n")
            
            # Aguarda um pouco
            time.sleep(2)
            
            # Loop principal
            last_state = None
            check_count = 0
            
            while True:
                check_count += 1
                
                # Verifica estado a cada 3 segundos
                time.sleep(3)
                
                # Verifica se está em combate
                in_combat = self.is_in_combat()
                
                # Log de status a cada 10 verificações (30 segundos)
                if check_count % 10 == 0:
                    status = "EM BATALHA" if in_combat else "FORA DE BATALHA"
                    self.log(f"🎮 Status: {status} | Batalhas: {self.battles_count}")
                
                # Se saiu do combate (perdeu ou ganhou)
                if last_state == True and in_combat == False:
                    self.log("\n" + "="*50)
                    self.log("💀 Batalha terminou!")
                    self.log("⏳ Aguardando 2 segundos...")
                    time.sleep(2)
                    
                    # Clica em "Fight Again"
                    if self.click_rejoin():
                        self.log("⏳ Aguardando 60 segundos para nova batalha...")
                        time.sleep(60)
                        self.log("✅ Continuando monitoramento...")
                    else:
                        self.log("⚠️ Não encontrou botão 'Fight Again'")
                        self.log("💡 Certifique-se de que está em uma área de batalha")
                        time.sleep(5)
                    
                    # Mostra stats a cada 5 batalhas
                    if self.battles_count % 5 == 0 and self.battles_count > 0:
                        self.print_stats()
                
                last_state = in_combat
                
        except KeyboardInterrupt:
            self.log("\n⛔ Bot interrompido pelo usuário!")
            self.print_stats()
        except Exception as e:
            self.log(f"❌ Erro: {e}")
            import traceback
            traceback.print_exc()
        finally:
            self.log("👋 Encerrando...")


def main():
    """Função principal"""
    print("="*60)
    print("🎮 POKECHILL BOT - Versão Simplificada")
    print("="*60)
    
    # Escolha do time
    while True:
        try:
            team_input = input("\n🎯 Escolha o time (1-30) ou ENTER para time 2: ").strip()
            
            if team_input == "":
                team_number = 2
                break
            
            team_number = int(team_input)
            
            if 1 <= team_number <= 30:
                break
            else:
                print("❌ Escolha um número entre 1 e 30")
        except ValueError:
            print("❌ Digite um número válido")
        except KeyboardInterrupt:
            print("\n👋 Saindo...")
            return
    
    print(f"\n✅ Time {team_number} selecionado!")
    
    bot = PokeChillBot(team_number=team_number)
    bot.run()


if __name__ == "__main__":
    main()
