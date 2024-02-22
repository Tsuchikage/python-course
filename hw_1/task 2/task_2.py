# TODO: доделать ввод польщзователя и несколько файлов

import argparse

import os

def tail(file_paths, num_lines=10, output_file=None):
    for file_path in file_paths:
        print(f"==> {file_path} <==")
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                result = '\n'.join(lines[-num_lines:])
                print(result)
                if output_file:
                    with open(output_file, 'a') as out_file:
                        out_file.write(f"==> {file_path} <==\n")
                        out_file.write(result)
        else:
            print(f"Error: File '{file_path}' not found.")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Print the last 10 lines of each specified file or 17 lines from stdin.")
    parser.add_argument("files", nargs="*", help="Input files")
    parser.add_argument(
        "-n",
        "--num-lines",
        type=int,
        default=10,
        help="Number of lines to print for each file (default: 10)")
    parser.add_argument(
        "-o",
        "--output-file",
        default="artifacts/artifact_2.txt",
        help="Output file (default: artifact_2.txt)")
    args = parser.parse_args()

    if not args.files:
        args.files.append("task_2")

    tail(args.files, num_lines=args.num_lines, output_file=args.output_file)
