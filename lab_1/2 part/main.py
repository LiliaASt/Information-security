import json
import collections

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

def read_key_from_file(file_name: str)->dict:
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
            key = data
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

def write_key_to_file(data: dict, file_name:str)->None:
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Ключ успешно записан в файл '{file_name}'.")
    except Exception as e:
        print(f"Произошла ошибка при записи ключа в файл '{file_name}': {e}")
