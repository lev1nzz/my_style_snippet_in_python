'''
Мои стилевые паттерны для работы с Python
'''

# 1. Наименование функций.
def used_only_snake_case() -> dict: ...
def typecil_heats(var_1: int, var_2: str) -> bool: ...
def convert_string_to_slug() -> str: ...

# 2. Структура типичной функции.
def my_typical_function(input_data: list[int]) -> list[int]:
	"""Краткое описание, что делает функция."""

	# Валидация.
	if not input_data:
		return []

	# Обработка.
	processed_data = [item.upper() for item in input_data]

	# Результат.
	return processed_data

# 3. Мои люьбимые конструкции.
def find_item_by_id(item_id: int, items: list) -> dict | None:
	"""Поиск элемента по ID с безопасным возвратом."""
	return next((item for item in items if item['id'] == item_id), None)
