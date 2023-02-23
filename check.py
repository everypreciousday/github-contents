# -*- conding: utf-8 -*-
import time
import pprint
import re
import os.path
from pathlib import Path
import subprocess
import traceback
import os
import sys
import logging
import yaml
pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler(f"log.txt", encoding="UTF-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

def main():
    with open('versions.yml', encoding='UTF8') as file:
        yaml_obj = yaml.safe_load(file)
        for book in yaml_obj:
            print("--------")
            print(f"book: {book}")
            book_obj = yaml_obj[book]

            book_version = book_obj['version']
            book_language = book_obj['language']
            book_chapters = book_obj['chapters']

            print(book_version)
            print(book_language)
            for book_chapter in book_chapters:
                filename = book_chapter['filename']
                print(filename)
                if ".yml" not in filename:
                    continue
                with open(book + "/" + filename, encoding='utf-8') as file:
                    content_dict = yaml.safe_load(file)
                    chapter = content_dict['chapter']
                    title = content_dict['title']
                    content = content_dict['content']
                    print(f"chapter: {chapter}")
                    print(f"title: {title}")
                    for para in content:
                        print(">>>>")
                        lines = para['lines']
                        for line in lines:
                            print(line)
                        vocas = para['vocas']
                        for voca in vocas:
                            print(voca)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
        print(traceback.format_exc())