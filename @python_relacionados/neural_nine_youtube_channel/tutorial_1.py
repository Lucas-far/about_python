

def perform_speed_test():
    import speedtest
    from time import sleep

    # Dependency required = pip install speedtest-cli

    line_skip = '\n'

    instructions = (
        '    Etapa 1: Por favor, aguarde alguns instantes, pois estamos coletando informações pertinentes',
        '    Etapa 2: Lista de servidores coletadas [OK]',
        '    Etapa 3: Servidor de melhor disponibilidade detectado [OK]',
        '    Etapa 4: Testes executados [OK]\n'
    )

    print(instructions[0])
    object_ = speedtest.Speedtest()
    servers_list = object_.get_servers()
    server_best = object_.get_best_server()
    outcome_download = object_.download()
    outcome_upload = object_.upload()
    outcome_ping = object_.results.ping

    report = f"""
    -------------------------------------------- MELHOR PROVEDOR ENCONTRADO --------------------------------------------
    Provedor || {server_best['host']} ({server_best['sponsor']})
    País     || {server_best['country']}
    Cidade   || {server_best['name']}"""

    report_2nd = f"""
    ----------------------------------------------------- TESTAGEM -----------------------------------------------------
    PING                  || {outcome_ping:.2f} ms
    Velocidade (Download) || {outcome_download / 1024 / 1024:.2f} mbps (megabits por segundo)
    Velocidade (Upload)   || {outcome_upload / 1024 / 1024:.2f} mbps (megabits por segundo)
    """

    print(instructions[1])
    sleep(1)
    print(instructions[2])
    sleep(1)
    print(instructions[3])
    sleep(1)

    print(report)
    print(line_skip)
    sleep(1)
    print(report_2nd)


if __name__ == '__main__':
    perform_speed_test()
