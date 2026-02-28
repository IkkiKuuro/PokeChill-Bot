"""
Bot para PokeChill - Automação de Batalhas
Funções:
- Roda o jogo infinitamente
- Reinicia automaticamente quando perde
- Seleciona time predefinido
- Log de progresso
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import random
import os
from datetime import datetime

class PokeChillBot:
    def __init__(self, team_number=1):
        """
        Inicializa o bot
        
        Args:
            team_number: Número do time (1 a 30)
        """
        self.driver = None
        self.team_number = team_number
        self.battles_won = 0
        self.battles_lost = 0
        self.total_battles = 0
        
    def connect_to_browser(self):
        """Conecta ao navegador (Chrome ou Brave) que você já abriu"""
        print("\n" + "="*60)
        print("🌐 INSTRUÇÕES:")
        print("="*60)
        print("1. Abra seu navegador (Chrome ou Brave)")
        print("2. Vá para: https://play-pokechill.github.io")
        print("3. Faça login se necessário")
        print("4. Deixe o jogo aberto e visível")
        print("="*60)
        input("\n✅ Depois que abrir o jogo, APERTE ENTER aqui... ")
        
        print("\n🔍 Procurando janela do navegador...")
        
        # Tenta conectar ao navegador com debug (funciona para Chrome e Brave)
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            self.driver = webdriver.Chrome(options=chrome_options)
            print("✅ Conectado ao navegador!")
            return True
        except:
            print("\n⚠️ Não conseguiu conectar ao navegador com debug.")
            print("\n📝 Para funcionar com seu navegador já aberto:")
            print("\n   BRAVE:")
            print('   1. Feche TODOS os Brave abertos')
            print('   2. Abra o cmd/terminal')
            print('   3. Execute:')
            print('      "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --remote-debugging-port=9222')
            print("\n   CHROME:")
            print('   1. Feche TODOS os Chrome abertos')
            print('   2. Abra o cmd/terminal')
            print('   3. Execute:')
            print('      chrome.exe --remote-debugging-port=9222')
            print("\n   4. Navegue para o jogo")
            print('   5. Execute o bot novamente')
            print("\n💡 OU deixe o bot abrir o navegador automaticamente!")
            
            print("\n" + "="*60)
            print("Qual navegador deseja usar?")
            print("1. Chrome (bot abre automaticamente)")
            print("2. Brave (bot abre automaticamente)")
            print("3. Cancelar")
            print("="*60)
            
            escolha = input("\nEscolha (1/2/3): ").strip()
            
            if escolha == "1":
                print("\n🚀 Abrindo Chrome...")
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.get("https://play-pokechill.github.io")
                print("✅ Chrome aberto!")
                input("\n✅ Faça login se necessário e APERTE ENTER para continuar... ")
                return True
            elif escolha == "2":
                print("\n🚀 Abrindo Brave...")
                brave_options = Options()
                # Caminhos comuns do Brave
                brave_paths = [
                    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
                    "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
                ]
                
                brave_path = None
                for path in brave_paths:
                    import os
                    if os.path.exists(path):
                        brave_path = path
                        break
                
                if brave_path:
                    brave_options.binary_location = brave_path
                    self.driver = webdriver.Chrome(options=brave_options)
                    self.driver.maximize_window()
                    self.driver.get("https://play-pokechill.github.io")
                    print("✅ Brave aberto!")
                    input("\n✅ Faça login se necessário e APERTE ENTER para continuar... ")
                    return True
                else:
                    print("\n⚠️ Não encontrou o Brave instalado.")
                    print("Digite o caminho completo do brave.exe:")
                    custom_path = input("> ").strip().strip('"')
                    if os.path.exists(custom_path):
                        brave_options.binary_location = custom_path
                        self.driver = webdriver.Chrome(options=brave_options)
                        self.driver.maximize_window()
                        self.driver.get("https://play-pokechill.github.io")
                        print("✅ Brave aberto!")
                        input("\n✅ Faça login se necessário e APERTE ENTER para continuar... ")
                        return True
                    else:
                        print("❌ Caminho inválido!")
                        return False
            else:
                return False
        
    def log(self, message):
        """Log com timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
        
    def wait_and_click(self, by, value, timeout=10):
        """Espera elemento aparecer e clica"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except TimeoutException:
            self.log(f"⚠️ Timeout esperando elemento: {value}")
            return False
            
    def check_element_exists(self, by, value, timeout=2):
        """Verifica se elemento existe"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False
            
    def select_team(self):
        """Seleciona o time predefinido (1 a 30)"""
        self.log(f"🎯 Tentando selecionar time {self.team_number}...")
        
        # Primeiro tenta abrir o menu de times se necessário
        try:
            # Procura pelo menu de times
            team_menu_buttons = [
                (By.ID, "team-menu"),
                (By.XPATH, "//div[@id='team-menu']"),
                (By.XPATH, "//button[contains(text(), 'Team')]"),
                (By.XPATH, "//button[contains(text(), 'Time')]"),
            ]
            
            for by, value in team_menu_buttons:
                try:
                    element = self.driver.find_element(by, value)
                    if element and not element.is_displayed():
                        # Menu não visível, pode precisar abrir
                        continue
                except:
                    pass
        except:
            pass
        
        # Seletores baseados no que o Test.py encontrou
        # O jogo usa preview1, preview2, etc no save.json
        team_selectors = [
            # Tenta clicar no preview team específico
            (By.ID, f"preview-team-{self.team_number}"),
            (By.ID, f"team-preview-{self.team_number}"),
            (By.XPATH, f"//div[contains(@id, 'preview') and contains(@id, '{self.team_number}')]"),
            (By.XPATH, f"//button[contains(@class, 'preview') and contains(text(), '{self.team_number}')]"),
            # Formato do save.json
            (By.ID, f"preview{self.team_number}"),
            (By.XPATH, f"//div[@data-team='{self.team_number}']"),
            (By.XPATH, f"//button[@data-preview='{self.team_number}']"),
        ]
        
        for by, value in team_selectors:
            if self.wait_and_click(by, value, timeout=2):
                self.log(f"✅ Time {self.team_number} selecionado!")
                time.sleep(1)
                return True
        
        # Se não encontrou, assume que já está no time correto        
        self.log(f"⚠️ Não encontrou botão de seleção de time, assumindo que já está selecionado...")
        return True
        
    def start_battle(self):
        """Inicia uma nova batalha"""
        self.log("⚔️ Procurando botão de batalha...")
        
        # Lista TODOS os botões visíveis para debug
        try:
            all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
            visible_buttons = [btn for btn in all_buttons if btn.is_displayed()]
            self.log(f"🔍 Encontrados {len(visible_buttons)} botões visíveis")
            
            # Mostra os primeiros 5 botões para debug
            for i, btn in enumerate(visible_buttons[:5], 1):
                try:
                    text = btn.text[:20] if btn.text else "(sem texto)"
                    btn_id = btn.get_attribute("id") or "(sem id)"
                    self.log(f"   Botão {i}: '{text}' | ID: '{btn_id}'")
                except:
                    pass
        except Exception as e:
            self.log(f"⚠️ Erro ao listar botões: {e}")
        
        # Tenta diferentes possíveis botões de iniciar
        start_buttons = [
            # IDs específicos
            (By.ID, "start-battle"),
            (By.ID, "battle-button"),
            (By.ID, "fightBtn"),
            (By.ID, "fight-btn"),
            (By.ID, "startBattle"),
            (By.ID, "battleBtn"),
            # Por texto
            (By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'battle')]"),
            (By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'fight')]"),
            (By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'start')]"),
            (By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'lutar')]"),
            (By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'batalha')]"),
            # Por classe
            (By.CLASS_NAME, "start-battle"),
            (By.CLASS_NAME, "battle-button"),
            (By.CLASS_NAME, "fight-button"),
        ]
        
        for by, value in start_buttons:
            if self.wait_and_click(by, value, timeout=2):
                self.log("✅ Batalha iniciada!")
                self.log("⏳ Aguardando 1 minuto para a batalha começar...")
                time.sleep(60)  # Espera 1 minuto antes de começar a verificar
                self.log("🎮 Começando monitoramento da batalha...")
                return True
        
        self.log("❌ Não encontrou botão de iniciar batalha!")
        self.log("👉 Use o Test.py para descobrir o ID/texto do botão correto")
        return False
        
    def battle_loop(self):
        """Loop principal durante a batalha"""
        self.log("🎮 Em batalha...")
        
        check_count = 0
        while True:
            time.sleep(3)  # Espera 3 segundos entre cada verificação
            check_count += 1
            
            # Log a cada 10 verificações (30 segundos)
            if check_count % 10 == 0:
                self.log(f"⏱️ Monitorando... ({check_count * 3} segundos)")
            
            # Verifica se perdeu
            if self.check_lost():
                self.log("❌ Perdeu a batalha!")
                self.battles_lost += 1
                self.total_battles += 1
                return "lost"
            
            # Verifica se ganhou
            if self.check_won():
                self.log("✅ Ganhou a batalha!")
                self.battles_won += 1
                self.total_battles += 1
                return "won"
            
            # Tenta atacar (só a cada 5 segundos para não sobrecarregar)
            if check_count % 2 == 0:
                self.attack()
            
    def check_lost(self):
        """Verifica se perdeu a batalha"""
        # Possíveis indicadores de derrota
        lost_indicators = [
            (By.XPATH, "//div[contains(text(), 'You lost')]"),
            (By.XPATH, "//div[contains(text(), 'Defeat')]"),
            (By.XPATH, "//div[contains(text(), 'Lost')]"),
            (By.XPATH, "//div[contains(text(), 'Derrot')]"),
            (By.XPATH, "//button[contains(text(), 'Try Again')]"),
            (By.XPATH, "//button[contains(text(), 'Restart')]"),
            (By.XPATH, "//button[contains(text(), 'Tentar')]"),
            (By.ID, "defeat-screen"),
            (By.ID, "lost-screen"),
            (By.CLASS_NAME, "defeat"),
            (By.CLASS_NAME, "lost"),
        ]
        
        for by, value in lost_indicators:
            if self.check_element_exists(by, value, timeout=0.5):
                return True
        return False
        
    def check_won(self):
        """Verifica se ganhou a batalha"""
        # Possíveis indicadores de vitória
        won_indicators = [
            (By.XPATH, "//div[contains(text(), 'You won')]"),
            (By.XPATH, "//div[contains(text(), 'Victory')]"),
            (By.XPATH, "//div[contains(text(), 'Won')]"),
            (By.XPATH, "//div[contains(text(), 'Vitória')]"),
            (By.XPATH, "//div[contains(text(), 'Venceu')]"),
            (By.XPATH, "//button[contains(text(), 'Continue')]"),
            (By.XPATH, "//button[contains(text(), 'Continuar')]"),
            (By.ID, "victory-screen"),
            (By.ID, "won-screen"),
            (By.CLASS_NAME, "victory"),
            (By.CLASS_NAME, "won"),
        ]
        
        for by, value in won_indicators:
            if self.check_element_exists(by, value, timeout=0.5):
                return True
        return False
        
    def attack(self):
        """Executa um ataque"""
        # Tenta clicar em botões de ataque
        attack_buttons = [
            # Seletores comuns de moves/ataques
            (By.CLASS_NAME, "move-button"),
            (By.CLASS_NAME, "attack"),
            (By.CLASS_NAME, "move"),
            (By.CLASS_NAME, "attack-button"),
            # Por XPATH
            (By.XPATH, "//button[contains(@class, 'move')]"),
            (By.XPATH, "//div[contains(@class, 'move') and contains(@class, 'button')]"),
            (By.XPATH, "//button[contains(@class, 'attack')]"),
            # IDs específicos
            (By.ID, "move1"),
            (By.ID, "move2"),
            (By.ID, "move3"),
            (By.ID, "move4"),
            (By.ID, "attack1"),
            (By.ID, "attack-1"),
            # Slots de move
            (By.ID, "move-slot-1"),
            (By.ID, "move-slot-2"),
            (By.XPATH, "//div[contains(@id, 'move-slot')]"),
        ]
        
        for by, value in attack_buttons:
            try:
                elements = self.driver.find_elements(by, value)
                if elements:
                    # Filtra apenas elementos visíveis e clicáveis
                    visible_elements = [e for e in elements if e.is_displayed() and e.is_enabled()]
                    if visible_elements:
                        # Escolhe um ataque aleatório
                        element = random.choice(visible_elements)
                        element.click()
                        self.log("💥 Atacou!")
                        time.sleep(1)
                        return True
            except Exception as e:
                continue
        
        # Se não encontrou botões específicos, tenta qualquer botão visível na área de batalha
        try:
            all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
            battle_buttons = [btn for btn in all_buttons if btn.is_displayed() and btn.is_enabled()]
            if battle_buttons:
                # Pega um botão aleatório (pode ser um ataque)
                btn = random.choice(battle_buttons[:4])  # Limita aos primeiros 4
                btn.click()
                time.sleep(1)
                return True
        except:
            pass
            
        return False
        
    def restart_after_loss(self):
        """Reinicia o jogo após perder"""
        self.log("🔄 Reiniciando jogo...")
        
        # Possíveis botões de reinício
        restart_buttons = [
            (By.XPATH, "//button[contains(text(), 'Try Again')]"),
            (By.XPATH, "//button[contains(text(), 'Restart')]"),
            (By.XPATH, "//button[contains(text(), 'New Game')]"),
            (By.ID, "restart-button"),
            (By.ID, "try-again"),
            (By.CLASS_NAME, "restart"),
        ]
        
        for by, value in restart_buttons:
            if self.wait_and_click(by, value, timeout=3):
                time.sleep(2)
                self.log("✅ Jogo reiniciado!")
                return True
                
        # Se não encontrou botão, recarrega a página
        self.log("🔄 Recarregando página...")
        self.driver.refresh()
        time.sleep(3)
        return True
        
    def continue_after_win(self):
        """Continua após vitória"""
        self.log("➡️ Continuando após vitória...")
        
        continue_buttons = [
            (By.XPATH, "//button[contains(text(), 'Continue')]"),
            (By.XPATH, "//button[contains(text(), 'Next')]"),
            (By.ID, "continue-button"),
            (By.CLASS_NAME, "continue"),
        ]
        
        for by, value in continue_buttons:
            if self.wait_and_click(by, value, timeout=3):
                time.sleep(2)
                return True
                
        return False
        
    def print_stats(self):
        """Imprime estatísticas"""
        win_rate = (self.battles_won / self.total_battles * 100) if self.total_battles > 0 else 0
        print("\n" + "="*50)
        print(f"📊 ESTATÍSTICAS")
        print(f"   Total de batalhas: {self.total_battles}")
        print(f"   Vitórias: {self.battles_won}")
        print(f"   Derrotas: {self.battles_lost}")
        print(f"   Taxa de vitória: {win_rate:.1f}%")
        print(f"   Time usado: {self.team_number}")
        print("="*50 + "\n")
        
    def run(self):
        """Loop principal do bot"""
        try:
            if not self.connect_to_browser():
                self.log("❌ Não foi possível conectar ao navegador!")
                return
            
            self.log("🤖 Iniciando bot automático!")
            
            while True:
                try:
                    # Seleciona time
                    self.log("\n" + "="*50)
                    self.select_team()
                    time.sleep(2)
                    
                    # Inicia batalha
                    if not self.start_battle():
                        self.log("⚠️ Não encontrou botão de batalha!")
                        self.log("💡 DICA: Execute Test.py para descobrir o botão correto")
                        self.log("⏳ Aguardando 10 segundos antes de tentar novamente...")
                        time.sleep(10)
                        continue
                    
                    # Loop de batalha (já tem o delay de 1 minuto no start_battle)
                    result = self.battle_loop()
                    
                    # Processa resultado
                    if result == "lost":
                        self.log("\n💀 Processando derrota...")
                        self.restart_after_loss()
                        time.sleep(3)
                    elif result == "won":
                        self.log("\n🎉 Processando vitória...")
                        self.continue_after_win()
                        time.sleep(3)
                    
                    # Mostra estatísticas a cada 5 batalhas
                    if self.total_battles % 5 == 0:
                        self.print_stats()
                        
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    self.log(f"❌ Erro no loop: {e}")
                    import traceback
                    traceback.print_exc()
                    self.log("⏳ Aguardando 5 segundos antes de continuar...")
                    time.sleep(5)
                    
        except KeyboardInterrupt:
            self.log("\n⛔ Bot interrompido pelo usuário!")
            self.print_stats()
        except Exception as e:
            self.log(f"❌ Erro fatal: {e}")
        finally:
            if self.driver:
                self.log("🔚 Fechando navegador...")
                self.driver.quit()


def main():
    """Função principal"""
    print("="*60)
    print("🎮 POKECHILL BOT")
    print("="*60)
    
    # Escolha do time (1 a 30)
    while True:
        try:
            team_input = input("\n🎯 Escolha o time (1-30) ou ENTER para time 1: ").strip()
            
            if team_input == "":
                team_number = 1
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
    print("💡 Pressione Ctrl+C a qualquer momento para parar\n")
    
    bot = PokeChillBot(team_number=team_number)
    bot.run()


if __name__ == "__main__":
    main()
