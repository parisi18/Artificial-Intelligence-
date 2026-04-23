from src.agent.executor import execute_agent_turn

def main():
    respostas_do_agente = [
        '''Thought:
Vou explorar uma casa à direita.

Action:
{"action": "andar", "action_input": {"direcao": "direita"}}''',

        '''Thought:
Agora vou descer.

Action:
{"action": "andar", "action_input": {"direcao": "baixo"}}''',

        '''Thought:
Vou tentar atirar para baixo.

Action:
{"action": "atirar", "action_input": {"direcao": "baixo"}}''',

        '''Final Answer:
Não consegui concluir a missão ainda.'''
    ]

    for i, resposta in enumerate(respostas_do_agente, start=1):
        print(f"[Turno {i}] resposta=\n{resposta}")

        if "Final Answer:" in resposta:
            print("[Resultado] Agente encerrou a tarefa.")
            break

        resultado = execute_agent_turn(resposta)
        print(f"[Resultado] {resultado}")
        print("-" * 50)

if __name__ == "__main__":
    main()