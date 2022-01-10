

def importante():
    """
    Em um loop infinito, o [ return ] pode ser seu ponto de ruptura
    Caso queira que o loop se repita, não use [ return ] (ex: tratamento do loop para input não desejado)
    """


# exemplo (consultar informações dentro da função)
def get_name(text_instruction, message_success, message_error):

    allowed = [
        ' ',
        *'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.split('.'),
        *'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.upper().split('.')
    ]

    # Forma de tratar erro (a intenção é que sejam incrementados no loop, e o valor de [no], não pode incrementar)
    yes = 0
    no = 0

    while True:

        this_input = input(text_instruction)

        # Aqui acontece a incrementação
        for letter in this_input:
            if letter in allowed:
                yes += 1
            else:
                no += 1

        # Aqui acontece o tratamento
        if no != 0:
            print(message_error)
            # Estando em um algoritmo contendo loop infinito, esses valores precisam ser resetados no input indesejado
            yes = 0
            no = 0
        else:
            print(message_success)
            # O loop encerra aqui pela presença do [return]
            return this_input
