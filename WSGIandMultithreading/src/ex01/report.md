## Инструкции к Упражнению 01
### Запустите Python-сервер:
```bash
make venv
source venv/bin/activate
python server.py
```
Это запустит сервер на localhost с портом 8888.

### Во втором терминале выполните следующую команду для тестирования сервера:

Активация виртуального окружения Python:
   ```bash
   source venv/bin/activate
   ```

Загрузка локального аудиофайла на сервер:
   ```bash
   python screwdriver.py upload /path/to/file.mp3
   ```

Получение списка имен файлов на сервере:
   ```bash
   python screwdriver.py list
   ```