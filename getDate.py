

class GetDate():

    def get_start_date(self):
        # Сумма указывается в рублях -> integer or long
        all_sum = 200000


        # Период указывается в месяцах -> integer
        period = 24


        # Ставка указывается за год -> float
        annual_rate = 18.5


        # Способ погашения кредита ( 0 if аннуитетный ; 1 if деференцированный ) -> boolean default False
        type_pay = False


        #Предпочтения плательщика (0 if операция игнорируется; 1 if уменьшить сумму выплат; 2 if уменьшить период выплат) -> integer default 0
        credit_metgod = 0

        return all_sum,period,annual_rate,type_pay, credit_metgod


    def get_date_reduce_pay(self) -> int:

        # На какую сумму плательщик желает уменьшить ежемесячный платёж -> integer
        reduce_pay = 3000

        return reduce_pay


