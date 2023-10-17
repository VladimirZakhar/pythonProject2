# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


folder_in = "/home/gt/folder_in/"
folder_out = "/home/gt/folder_out/"
folder_ext = "/home/gt/folder_ext/"


def test_step1():
    assert checkout(f"cd {folder_in}; 7z a {folder_out}arch", "Everything is Ok"), "test1 FAIL"


def test_step2():
    assert checkout(f"cd {folder_out}; 7z d arch file1.txt", "Everything is Ok"), "test2 FAIL"


def test_step3():
    assert checkout(f"cd {folder_out}; 7z l arch.7z", "Name\n"), "test3 FAIL"


def test_step4():
    assert checkout(f"cd {folder_out}; 7z x arch.7z -o{folder_ext}", "Everything is Ok"), "test4 FAIL"
