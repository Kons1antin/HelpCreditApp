from getDate import GetDate

class DeffPay():
    def __init__(self,all_sum,period,annual_rate) -> None:
        self.all_sum = all_sum
        self.period = period
        self.annual_rate = annual_rate



    def get_all_pay(self) -> list:
        #Список платежей ежемесячных
        list_pay = []

        # Сумма для погашения долга без процента
        month_pay_clear = self.all_sum / self.period

        # Ежемесячная ставка
        monthly_rate = ((self.annual_rate / 12) / 100)

        count = self.all_sum


        for n in range(self.period):
            accrued_interest = count * monthly_rate
            count -= month_pay_clear
            list_pay.append(month_pay_clear + accrued_interest)

        return list_pay

    # Общая сумма выплат
    def total_pay(self) -> float:
        return sum(self.get_all_pay())

    # Выплаты банку
    def pay_bank(self):
        return self.total_pay() - self.all_sum


    # Приблизительный средний платёж каждый месяц
    def midl_pay_month(self):
        return self.total_pay() / self.period

    # Процент выплаченный банку от общей суммы
    def percent_pay(self):
        return (self.pay_bank() * 100) / self.all_sum



class AnnuitPay():

    def __init__(self,all_sum,period,annual_rate):
        self.all_sum = all_sum
        self.period = period
        self.annual_rate = annual_rate

    # Расчёт ежемесячного платежа
    def month_pay(self):
        p = (self.annual_rate / 100) / 12
        return self.all_sum * (p + (p /(((1 + p) ** self.period) - 1)))

    # Общая сумма выплат
    def total_pay(self):
        return self.month_pay() * self.period


    # Выплаты банку
    def pay_bank(self):
        return self.total_pay() - self.all_sum

    # Процент выплаченный банку от общей суммы
    def percent_pay(self):
        return (self.pay_bank() * 100) / self.all_sum


    def calc_reduc_pay(self) -> float:
        p = (self.annual_rate / 100) / 12
        target = self.month_pay() - GetDate().get_date_reduce_pay()

        new_summ = target / (p + (p /(((1 + p) ** self.period) - 1)))
        return  new_summ






if __name__ == "__main__":
    # print(DeffPay(200000,24,18.5,9192).get_all_pay())
    # print(sum(DeffPay(200000,24,18.5,9192).get_all_pay()))
    # print(DeffPay(100000,12,18.5,9192).get_fix_pay())
    print(AnnuitPay(200000, 24, 18.5).month_pay())
    print(AnnuitPay(200000, 24, 18.5).calc_reduc_pay())
