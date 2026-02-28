"""
Pokechill Game Bot
Bot para automatizar ações no jogo Pokechill
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
from typing import Optional, Dict, Any


class PokechillBot:
    """Bot principal para interagir com o jogo Pokechill"""
    
    def __init__(self, game_url: str = "file:///index.html", headless: bool = False):
        """
        Inicializa o bot
        
        Args:
            game_url: URL do jogo (pode ser local ou online)
            headless: Se True, executa o navegador sem interface gráfica
        """
        self.game_url = game_url
        self.driver = None
        self.headless = headless
        self.is_running = False
        
    def start(self):
        """Inicia o navegador e carrega o jogo"""
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.game_url)
        print(f"🎮 Jogo carregado: {self.game_url}")
        time.sleep(2)  # Aguarda o jogo carregar
        
    def stop(self):
        """Fecha o navegador"""
        if self.driver:
            self.driver.quit()
            print("🛑 Bot encerrado")
            
    def execute_js(self, script: str) -> Any:
        """
        Executa JavaScript no contexto do jogo
        
        Args:
            script: Código JavaScript para executar
            
        Returns:
            Resultado da execução
        """
        return self.driver.execute_script(script)
    
    def get_game_state(self) -> Dict[str, Any]:
        """
        Obtém o estado atual do jogo
        
        Returns:
            Dicionário com informações do jogo
        """
        script = """
        return {
            currentArea: saved.currentArea,
            autoRefight: saved.autoRefight,
            inCombat: document.getElementById('explore-combat')?.style.display !== 'none',
            currentTrainerSlot: typeof currentTrainerSlot !== 'undefined' ? currentTrainerSlot : null,
            wildPkmnHp: typeof wildPkmnHp !== 'undefined' ? wildPkmnHp : null,
            wildPkmnHpMax: typeof wildPkmnHpMax !== 'undefined' ? wildPkmnHpMax : null
        };
        """
        return self.execute_js(script)
    
    def is_in_combat(self) -> bool:
        """Verifica se está em combate"""
        try:
            combat_div = self.driver.find_element(By.ID, "explore-combat")
            return combat_div.value_of_css_property("display") != "none"
        except NoSuchElementException:
            return False
    
    def is_battle_lost(self) -> bool:
        """
        Verifica se perdeu a batalha
        Detecta através de mensagens ou estado do jogo
        """
        # Verifica se saiu do combate (leaveCombat foi chamado)
        state = self.get_game_state()
        
        # Se não está em combate mas estava, pode ter perdido
        if not state.get('inCombat', True):
            return True
            
        # Verifica se todos os Pokémon do time foram derrotados
        script = """
        let allDefeated = true;
        for (let i = 1; i <= 6; i++) {
            const slot = team['slot' + i];
            if (slot && slot.pkmn && slot.pkmn.currentHp > 0) {
                allDefeated = false;
                break;
            }
        }
        return allDefeated;
        """
        return self.execute_js(script)
    
    def is_battle_won(self) -> bool:
        """Verifica se venceu a batalha"""
        state = self.get_game_state()
        
        # Verifica se o HP do Pokémon selvagem chegou a 0
        if state.get('wildPkmnHp') is not None:
            return state['wildPkmnHp'] <= 0
            
        return False
    
    def restart_battle(self):
        """Reinicia a batalha atual"""
        print("🔄 Reiniciando batalha...")
        
        # Primeiro sai do combate se estiver nele
        self.execute_js("if (typeof leaveCombat === 'function') leaveCombat();")
        time.sleep(0.5)
        
        # Depois reinicia a área
        self.execute_js("if (typeof setWildPkmn === 'function') setWildPkmn();")
        time.sleep(0.5)
        
        print("✅ Batalha reiniciada")
    
    def enable_auto_refight(self):
        """Ativa o auto-refight do jogo"""
        self.execute_js("saved.autoRefight = true;")
        print("⚡ Auto-refight ativado")
    
    def disable_auto_refight(self):
        """Desativa o auto-refight do jogo"""
        self.execute_js("saved.autoRefight = false;")
        print("⏸️ Auto-refight desativado")
    
    def click_element(self, element_id: str):
        """Clica em um elemento pelo ID"""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, element_id))
            )
            element.click()
            print(f"🖱️ Clicou em: {element_id}")
        except TimeoutException:
            print(f"❌ Elemento não encontrado: {element_id}")
    
    def wait_for_element(self, element_id: str, timeout: int = 10) -> bool:
        """
        Aguarda um elemento aparecer
        
        Args:
            element_id: ID do elemento
            timeout: Tempo máximo de espera em segundos
            
        Returns:
            True se o elemento foi encontrado
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            return True
        except TimeoutException:
            return False
    
    def save_game(self):
        """Salva o jogo"""
        self.execute_js("if (typeof saveGame === 'function') saveGame();")
        print("💾 Jogo salvo")
    
    def load_game(self):
        """Carrega o jogo salvo"""
        self.execute_js("if (typeof loadGame === 'function') loadGame();")
        print("📂 Jogo carregado")
    
    def monitor_battle(self, auto_restart_on_loss: bool = True, auto_restart_on_win: bool = False):
        """
        Monitora a batalha e executa ações
        
        Args:
            auto_restart_on_loss: Se True, reinicia automaticamente ao perder
            auto_restart_on_win: Se True, reinicia automaticamente ao vencer
        """
        print("👀 Monitorando batalha...")
        self.is_running = True
        
        last_state = None
        
        try:
            while self.is_running:
                state = self.get_game_state()
                
                if state != last_state:
                    print(f"📊 Estado: {state}")
                    last_state = state
                
                # Verifica se perdeu
                if auto_restart_on_loss and self.is_battle_lost():
                    print("💀 Batalha perdida!")
                    time.sleep(1)
                    self.restart_battle()
                    time.sleep(2)
                
                # Verifica se venceu
                if auto_restart_on_win and self.is_battle_won():
                    print("🏆 Batalha vencida!")
                    time.sleep(1)
                    self.restart_battle()
                    time.sleep(2)
                
                time.sleep(0.5)  # Checa a cada 0.5 segundos
                
        except KeyboardInterrupt:
            print("\n⏹️ Monitoramento interrompido pelo usuário")
            self.is_running = False


# Funções auxiliares para uso direto
def create_bot(game_url: str = None, headless: bool = False) -> PokechillBot:
    """
    Cria e inicia um bot
    
    Args:
        game_url: URL do jogo (se None, usa o caminho local)
        headless: Se True, executa sem interface gráfica
        
    Returns:
        Instância do bot
    """
    if game_url is None:
        # Tenta usar o caminho local
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        game_path = os.path.join(os.path.dirname(current_dir), "index.html")
        game_url = f"file:///{game_path.replace(os.sep, '/')}"
    
    bot = PokechillBot(game_url, headless)
    bot.start()
    return bot


if __name__ == "__main__":
    # Exemplo de uso
    print("🤖 Pokechill Bot Iniciando...\n")
    
    # Cria o bot
    bot = create_bot()
    
    try:
        # Aguarda o jogo carregar completamente
        print("Aguardando jogo carregar...")
        time.sleep(5)
        
        # Exemplo: Monitora batalhas e reinicia ao perder
        bot.monitor_battle(auto_restart_on_loss=True, auto_restart_on_win=False)
        
    except KeyboardInterrupt:
        print("\n\n👋 Encerrando bot...")
    finally:
        bot.stop()
