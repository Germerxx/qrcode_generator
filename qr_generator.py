import sys
import qrcode


def generate(text: str, output_file: str = "qr.png", size: int = 10):
    """
    Генерирует QR-код: показывает его прямо в консоли и сохраняет в PNG-файл.

    :param text: текст или ссылка для кодирования
    :param output_file: имя выходного файла
    :param size: размер одного "квадратика" QR-кода в пикселях (box_size)
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=size,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # выводит QR-код прямо в консоль (ASCII)
    qr.print_ascii(invert=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)


def main():
    if len(sys.argv) >= 2:
        text = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) >= 3 else "qr.png"
        size = int(sys.argv[3]) if len(sys.argv) >= 4 else 10
    else:

        text = input("Введите ссылку: ")
        output_file = "qr.png"
        size = 10

    generate(text, output_file, size)

    print(f"QR-код также сохранён в файл: {output_file}")
    input("Нажмите Enter, чтобы закрыть...")


if __name__ == "__main__":
    main()
