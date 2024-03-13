import os
import subprocess

from latex_generator.latex_generator import generate_latex_with_image

if __name__ == "__main__":
    example_data = [
        ["Header 1", "Header 2", "Header 3"],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    image_path = "artifacts/image.png"

    latex_code_with_image = generate_latex_with_image(example_data, image_path)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    artifacts_directory = os.path.join(script_directory, "artifacts")
    os.makedirs(artifacts_directory, exist_ok=True)

    tex_file_path = os.path.join(artifacts_directory, "artifact_1.tex")
    pdf_file_path = os.path.join(artifacts_directory, "artifact_1.pdf")

    with open(tex_file_path, "w") as file:
        file.write(latex_code_with_image)

    pdflatex_path = r'C:\Users\nevsk\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe'

    subprocess.run([pdflatex_path, "-output-directory", artifacts_directory, tex_file_path])

    print(f"PDF generated at: {pdf_file_path}")

# Установка созданной библиотеки
# pip install latex-generator==0.6 