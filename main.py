from logic import DeffPay, AnnuitPay
from show import ShowDeffPay, ShowAnnuitPay
from getDate import GetDate


def main():
    '''
    #Сумма указывается в рублях -> integer or long
    all_sum = 0

    # Период указывается в месяцах -> integer
    period = 0

    # Ставка указывается за год -> float
    annual_rate = 0.0

    # Способ погашения кредита ( 0 if аннуитетный ; 1 if деференцированный ) -> boolean default False
    type_pay = False
    '''

    # ShowDeffPay().show_pay_month()
    # ShowDeffPay().show_pay_all_time()
    # ShowDeffPay().show_pay_bank()
    # ShowDeffPay().show_percent_pay()

    ShowAnnuitPay().show_month_pay()
    ShowAnnuitPay().show_pay_all_time()
    ShowAnnuitPay().show_pay_bank()
    ShowAnnuitPay().show_percent_pay()

if __name__ == '__main__':
    main()
