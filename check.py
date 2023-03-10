# -*- conding: utf-8 -*-
import traceback
import yaml


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

            print(f"book_version:{book_version}")
            print(f"book_language:{book_language}")
            for book_chapter in book_chapters:
                filename = book_chapter
                print(f"filename:{filename}")
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
                        if 'vocas' in para:
                            vocas = para['vocas']
                            for voca in vocas:
                                print(voca)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        print(traceback.format_exc())