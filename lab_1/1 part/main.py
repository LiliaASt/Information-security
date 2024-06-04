import json

def read_text_from_file(file_name: str) ->str:
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

def read_key_from_file(file_name: str)->int:
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
            key = data["key"]
        return key
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except ValueError:
        print(f"Неверный формат ключа в файле '{file_name}'. Ключ должен быть целым числом.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_name}': {e}")
        return None

def write_text_to_file(text: str, file_name: str)->None:
    try:
        with open(file_name, 'w',encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл '{file_name}': {e}")


def encode_scytale(text:str, key: int)->str:
    encoded_text = [''] * key
    for i, char in enumerate(text):
        index = i % key
        encoded_text[index] += char
    return ''.join(encoded_text)

def decode_scytale(text:str, key: int)->str:
    decoded_text = [''] * 86
    for i, char in enumerate(text):
        index = i% 86
        decoded_text[index] += char
    return ''.join(decoded_text)

if __name__ == "__main__":
    input_text = read_text_from_file(r"C:/Users/lasts/projects/Information-security/lab_1/1 part/original_text.txt")
    substitution = read_key_from_file(r"C:/Users/lasts/projects/Information-security/lab_1/1 part/key.json")
    if input_text is not None and substitution is not None:
        encrypted_text = encode_scytale(input_text, substitution)
        write_text_to_file(encrypted_text, r"C:/Users/lasts/projects/Information-security/lab_1/1 part/encrypted.txt")
        decoded_text = decode_scytale(encrypted_text, substitution)
        write_text_to_file(decoded_text, r"C:/Users/lasts/projects/Information-security/lab_1/1 part/decoded.txt")
