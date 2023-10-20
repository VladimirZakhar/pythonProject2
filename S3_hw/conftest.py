import pytest
from checkout import checkout
from yaml_reader import data
import time


@pytest.fixture()
def make_folder():
    yield checkout(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ext")}', '')
    checkout(f'rm -r {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ext")}', '')

@pytest.fixture()
def make_files():
    return checkout(f'cd {data.get("folder_in")}; touch file1.txt file2.txt file3.txt', '')

@pytest.fixture(autouse=True)
def write_test_statistics():
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    num_files = len(data.get('files', []))
    file_size = data.get('file_size', 0)

    with open('/proc/loadavg', 'r') as loadavg_file:
        processor_load = loadavg_file.read()

    statistics_line = (
        f'Timestamp: {timestamp}\n'
        f'Number of Files: {num_files}\n'
        f'File Size: {file_size} bytes\n'
        f'Processor Load Statistics:\n{processor_load}'
    )

    with open(data.get('stat_file'), 'a') as stat_file:
        stat_file.write(statistics_line + '\n')
