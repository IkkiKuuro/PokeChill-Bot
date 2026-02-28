"""
Exemplo avançado usando arquivo de configuração
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pokechill_bot import PokechillBot
import config
import time


class AdvancedBot:
    """Bot avançado com funcionalidades extras"""
    
    def __init__(self):
        self.bot = None
        self.stats = {
            'wins': 0,
            'losses': 0,
            'consecutive_losses': 0,
            'total_battles': 0,
            'start_time': time.time()
        }
    
    def start(self):
        """Inicia o bot com configurações"""
        print("🚀 Iniciando bot avançado...")
        
        self.bot = PokechillBot(
            game_url=config.GAME_URL,
            headless=config.HEADLESS
        )
        self.bot.start()
        
        print(f"⏳ Aguardando {config.LOAD_WAIT_TIME}s para o jogo carregar...")
        time.sleep(config.LOAD_WAIT_TIME)
        
        print("✅ Bot iniciado!")
    
    def stop(self):
        """Para o bot e mostra estatísticas"""
        if self.bot:
            self.bot.stop()
        
        self.show_stats()
    
    def show_stats(self):
        """Mostra estatísticas da sessão"""
        elapsed = time.time() - self.stats['start_time']
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        
        print("\n" + "="*60)
        print("📊 ESTATÍSTICAS DA SESSÃO")
        print("="*60)
        print(f"⏱️  Tempo de execução: {hours:02d}:{minutes:02d}:{seconds:02d}")
        print(f"⚔️  Total de batalhas: {self.stats['total_battles']}")
        print(f"🏆 Vitórias: {self.stats['wins']}")
        print(f"💀 Derrotas: {self.stats['losses']}")
        
        if self.stats['total_battles'] > 0:
            win_rate = (self.stats['wins'] / self.stats['total_battles']) * 100
            print(f"📈 Taxa de vitória: {win_rate:.1f}%")
        
        print("="*60 + "\n")
    
    def run(self):
        """Executa o loop principal do bot"""
        print("\n" + "="*60)
        print("CONFIGURAÇÕES ATIVAS:")
        print(f"  Auto-restart ao perder: {config.AUTO_RESTART_ON_LOSS}")
        print(f"  Auto-restart ao vencer: {config.AUTO_RESTART_ON_WIN}")
        print(f"  Auto-save: {config.AUTO_SAVE}")
        if config.AUTO_SAVE:
            print(f"  Salvar a cada: {config.SAVE_INTERVAL} vitórias")
        if config.MAX_CONSECUTIVE_LOSSES > 0:
            print(f"  Parar após {config.MAX_CONSECUTIVE_LOSSES} derrotas consecutivas")
        print("="*60 + "\n")
        
        print("👀 Monitoramento iniciado...")
        print("Pressione Ctrl+C para parar\n")
        
        try:
            while True:
                # Verifica vitória
                if self.bot.is_battle_won():
                    self.stats['wins'] += 1
                    self.stats['total_battles'] += 1
                    self.stats['consecutive_losses'] = 0
                    
                    if config.VERBOSE_LOGGING:
                        print(f"🏆 Vitória #{self.stats['wins']}!")
                    
                    # Auto-save
                    if config.AUTO_SAVE and self.stats['wins'] % config.SAVE_INTERVAL == 0:
                        self.bot.save_game()
                        print(f"💾 Jogo salvo automaticamente! (Vitórias: {self.stats['wins']})")
                    
                    # Reinicia se configurado
                    if config.AUTO_RESTART_ON_WIN:
                        time.sleep(config.RESTART_DELAY)
                        self.bot.restart_battle()
                        if config.VERBOSE_LOGGING:
                            print("🔄 Reiniciando batalha...")
                
                # Verifica derrota
                elif self.bot.is_battle_lost():
                    self.stats['losses'] += 1
                    self.stats['total_battles'] += 1
                    self.stats['consecutive_losses'] += 1
                    
                    if config.VERBOSE_LOGGING:
                        print(f"💀 Derrota #{self.stats['losses']} (Consecutivas: {self.stats['consecutive_losses']})")
                    
                    # Verifica se deve parar
                    if config.MAX_CONSECUTIVE_LOSSES > 0 and self.stats['consecutive_losses'] >= config.MAX_CONSECUTIVE_LOSSES:
                        print(f"\n⚠️ Atingido o limite de {config.MAX_CONSECUTIVE_LOSSES} derrotas consecutivas!")
                        print("🛑 Parando bot...")
                        break
                    
                    # Reinicia se configurado
                    if config.AUTO_RESTART_ON_LOSS:
                        time.sleep(config.RESTART_DELAY)
                        self.bot.restart_battle()
                        if config.VERBOSE_LOGGING:
                            print("🔄 Reiniciando batalha...")
                
                time.sleep(config.CHECK_INTERVAL)
        
        except KeyboardInterrupt:
            print("\n⏹️ Interrompido pelo usuário")


def main():
    print("🤖 Pokechill Bot Avançado\n")
    
    bot = AdvancedBot()
    
    try:
        bot.start()
        bot.run()
    except Exception as e:
        print(f"\n❌ Erro: {e}")
    finally:
        bot.stop()


if __name__ == "__main__":
    main()
