import discord
import subprocess




if __name__ == '__main__':
    input_text = str(input())
    hoge = subprocess.run(["node", "vimhelp.js", input_text], encoding='utf-8', stdout=subprocess.PIPE)
    print(hoge.stdout)
