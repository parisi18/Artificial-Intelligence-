import json


def parse_action(response_text: str) -> dict:
    """
    Converte a resposta do modelo em um dict no formato:
    {"tool": "...", "args": {...}}
    """
    try:
        action = json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError(f"Resposta não está em JSON válido: {response_text}")

    if not isinstance(action, dict):
        raise ValueError("A resposta do agente deve ser um objeto JSON.")

    if "tool" not in action:
        raise ValueError("JSON sem campo obrigatório 'tool'.")

    if "args" not in action:
        raise ValueError("JSON sem campo obrigatório 'args'.")

    if not isinstance(action["args"], dict):
        raise ValueError("O campo 'args' deve ser um objeto JSON.")

    return action