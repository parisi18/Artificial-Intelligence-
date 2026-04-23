from src.agent.prompt import SYSTEM_PROMPT
from src.agent.llm import ask_llm
from src.agent.executor import execute_agent_turn


def run_agent_loop(objetivo: str, max_turnos: int = 10):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Objetivo: {objetivo}"},
        {"role": "user", "content": "Observação inicial: nada"},
    ]

    for turno in range(1, max_turnos + 1):
        resposta = ask_llm(messages)

        print(f"[Turno {turno}] resposta=\n{resposta}")

        messages.append({"role": "assistant", "content": resposta})

        if "Final Answer:" in resposta:
            print("[Resultado] Agente encerrou a tarefa.")
            break

        resultado = execute_agent_turn(resposta)
        print(f"[Resultado] {resultado}")
        print("-" * 50)

        messages.append({"role": "user", "content": f"Observation: {resultado}"})

    return messages