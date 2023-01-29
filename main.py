import argparse
import os
from PIL import Image
from tqdm import tqdm
from colorama import Fore, Style

def convert_images(folder):
    files_count = 0
    for subdir, dirs, files in os.walk(folder):
        files_count += len(files)
    with tqdm(total=files_count, desc="Converting Images", unit="files", dynamic_ncols=True, leave=False) as pbar:
        for subdir, dirs, files in os.walk(folder):
            for file in files:
                try:
                    filepath = os.path.join(subdir, file)
                    if not file.endswith(".jpg"):
                        with Image.open(filepath) as img:
                            new_filepath = os.path.join(subdir, os.path.splitext(file)[0] + ".jpg")
                            img.save(new_filepath, "JPEG")
                            os.remove(filepath) 
                            pbar.update(1)
                            print(f"{Fore.GREEN}Converted {file} to {new_filepath}{Style.RESET_ALL}")
                    else:
                        pbar.update(1)
                        print(f"{Fore.YELLOW}Skipped {file}, already in jpeg format.{Style.RESET_ALL}")
                except OSError as e:
                    pbar.update(1)
                    print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert all images in a folder and its subfolders to jpg format')
    parser.add_argument('folder', help='The path of the folder containing images')
    args = parser.parse_args()
    convert_images(args.folder)
