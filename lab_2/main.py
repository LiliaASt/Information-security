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

def long_sequence_test (number: str) -> float:
    try:
        size = 8
        pi = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}
        v = {0: 0, 1: 0, 2: 0, 3: 0}
        blocks = [number[i:i+size] for i in range(0, len(number), size)]

        for block in blocks:
            current = 0
            current_max = 0
            for i in block:
                if i == '1':
                    current += 1
                    current_max = max(current_max, current)
                else:
                    current = 0

            if current_max <= 1:
                v[0] += 1
            elif current_max == 2:
                v[1] += 1
            elif current_max == 3:
                v[2] += 1
            elif current_max >= 4:
                v[3] += 1

            X = 0
            for i in range(4):
                X += pow((v[i]-16*pi[i]), 2)/(16*pi[i])
            value = gammainc(1.5, (X/2))
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
            "long_sequence_test ": long_sequence_test(cpp_sequence)
        }
        print (cpp_results)

        java_results = {
            "frequency_test": frequency_test(java_sequence),
            "same_bits_test": same_bits_test(java_sequence),
            "long_sequence_test ": long_sequence_test(java_sequence)
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
