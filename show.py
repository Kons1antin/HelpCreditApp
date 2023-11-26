from logic import DeffPay, AnnuitPay
from getDate import GetDate
import numpy as np
import pandas as pd


class ShowDeffPay():

    def __init__(self):
        self.summ = GetDate().get_start_date()[0]
        self.per = GetDate().get_start_date()[1]
        self.ann = GetDate().get_start_date()[2]




    def show_pay_month(self) -> None:

        l = [round(i,2) for i in DeffPay(self.summ,self.per,self.ann).get_all_pay()]

        dict_date = {"Сумма выплат": l}
        print(pd.DataFrame(dict_date))


    def show_pay_all_time(self) -> None:
        print(f'Общая сумма выплат: {round(DeffPay(self.summ,self.per,self.ann).total_pay(),2)} руб')

    def show_pay_bank(self) -> None:
        print(f'Выплаты банку: {round(DeffPay(self.summ,self.per,self.ann).pay_bank(),2)} руб')

    def show_percent_pay(self) -> None:
        print(f'Процент выплаченный банку от общей суммы: {round(DeffPay(self.summ,self.per,self.ann).percent_pay(),1)} %')


class ShowAnnuitPay():

    def __init__(self):
        self.summ = GetDate().get_start_date()[0]
        self.per = GetDate().get_start_date()[1]
        self.ann = GetDate().get_start_date()[2]


    def show_month_pay(self) -> None:
        print(f'Ежемесячная выплата: {round(AnnuitPay(self.summ,self.per,self.ann).month_pay(),2)} руб')

    def show_pay_all_time(self) -> None:
        print(f'Общая сумма выплат: {round(AnnuitPay(self.summ,self.per,self.ann).total_pay(),2)} руб')

    def show_pay_bank(self) -> None:
        print(f'Выплаты банку: {round(AnnuitPay(self.summ,self.per,self.ann).pay_bank(),2)} руб')

    def show_percent_pay(self) -> None:
        print(f'Процент выплаченный банку от общей суммы: {round(AnnuitPay(self.summ,self.per,self.ann).percent_pay(),1)} %')

    def show_reduc_pay(self)-> None:
        print(f'Ежежмесячная сумма выплат будет составлять: {round(AnnuitPay(self.summ,self.per,self.ann).calc_reduc_pay()[1],2)} руб')
        print(f'Взнос банку составит: {round(AnnuitPay(self.summ,self.per,self.ann).calc_reduc_pay()[0],2)} руб')
        print(f'Общая сумма выплат составит: {round(AnnuitPay(self.summ,self.per,self.ann).calc_reduc_pay()[2],2)} руб')

    def show_reduc_period(self)-> None:
        print(f'Ежежмесячная сумма выплат будет составлять: {round(AnnuitPay(self.summ,self.per,self.ann).calc_reduc_period()[0],2)} руб')
        print(f'Общая сумма переплаты банку: {round(AnnuitPay(self.summ,self.per,self.ann).calc_reduc_period()[1],2)} руб')