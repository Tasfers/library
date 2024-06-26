import aiofiles


async def write_text_to_file(file_path: str, text: str):
    """
    Асинхронно записывает текст в файл. Если файл существует, добавляет текст с новой строки.
    Если файла нет, создаёт его и записывает текст.

    :param file_path: Путь к файлу
    :param text: Текст для записи
    """
    try:
        async with aiofiles.open(file_path, mode='a', encoding='utf-8') as file:
            await file.write(text + '\n')
    except IOError as e:
        print(f"Ошибка при работе с файлом: {e}")
