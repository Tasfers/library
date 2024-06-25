import asyncio
import io
from .async_funcs import write_text_to_file as async_write_text_to_file


def write_text_to_file(file_path: str, text: str):
    """
    Записывает текст в файл. Если файл существует, добавляет текст с новой строки.
    Если файла нет, создаёт его и записывает текст.

    :param file_path: Путь к файлу
    :param text: Текст для записи
    """
    asyncio.run(async_write_text_to_file(file_path, text))


def text_to_bytes(text: str) -> io.StringIO:
    """
    Создает объект StringIO и записывает в него переданный текст. Затем перемещает указатель чтения/записи в начало, чтобы можно было прочитать записанные данные.

    :param text: Текст для записи в объект StringIO.
    :return: Объект StringIO с записанным текстом.
    """
    string_io = io.StringIO()
    string_io.write(text)
    string_io.seek(0)
    return string_io
