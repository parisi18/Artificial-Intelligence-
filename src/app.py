from src.agent.loop import run_agent_loop

def main():
    objetivo = "Encontre o ouro e saia vivo da caverna."
    run_agent_loop(objetivo, max_turnos=10)

if __name__ == "__main__":
    main()