import json


def parse_action_from_react(response_text: str) -> dict:
    if "Action:" not in response_text:
        raise ValueError("Resposta sem bloco 'Action:'.")

    action_part = response_text.split("Action:", 1)[1].strip()

    try:
        action = json.loads(action_part)
    except json.JSONDecodeError:
        raise ValueError(f"Bloco Action não contém JSON válido: {action_part}")

    if "action" not in action:
        raise ValueError("JSON sem campo 'action'.")

    if "action_input" not in action:
        raise ValueError("JSON sem campo 'action_input'.")

    if not isinstance(action["action_input"], dict):
        raise ValueError("O campo 'action_input' deve ser um objeto JSON.")

    return action