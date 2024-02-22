import argparse
import os


def nl(input_file=None, num_lines=None, output_file=None):
    # Проверяем, передан ли файл и существует ли он
    if input_file and os.path.isfile(input_file):
        # Если файл существует, читаем строки из файла
        with open(input_file, 'r') as file:
            lines = file.readlines()
    else:
        # Если файл не передан или не существует, читаем строки из stdin
        lines = [input() for _ in range(num_lines)]

    # Выводим пронумерованные строки в консоль
    for i, line in enumerate(lines, start=1):
        print(f"{i}\t{line.strip()}")

    # Если указан файл для записи, записываем туда вывод
    if output_file:
        with open(output_file, 'w') as out_file:
            for i, line in enumerate(lines, start=1):
                out_file.write(f"{i}\t{line.strip()}\n")


if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Print numbered lines from a file or stdin.")
    default_file = os.path.abspath("task_1")
    parser.add_argument("file", nargs="?", default=default_file, help="Input file (default: task_1.txt)")
    parser.add_argument(
        "-n",
        "--num-lines",
        type=int,
        default=5,
        help="Number of lines to read from stdin (default: 5)")
    parser.add_argument(
        "-o",
        "--output-file",
        default="artifacts/artifact_1.txt",
        help="Output file (default: artifact_1.txt)")
    args = parser.parse_args()

    # Вызываем функцию nl с переданными аргументами
    nl(input_file=args.file, num_lines=args.num_lines, output_file=args.output_file)
