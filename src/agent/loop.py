from src.agent.prompt import SYSTEM_PROMPT
from src.agent.llm import ask_llm
from src.agent.executor import execute_agent_turn
from src.tools import get_estado_atual


def run_agent_loop(objetivo: str, max_turnos: int = 10):
    heroi, mundo = get_estado_atual()

    observacao_inicial = mundo.perceber(heroi)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Objetivo: {objetivo}"},
        {
            "role": "user",
            "content": f"Observation: {observacao_inicial}\n\n{heroi.formatar_memoria()}"
        },
    ]

    for turno in range(1, max_turnos + 1):
        resposta = ask_llm(messages)

        if resposta is None:
            print("[Erro] O modelo não retornou resposta.")
            break

        print(f"[Turno {turno}] resposta=\n{resposta}")

        messages.append({"role": "assistant", "content": resposta})

        if "Final Answer:" in resposta:
            print("[Encerrado] O agente finalizou a tarefa.")
            break

        resultado = execute_agent_turn(resposta)

        print(f"[Resultado] {resultado}")
        print(heroi.formatar_memoria())
        print("-" * 50)

        heroi, mundo = get_estado_atual()

        messages.append({
            "role": "user",
            "content": f"Observation: {resultado}\n\n{heroi.formatar_memoria()}"
        })

    return messages