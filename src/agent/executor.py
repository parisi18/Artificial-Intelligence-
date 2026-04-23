from src.tools import call_tool
from src.agent.parser import parse_action_from_react


def execute_agent_turn(response_text: str) -> str:
    try:
        action = parse_action_from_react(response_text)
    except Exception as e:
        return f"Erro de parsing da resposta do agente: {e}"

    try:
        tool_name = action["action"]
        args = action["action_input"]
        return call_tool(tool_name, **args)
    except Exception as e:
        return f"Erro ao executar a ferramenta '{tool_name}': {e}"