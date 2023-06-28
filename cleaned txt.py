import codecs


def delete_html_tags(html_file, cleaned_file="cleaned.txt"):
    with codecs.open(html_file, "r", encoding="utf-8") as file:

        clean_text = ""
        inside_tag = False

        for line in file:
            for char in line:
                if char == "<":
                    inside_tag = True
                elif char == ">":
                    inside_tag = False
                elif not inside_tag:
                    clean_text += char

    with codecs.open(cleaned_file, "w", encoding="utf-8") as file:
        file.write(clean_text)

    print(f"Cleaning is done,new file: {cleaned_file}")


delete_html_tags("draft.html", "cleaned.txt")
