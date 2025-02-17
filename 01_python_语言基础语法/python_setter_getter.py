#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/1/14 15:20
# @Author : limber
# @desc :


class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount


if __name__ == '__main__':
    bank_account = BankAccount("xiaoming", 100)
    print(bank_account.balance)
    bank_account.balance = 10000
    print(bank_account.balance)
