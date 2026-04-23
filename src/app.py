from src.agent.loop import run_agent_loop

def main():
    run_agent_loop("Encontre o ouro e saia vivo da caverna.", max_turnos=10)

if __name__ == "__main__":
    main()