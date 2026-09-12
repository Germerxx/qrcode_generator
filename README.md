# QR Code Generator (Python)

A simple console-based QR code generator written in Python. Uses the [qrcode](https://pypi.org/project/qrcode/) library.

## Installation

```bash
pip install qrcode[pil]
```

## Usage

Just run the file — it will ask for a link and print the QR code directly in the console:

```bash
python qr_generator.py
```

```
Введите ссылку: https://example.com
```

The QR code appears right in the terminal (ASCII art) and is also saved as `qr.png` in the same folder.

You can also run it with arguments:

```bash
python qr_generator.py "https://example.com" qr.png 10
```

- 1st argument — text or link to encode
- 2nd argument (optional) — output file name (default: `qr.png`)
- 3rd argument (optional) — size of one QR code box in pixels, `box_size` (default: `10`)

> For the best-looking result in the console, use a terminal with a dark background and a monospace font (e.g. Windows Terminal or PowerShell). In classic `cmd.exe` the code may look slightly squished vertically, but it will still scan correctly.

## Project structure

```
qr-python/
├── qr_generator.py
└── README.md
```

## License

MIT

---

# QR Code Generator (Python) — на русском

Простой консольный генератор QR-кодов на Python. Использует библиотеку [qrcode](https://pypi.org/project/qrcode/).

## Установка

```bash
pip install qrcode[pil]
```

## Использование

Просто запусти файл — он спросит ссылку и выведет QR-код прямо в консоли:

```bash
python qr_generator.py
```

```
Введите ссылку: https://example.com
```

QR-код появится прямо в терминале (ASCII-графика), а также сохранится в файл `qr.png` в той же папке.

Можно также запустить с аргументами:

```bash
python qr_generator.py "https://example.com" qr.png 10
```

- 1-й аргумент — текст или ссылка для кодирования
- 2-й аргумент (необязательный) — имя выходного файла (по умолчанию `qr.png`)
- 3-й аргумент (необязательный) — размер одного квадратика QR-кода в пикселях, `box_size` (по умолчанию `10`)

> Для аккуратного отображения в консоли лучше использовать терминал с тёмным фоном и моноширинным шрифтом (например, Windows Terminal или PowerShell). В обычном `cmd.exe` код может выглядеть немного сплющенным по вертикали, но при этом он всё равно останется сканируемым.

## Структура проекта

```
qr-python/
├── qr_generator.py
└── README.md
```

## Лицензия

MIT
