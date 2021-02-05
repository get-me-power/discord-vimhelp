import subprocess


def vimhelp(search_word):
    help_index = subprocess.run(["node", "../vimhelp.js", search_word],
                                encoding='utf-8', stdout=subprocess.PIPE)
    return help_index.stdout, help_index.returncode
