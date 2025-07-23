from fractions import Fraction

def fraction_calculator():
    print("Дробный калькулятор (введите 'exit' для выхода)")
    while True:
        try:
            expr = input("Введите выражение (например, '3/4 + 1/2'): ").strip()
            if expr.lower() == 'exit':
                break
            
            parts = expr.split()
            a = Fraction(parts[0])
            op = parts[1]
            b = Fraction(parts[2])
            
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                res = a / b
            else:
                print("Ошибка: неизвестная операция")
                continue
            
            print(f"Результат: {res}")
        
        except (ValueError, IndexError):
            print("Ошибка: некорректный ввод. Пример: '1/2 + 3/4'")

fraction_calculator()