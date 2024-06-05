import json
import collections


def read_text_from_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_name}': {e}")
        return None


def read_key_from_file(file_name: str) -> dict:
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
            key = data
        return key
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except ValueError:
        print(f"Неверный формат ключа в файле '{
              file_name}'. Ключ должен быть целым числом.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_name}': {e}")
        return None


def write_text_to_file(text: str, file_name: str) -> None:
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл '{file_name}': {e}")


def write_key_to_file(data: dict, file_name: str) -> None:
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Ключ успешно записан в файл '{file_name}'.")
    except Exception as e:
        print(f"Произошла ошибка при записи ключа в файл '{file_name}': {e}")


def calculate_frequency(file_name: str) -> None:
    frequency = {}
    data = read_text_from_file(file_name).lower().replace('\n', '')

    frequency = collections.Counter(data)
    total = len(data)
    normalized_frequency = {char: count /
                            total for char, count in frequency.items()}
    sorted_frequency = dict(
        sorted(normalized_frequency .items(), key=lambda x: x[1], reverse=True))
    return sorted_frequency


def generate_decryption_key(encrypted_frequency: str, rus_frequency: str) -> dict:
    decryption_mapping = dict(zip(encrypted_frequency, rus_frequency))
    return decryption_mapping


def decode_text(text: str, key: dict) -> str:
    decoded_text = ''.join(str(key.get(char, char)) for char in text)
    return decoded_text


if __name__ == "__main__":
    encrypted_text = read_text_from_file(
        r'C:/Users/lasts/projects/Information-security/lab_1/2 part/code4.txt')
    encrypted_frequency = calculate_frequency(
        r'C:/Users/lasts/projects/Information-security/lab_1/2 part/code4.txt')
    write_key_to_file(encrypted_frequency,
                      r'C:/Users/lasts/projects/Information-security/lab_1/2 part/tex_frequencies.json')
    rus_frequency = read_key_from_file(
        r'C:/Users/lasts/projects/Information-security/lab_1/2 part/rus_frequencies.json')
    key = generate_decryption_key(encrypted_frequency, rus_frequency)
    decod = decode_text(encrypted_text, read_key_from_file(
        r'C:/Users/lasts/projects/Information-security/lab_1/2 part/key.json'))
    write_text_to_file(
        decod, r'C:/Users/lasts/projects/Information-security/lab_1/2 part/decoded.txt')
