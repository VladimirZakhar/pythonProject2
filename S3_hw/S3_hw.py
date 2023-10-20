# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл
# stat.txt строку вида: время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки
# процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

from checkout import checkout
from yaml_reader import data
import pytest


class TestsPositive:

    def test_step1(self, make_folder, make_files):
        assert checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}arch",
                        "Everything is Ok"), "test1 FAIL"

    def test_step2(self, make_folder, make_files):
        assert checkout(f"cd {data.get('folder_out')}; 7z d arch.7z file1.txt", "Everything is Ok"), "test2 FAIL"

    # def test_step3(self, make_folder, make_files):
    #     assert checkout(f"cd {data.get('folder_out')}; 7z l arch.7z", "Name\n"), "test3 FAIL"
    #
    # def test_step4(self, make_folder, make_files):
    #     assert checkout(f"cd {data.get('folder_out')}; 7z x arch.7z -o{data.get('folder_ext')} -y",
    #     "Everything is Ok"), "test4 FAIL"


if __name__ == '__main__':
    pytest.main(["-vv"])
