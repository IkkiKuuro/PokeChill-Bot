"""
Script de teste e demonstração do bot
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pokechill_bot import create_bot
import time


def print_header():
    print("\n" + "="*60)
    print("   🤖 POKECHILL BOT - DEMONSTRAÇÃO")
    print("="*60 + "\n")


def test_basic_functions(bot):
    """Testa funções básicas do bot"""
    print("🧪 Testando funções básicas...\n")
    
    # Testa obtenção de estado
    print("1️⃣ Obtendo estado do jogo...")
    state = bot.get_game_state()
    print(f"   ✓ Área atual: {state.get('currentArea', 'N/A')}")
    print(f"   ✓ Em combate: {state.get('inCombat', 'N/A')}")
    print(f"   ✓ Auto-refight: {state.get('autoRefight', 'N/A')}")
    
    # Testa execução de JavaScript
    print("\n2️⃣ Testando execução de JavaScript...")
    result = bot.execute_js("return typeof saved")
    print(f"   ✓ Tipo de 'saved': {result}")
    
    # Testa detecção de combate
    print("\n3️⃣ Verificando estado de combate...")
    in_combat = bot.is_in_combat()
    print(f"   ✓ Está em combate: {in_combat}")
    
    print("\n✅ Testes básicos concluídos!\n")


def interactive_menu(bot):
    """Menu interativo para testar funcionalidades"""
    while True:
        print("\n" + "="*60)
        print("MENU INTERATIVO")
        print("="*60)
        print("1. Ver estado do jogo")
        print("2. Verificar se está em combate")
        print("3. Verificar vitória/derrota")
        print("4. Reiniciar batalha")
        print("5. Ativar auto-refight")
        print("6. Desativar auto-refight")
        print("7. Salvar jogo")
        print("8. Executar JavaScript customizado")
        print("9. Iniciar monitoramento automático")
        print("0. Sair")
        print("="*60)
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            state = bot.get_game_state()
            print("\n📊 Estado do jogo:")
            for key, value in state.items():
                print(f"   {key}: {value}")
        
        elif choice == "2":
            in_combat = bot.is_in_combat()
            print(f"\n🎯 Em combate: {in_combat}")
        
        elif choice == "3":
            won = bot.is_battle_won()
            lost = bot.is_battle_lost()
            print(f"\n🏆 Venceu: {won}")
            print(f"💀 Perdeu: {lost}")
        
        elif choice == "4":
            bot.restart_battle()
        
        elif choice == "5":
            bot.enable_auto_refight()
        
        elif choice == "6":
            bot.disable_auto_refight()
        
        elif choice == "7":
            bot.save_game()
        
        elif choice == "8":
            js_code = input("\nDigite o código JavaScript: ")
            try:
                result = bot.execute_js(js_code)
                print(f"\n✓ Resultado: {result}")
            except Exception as e:
                print(f"\n✗ Erro: {e}")
        
        elif choice == "9":
            print("\n🔄 Iniciando monitoramento...")
            print("Pressione Ctrl+C para parar\n")
            restart_loss = input("Reiniciar ao perder? (s/n): ").lower() == 's'
            restart_win = input("Reiniciar ao vencer? (s/n): ").lower() == 's'
            
            try:
                bot.monitor_battle(
                    auto_restart_on_loss=restart_loss,
                    auto_restart_on_win=restart_win
                )
            except KeyboardInterrupt:
                print("\n⏹️ Monitoramento parado")
        
        elif choice == "0":
            print("\n👋 Saindo...")
            break
        
        else:
            print("\n❌ Opção inválida!")


def main():
    print_header()
    
    print("Escolha o modo de execução:")
    print("1. Teste rápido das funções")
    print("2. Menu interativo")
    print("3. Auto-farm (monitoramento contínuo)")
    
    choice = input("\nOpção: ").strip()
    
    print("\n🚀 Iniciando bot...")
    bot = create_bot()
    
    try:
        print("⏳ Aguardando o jogo carregar...")
        time.sleep(5)
        
        if choice == "1":
            test_basic_functions(bot)
            print("✨ Demonstração concluída!")
        
        elif choice == "2":
            interactive_menu(bot)
        
        elif choice == "3":
            print("\n🎮 Modo Auto-Farm")
            print("Reiniciará batalhas automaticamente")
            print("Pressione Ctrl+C para parar\n")
            time.sleep(2)
            
            bot.monitor_battle(
                auto_restart_on_loss=True,
                auto_restart_on_win=True
            )
        
        else:
            print("❌ Opção inválida!")
    
    except KeyboardInterrupt:
        print("\n\n⏹️ Interrompido pelo usuário")
    
    finally:
        print("\n🛑 Encerrando bot...")
        bot.stop()
        print("✅ Encerrado com sucesso!")


if __name__ == "__main__":
    main()
