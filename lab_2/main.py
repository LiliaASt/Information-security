import json

from math import erfc, fabs, sqrt, pow
from scipy.special import gammainc
from path import (
    gen_sequence,
    result)

def frequency_test(number: str) -> float:
    try:
        sum = 0
        for x in number:
            if x == '1':
                sum+=1
            else:
                sum-=1
        value = erfc(fabs(sum)/sqrt(2*len(number)))
        return value

    except Exception as e:
        print(f"Произошла ошибка при чтении '{number}': {e}")
        return None

def same_bits_test (number: str) -> float:
    try:
        long = len(number)
        sum = 0
        for x in number:
            sum+=int(x)
        e = sum/long

        if fabs(e - 0.5) >= (2/sqrt(long)):
            return 0
        V_n = 0
        for i in range(0, long - 1):
            if number[i] != number[i+1]:
                V_n += 1
        value = erfc(fabs(V_n - 2*long*e*(1-e))/(2*sqrt(2*long)*e*(1-e)))
        return value

    except Exception as e:
        print(f"Произошла ошибка при чтении '{number}': {e}")
        return None

if __name__ == "__main__":
    try:
        with open(gen_sequence, 'r', encoding="utf-8") as file:
            data = json.load(file)
            cpp_sequence = data['cpp']
            java_sequence = data['java']

        cpp_results = {
            "frequency_test": frequency_test(cpp_sequence),
            "same_bits_test": same_bits_test(cpp_sequence),
        }
        print (cpp_results)

        java_results = {
            "frequency_test": frequency_test(java_sequence),
            "same_bits_test": same_bits_test(java_sequence),
        }
        print (java_results)

        with open(result, 'w', encoding="utf-8") as file:
            file.write("C++ Results:\n")
            file.write(json.dumps(cpp_results, indent=4))
            file.write("\n\nJava Results:\n")
            file.write(json.dumps(java_results, indent=4))

    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError as e:
       print(f"Ошибка: Нет прав для записи - {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
