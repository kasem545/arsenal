#!/usr/bin/env python3

import re
import sys


def process_text(text):
    text = re.sub(r"{{/([^}]*)}}", r"{{\1}}", text)
    
    def replace_placeholder(match):
        placeholder = match.group(1)
        if not placeholder.startswith("~/"):
            placeholder = placeholder.replace("/", "_")
        return "<" + placeholder + ">"
    
    return re.sub(r"{{([^}]*)}}", replace_placeholder, text)


if __name__ == "__main__":
    text = sys.stdin.read()
    print(process_text(text), end='')
