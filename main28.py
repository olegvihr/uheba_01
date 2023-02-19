try:
    x, y = map(int, input().split())
    res = x / y
except ValueError:
    print("Ошибка типа данных")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except Exception:
    print("Ошибка Exception")
except:
    print("Ошибка")

print("Штатное завершение")