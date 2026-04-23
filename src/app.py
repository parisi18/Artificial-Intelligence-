from src.tools import call_tool

def main():
    acoes = [
        {"tool": "andar", "args": {"direcao": "direita"}},
        {"tool": "andar", "args": {"direcao": "baixo"}},
        {"tool": "atirar", "args": {"direcao": "baixo"}},
        {"tool": "pegar_ouro", "args": {}},
        {"tool": "escalar_saida", "args": {}},
    ]

    for i, acao in enumerate(acoes, start=1):
        tool = acao["tool"]
        args = acao["args"]
        resultado = call_tool(tool, **args)
        print(f"[Ação {i}] {tool} -> {resultado}")

if __name__ == "__main__":
    main()