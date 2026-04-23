from src.agent.prompt import SYSTEM_PROMPT
from src.agent.executor import execute_agent_turn


def run_fake_agent_loop(agent_responses: list[str], objetivo: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Objetivo: {objetivo}"},
        {"role": "user", "content": "Observação inicial: nada"},
    ]

    for turno, response_text in enumerate(agent_responses, start=1):
        messages.append({"role": "assistant", "content": response_text})

        resultado = execute_agent_turn(response_text)

        messages.append({"role": "user", "content": f"Resultado da ação: {resultado}"})

        print(f"[Turno {turno}] resposta={response_text}")
        print(f"[Resultado] {resultado}")
        print("-" * 50)

    return messages