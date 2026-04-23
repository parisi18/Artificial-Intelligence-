from src.agent.executor import execute_agent_turn

def main():
    respostas_do_agente = [
        '{"tool": "andar", "args": {"direcao": "direita"}}',
        '{"tool": "andar", "args": {"direcao": "baixo"}}',
        '{"tool": "atirar", "args": {"direcao": "baixo"}}',
        '{"tool": "pegar_ouro", "args": {}}',
        '{"tool": "escalar_saida", "args": {}}',
        '{"tool": "andar", "args": {}}',
        'qualquer coisa errada',
    ]

    for i, resposta in enumerate(respostas_do_agente, start=1):
        resultado = execute_agent_turn(resposta)
        print(f"[Turno {i}] resposta={resposta}")
        print(f"[Resultado] {resultado}")
        print("-" * 50)

if __name__ == "__main__":
    main()