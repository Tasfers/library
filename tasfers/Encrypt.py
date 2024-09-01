from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)


class AesCBC:
    @staticmethod
    def encrypt(data: str, key: bytes, iv: bytes) -> bytes:
        """
        Шифрует данные с использованием AES в режиме CBC.

        :param data: Данные для шифрования.
        :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
        :param iv: Инициализационный вектор (IV) длиной 16 байт.
        :return: Зашифрованные данные (в байтах).
        """
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data.encode('utf-8')) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_data

    @staticmethod
    def decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
        """
        Дешифрует данные с использованием AES в режиме CBC.

        :param data: Зашифрованные данные (в байтах).
        :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
        :param iv: Инициализационный вектор (IV) длиной 16 байт.
        :return: Дешифрованные данные (в байтах).
        """
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded_data = decryptor.update(data) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        return decrypted_data


# class AesGCM:
#     @staticmethod
#     def encrypt(data: bytes, key: bytes, nonce: bytes) -> tuple:
#         """
#         Шифрует данные с использованием AES в режиме GCM.
#
#         :param data: Данные для шифрования (в байтах).
#         :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
#         :param nonce: Уникальный номер (nonce) длиной 12 байт для режима GCM.
#         :return: Кортеж, содержащий зашифрованные данные (в байтах) и тег аутентификации (в байтах).
#         """
#         cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
#         encryptor = cipher.encryptor()
#         encrypted_data = encryptor.update(data) + encryptor.finalize()
#         return encrypted_data, encryptor.tag
#
#     @staticmethod
#     def decrypt(data: bytes, tag: bytes, nonce: bytes, key: bytes) -> bytes:
#         """
#         Дешифрует данные с использованием AES в режиме GCM.
#
#         :param data: Зашифрованные данные (в байтах).
#         :param tag: Тег аутентификации (в байтах), полученный при шифровании.
#         :param nonce: Уникальный номер (nonce) длиной 12 байт для режима GCM.
#         :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
#         :return: Дешифрованные данные (в байтах).
#         """
#         cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
#         decryptor = cipher.decryptor()
#         decrypted_data = decryptor.update(data) + decryptor.finalize()
#         return decrypted_data


class AsyncAesCBC:
    @staticmethod
    async def encrypt(data: str, key: bytes, iv: bytes) -> bytes:
        """
        Асинхронно шифрует данные с использованием AES в режиме CBC.

        :param data: Данные для шифрования (в байтах).
        :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
        :param iv: Инициализационный вектор (IV) длиной 16 байт.
        :return: Зашифрованные данные (в байтах).
        """
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            executor, AesCBC.encrypt, data, key, iv
        )

    @staticmethod
    async def decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
        """
        Асинхронно дешифрует данные с использованием AES в режиме CBC.

        :param data: Зашифрованные данные (в байтах).
        :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
        :param iv: Инициализационный вектор (IV) длиной 16 байт.
        :return: Дешифрованные данные (в байтах).
        """
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            executor, AesCBC.decrypt, data, key, iv
        )


# class AsyncAesGCM:
#     @staticmethod
#     async def encrypt(data: bytes, key: bytes, nonce: bytes) -> tuple:
#         """
#         Асинхронно шифрует данные с использованием AES в режиме GCM.
#
#         :param data: Данные для шифрования (в байтах).
#         :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
#         :param nonce: Уникальный номер (nonce) длиной 12 байт для режима GCM.
#         :return: Кортеж, содержащий зашифрованные данные (в байтах) и тег аутентификации (в байтах).
#         """
#         loop = asyncio.get_running_loop()
#         return await loop.run_in_executor(
#             executor, AesGCM.encrypt, data, key, nonce
#         )
#
#     @staticmethod
#     async def decrypt(data: bytes, tag: bytes, nonce: bytes, key: bytes) -> bytes:
#         """
#         Асинхронно дешифрует данные с использованием AES в режиме GCM.
#
#         :param data: Зашифрованные данные (в байтах).
#         :param tag: Тег аутентификации (в байтах), полученный при шифровании.
#         :param nonce: Уникальный номер (nonce) длиной 12 байт для режима GCM.
#         :param key: Ключ шифрования длиной 16, 24 или 32 байта (AES-128, AES-192, AES-256).
#         :return: Дешифрованные данные (в байтах).
#         """
#         loop = asyncio.get_running_loop()
#         return await loop.run_in_executor(
#             executor, AesGCM.decrypt, data, tag, nonce, key
#         )
