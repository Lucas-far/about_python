

def warn(repetitions: int, interval_between_messages: int, typing_bar_x: int, typing_bar_y: int):

    from random import choice as ch
    import pyautogui
    from time import sleep
    from datetime import datetime
    import pyperclip

    adjectives = (
        'Delícia', 'Amor', 'Minha gata selvagem', 'Minha deusa', 'Gostosa', 'Tesão', 'Moranguinho', 'Bruxinha',
        'Cerejinha', 'Razão da minha felicidade', 'Lanna aventureira', 'Pituiba', 'Cosplay de boneca russa',
        'Perestroyka', 'Smirnoff', 'Cleitinha', 'Penípede', 'Tv Marisol', 'Minha deusa das coisinhas microscópicas',
        'Rosicleude', 'Prospera', 'Consagrada', 'Astralina', 'Tampinha', 'Luluzinha', 'Hello Kitty', 'Mulan',
        'Toco de gente', 'Smurf Albina', 'Pikachu', 'Mergulhadora de aquário', 'Alpinista de poltrona', 'Cotoco',
        'Escaladora de meio fio', 'Hobbit', 'Jóquei de pônei', 'Hantara', 'Pequena Sereia', 'Jane de samambaia',
        'Lenhadora de Bonsai', 'Piloto de autorama', 'Bundinha de almofada', 'Vegana carnívora', 'Amanhecer',
        'Creusa', 'Leoa das Savanas'
    )

    sentence_main = 'Você já bebeu água? '

    sentences_dtb = (
        'Você não vive só de gostosura!',
        'Não se faz de doida! bebe essa água, muié',
        'Se você é basicamente água, e não quer beber água, então você não se ama',
        'Quem vive sem água é camelo, e assistir filme de camelo, não torna você um',
        'Levante seus glúteos gostosos dessa cadeira, e vá beber!',
        "Já botou o desenho do copo d'água na janela, pra lembrar?",
        'Espero que não esteja fazendo cosplay do teu pai, querendo ter apenas um rim',
        'Se você não beber água, eu vou votar no Lula!',
        'Se você não beber água, eu vou sair nu em protesto!',
        'Se você não beber água, eu vou invadir a Senac e protestar pros teus chefes!',
        'Se você não beber água, eu vou pintar meu cabelo de verde neon!',
        'Eu te amo, e não quero ver você com problemas!',
        'Se você não beber água, eu faço greve de sexo',
        'Não adianta você enrolar, eu sei, você sabe e Deus sabe, que você não bebe água a horas!',
        "Seje como o planeta Terra: cheio d'agua!",
        'Encha seu bucho de água, meu amor!',
        'Se você me ama, beba água!',
        'Não...? Você perdeu as lamparinas do juízo?',
        'Seje uma boa menina, levante esse corpo gostoso do carvalho e vá beber...tá bom?',
        'Faça isso por mim, tá bem? Eu te amo!',
        'Se você tem boca, então a água pode entrar!',
        'Rapaz...Moça...minina réa...nãm',
        'Você está disposta a ouvir a palavra do H2O?',
        'Se você não vai até a água, a água vai até você...em forma de tsunami',
        'Bebeu água? Não! Tá com sede? Tô! Olha, olha, olha, olha a água mineral...',
        'Água mole em pedra dura, tanta bate até que cria lodo',
        'Se você ignora a água, saiba que está cometendo águafobia',
        'Se você não beber água, eu vou me vestir de copo de água mineral, vou pra tua casa e me vender pras pessoas!',
        'Se você não beber água, eu vou sequestrar o teu cachorro (brincadeira)',
        'Se você não beber água, eu me visto de mulher da vida e rodo bolsinha na frente da tua casa',
        'Se você já viu máquinas se rebelando, saiba que a água também pode fazer isso!',
        'Be water, my girlfriend! (By Bruci Li)',
        'Du muss wasser trinken!',
        'Você nadou em água por 9 meses, por que se nega a beber água agora?',
        'Você gosta de nadar, mas não gosta de beber água!',
        'Aceite a água na sua vida! ACEITE A ÁGUA, AAAAAAAAAA',
        'Taaaaaaaaaaaaake me, to the magic of the momment, on the glory night, where the children of the water drink ' +
        'away ♪',
        'Ei! você ai, bebe essa água, bebe essa água ai...',
        'Chegou, a turma do funil, todo mundo bebe, mas ninguém dorme no ponto...nós é que bebemos e eles que ficam ' +
        'tontos...pãpãpã!',
        'Se você beber água, vai ganhar na loteria!'
    )

    # https://textfac.es/
    emojis = (
        '¬_¬', 'xD', ':)', ':(', '=D', '=(', '=)', 'T-T', 'x_x', '^.^', ':P', 'u_u', '*_*', 'o3o', 'O3O', 'T_T',
        'xP', 'i.i', ':O', ':0', '@_@', 'o_o', '\o/', '( ͡° ͜ʖ ͡°)', '¯\_(ツ)_/¯', 'ʕ•ᴥ•ʔ', '(▀Ĺ̯▀)',
        'ಠ_ಠ', '◕_◕', '◕‿‿◕', '(͠° ͟ʖ ͡°)', '◕ヮ◕', '(• ε •)', "(ง'̀-'́)ง", 'ಥ﹏ಥ', "๏̯͡๏", '(•◡•)', "(❍ᴥ❍)", "(◕‿◕)",
        '(ᵔᴥᵔ)', "(╯°□°)╯", "(¬‿¬)", "￣ ³￣", 'ಠ╭╮ಠ', '(•_•)', '♥‿♥', 'ಥ_ಥ', '⌐■_■ ♪', '~(˘▾˘~)', '◉_◉',
        '\(•◡•)/', '(~˘▾˘)~', 'ʘل͜ʘ', 'ó_ó', 'ò_ò', 'ò_ó'
    )

    # ----------------------------------------- PRACTICAL PART OF THE FUNCTION -----------------------------------------
    counter = 0
    while counter < repetitions:

        midnight = '00'
        time_ = [datetime.now().hour, datetime.now().minute, datetime.now().second, datetime.now().microsecond]

        if time_[0] == 0:
            time_[0] = midnight

        elif time_[0] < 10:
            time_[0] = f"{'0' + str(time_[0])}"

        if time_[1] < 10:
            time_[1] = f"{'0' + str(time_[1])}"

        if time_[2] < 10:
            time_[2] = f"{'0' + str(time_[2])}"

        # print(time_)

        the_time = f'[ {time_[0]}:{time_[1]}:{time_[2]} e {time_[3]} MICROSEGUNDOS ]'

        # values = tuple(range(1, 1001))
        # value_1 = ch(values)
        # value_2 = ch(values)
        # calculus_symbols = ['+', '-', '*', '/']
        # calculus_choice = ch(calculus_symbols)
        #
        # actions = {
        #     calculus_symbols[0]: f'{value_1} + {value_2} = {value_1 + value_2:.2f}',
        #     calculus_symbols[1]: f'{value_1} - {value_2} = {value_1 - value_2:.2f}',
        #     calculus_symbols[2]: f'{value_1} x {value_2} = {value_1 * value_2:.2f}',
        #     calculus_symbols[3]: f'{value_1} / {value_2} = {value_1 / value_2:.2f}',
        # }
        #
        # box = []
        #
        # for string in calculus_symbols:
        #     if calculus_choice == string:
        #         box.append(actions[string])

        typing_bar = (typing_bar_x, typing_bar_y)

        pyautogui.moveTo(typing_bar[0], typing_bar[1])
        pyautogui.click(typing_bar[0], typing_bar[1])
        pyautogui.click(typing_bar[0], typing_bar[1])

        the_sentence = f"""
        {ch(adjectives)}, são {the_time}
        {sentence_main}
        {ch(sentences_dtb)} {ch(emojis)}"""
        # TELECURSO ÁLGEBRA DE GRÁTIS: {box[0]} (retirado)

        pyperclip.copy(the_sentence)
        pyautogui.hotkey('ctrl', 'v')
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(interval_between_messages)
        counter += 1

    # ------------------------------------------- TEST PART OF THE FUNCTION -------------------------------------------
    # the_sentence = f"""
    # {ch(adjectives)}, são {the_time}
    # {sentence_main}
    # {ch(sentences_dtb)} {ch(emojis)}
    # TELECURSO ÁLGEBRA DE GRÁTIS: {box[0]}"""
    #
    # return the_sentence


if __name__ == '__main__':
    warn(repetitions=1000,
         interval_between_messages=600,
         typing_bar_x=912,
         typing_bar_y=675)
    # print(warn(repetitions=20, speed_between_messages=1))
    # test = ''
    # print(test)
