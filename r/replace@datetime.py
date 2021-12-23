

from datetime import datetime
from metodos_bdd.month_converter import month_converter_int_str
from metodos_bdd.day_suffix_manager import day_suffix_manager

# "Método [ replace() ] pode ser útil para, por exemplo, mandar e-mails agendados [ não sei como fazer isso ]"

if __name__ == '__main__':

    # Suposto dia da compra
    print(day_purchase := datetime.now())

    # Com o método [ replace ] pode se fazer uma previsão de pagamento
    print(day_payment := day_purchase.replace(year=day_purchase.year,
                                              month=day_purchase.month + 1,
                                              day=day_purchase.day,
                                              hour=day_purchase.hour,
                                              minute=day_purchase.minute,
                                              second=day_purchase.second
                                              ))

    """ ---------------------------------------- Lógica para os meses seguintes ----------------------------------------
    print(day_payment_2nd := day_purchase.replace(year=day_payment.year,
                                                  month=day_payment.month + 1,
                                                  day=day_payment.day,
                                                  hour=day_payment.hour,
                                                  minute=day_payment.minute,
                                                  second=day_payment.second
                                                  ))
                                                  
    payment_2nd_date = (day_payment_2nd.year, day_payment_2nd.month, day_payment_2nd.day)
    payment_2nd_hour = (day_payment_2nd.hour, day_payment_2nd.minute, day_payment_2nd.second)
    
    day_payment_2nd_suffix = day_suffix_manager(day=str(payment_2nd_date[2]))
    month_payment_2nd_str = month_converter_int_str(month=payment_2nd_date[1])
    """

    # Os dados precisam ser separados em tuplas, tanto do dia da compra, quanto do pagamento
    purchase_date = (day_purchase.year, day_purchase.month, day_purchase.day)
    purchase_hour = (day_purchase.hour, day_purchase.minute, day_purchase.second)

    payment_date = (day_payment.year, day_payment.month, day_payment.day)
    payment_hour = (day_payment.hour, day_payment.minute, day_payment.second)

    # São usados métodos customizados para converter os valores de dia e mês para string
    day_purchase_suffix = day_suffix_manager(day=str(purchase_date[2]))
    day_payment_suffix = day_suffix_manager(day=str(payment_date[2]))

    month_purchase_str = month_converter_int_str(month=purchase_date[1])
    month_payment_str = month_converter_int_str(month=payment_date[1])

    # print(month_purchase_str, month_payment_str)

    print(report := f"""
        Date of the purchase     || {purchase_date[0]} {month_purchase_str} {day_purchase_suffix} at {purchase_hour[0]}:{purchase_hour[1]}:{purchase_hour[2]}
        Data of the next payment || {payment_date[0]} {month_payment_str} {day_payment_suffix} at {payment_hour[0]}:{payment_hour[1]}:{payment_hour[2]}
        """)
