import logging
import os
import time

logging.basicConfig(level=logging.INFO, filename='example.log', encoding='utf-8', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

consoleloger = logging.StreamHandler()
consoleloger.setLevel(logging.INFO)
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleloger.setFormatter(console_format)
logger.addHandler(consoleloger)

deleted_files = 0

class FileError():
    def __init__(self, message, filename, filemodetime):
        self.message = message
        self.filename = filename
        self.filemodetime = filemodetime
        logger.error(f"Файл {filename} {message} [LAST EDITED {time.ctime(filemodetime)}]")

def delete_old_files(directory, days=30):
    global deleted_files
    current_time = time.time()
    logger.info(f"Directory /{directory}/")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            file_mod_time = os.path.getmtime(file_path)
            if current_time - file_mod_time > days * 86400:
                deleted_files = deleted_files + 1
                os.remove(file_path)
                logger.warning(f"{filename} [LAST EDITED {time.ctime(file_mod_time)}][DELETED]")

            else:
                logger.info(f"{filename} [LAST EDITED {time.ctime(file_mod_time)}]")
        except FileNotFoundError:
            logger.warning(f"Файл {filename} вже було видалено.")
        except PermissionError:
            error = FileError(f"Виникла помилка при обробці файлу бо він використовується іншою програмою чи процесом але він мав бути видалений", filename, file_mod_time)

        except Exception as e:
            error = FileError(f"Виникла помилка при обробці файлу але він мав бути видалений", filename, file_mod_time)

directory_path = "poligon"
delete_old_files(directory_path)
print(f"{deleted_files} file deleted")
