
def shapka_cheka():
    import datetime
    print("......................")
    print("\n")
    print("ЧЕК ИЗ МАГАЗИНА ВОСЬМЁРОЧКА")
    print("\n")
    date_obj = datetime.datetime.now()
    print(date_obj)
    print("\n")

chek = {}

def product():
    for key, value in chek.items():
        print(f"Продукт: {key}, Цена: {value} \n")

def summa(sum=0):
    for c in chek.values():
        sum = c + sum
    print("----------------------")
    print(sum)
    print("......................")


chek["Фунчоза"] = 129
chek["Пицца"] = 500


