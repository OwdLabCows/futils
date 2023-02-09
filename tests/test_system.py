import pytest
import datetime
from pathlib import Path
import os
import shutil
# import SystemUtils class from baseutil.py
from futils import SystemUtils
# typing
from typing import Dict, List


# content of test files
CONTENT = "Sample file for test"


@pytest.fixture
def directory(tmpdir: Path) -> str:
    # create base directory that contains some files or directories for test
    basedir_name = __name__ + \
        datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%f")
    # basedir = tmpdir.join(basedir_name)
    basedir = tmpdir / basedir_name
    basedir.mkdir()
    # create some files for test
    for i in range(4):
        testfile = basedir / f"test_{i}.file"
        testfile.write_text(CONTENT, encoding='utf-8')
    # create some directories for test
    for alp in ['a', 'b', 'c']:
        testdir = basedir / f"test_{alp}_d"
        testdir.mkdir()
    # create a directory having some files
    testdir = basedir / "test_havingsomefiles_d"
    testdir.mkdir()
    for i in range(3):
        testfile = testdir / f"test_{i}.file"
        testfile.write_text(CONTENT, encoding='utf-8')
        subtestdir = testdir / f"test_sub_havingsomefiles_{i}_d"
        subtestdir.mkdir()
        for j in range(2):
            subtestfile = subtestdir / f"test_sub_{j}.file"
            subtestfile.write_text(CONTENT, encoding='utf-8')
    # return basedir_name and stop
    yield basedir
    # finally remove basedir
    shutil.rmtree(str(basedir))


# test 'make_directories'
@pytest.mark.parametrize(('subpath', 'reset', 'exists'), [
    ("test_havingsomefiles_d", False, True),
    ("test_havingsomefiles_d", True, True),
    ("new_d", False, True),
    ("new_d", True, True),
])
def test_make_directories_exist(subpath, reset, exists, directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(str(directory), subpath)
    system_utils.make_directories(path, reset=reset)
    assert os.path.exists(path) == exists


# test 'make_directories' if the item is a file
@pytest.mark.parametrize(('subpath', 'reset', 'is_file', 'is_dir'), [
    ("test_1.file", False, True, False),
    ("test_1.file", True, True, False)
])
def test_make_directories_is_file(
        subpath, reset, is_file, is_dir,
        directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(str(directory), subpath)
    system_utils.make_directories(path, reset=reset)
    assert os.path.isfile(path) == is_file
    assert os.path.isdir(path) == is_dir


# test 'remove_file'
def test_remove_file(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_1.file")
    system_utils.remove_file(path)
    assert os.path.exists(path) == False


# test 'remove_directory' if the directory have some files
def test_remove_direcotry(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_havingsomefiles_d")
    system_utils.remove_directory(path)
    assert os.path.exists(path) == False


# test 'remove_directory' if the directory is empty
def test_remove_empty_dir(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_a_d")
    system_utils.remove_directory(path)
    assert os.path.exists(path) == False


# test 'reset_directory'
def test_reset_directory_is_done(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(str(directory), "test_havingsomefiles_d")
    system_utils.reset_directory(path)
    assert len(os.listdir(path)) == 0


# test 'reset_directory' if the item is not a directory
def test_reset_directory_not_dir(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(str(directory), "test_1.file")
    system_utils.reset_directory(path)
    assert os.path.isfile(path)


# test 'reset_directory' if the item does not exist
def test_reset_directory_not_exist(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(str(directory), "unknown_item")
    system_utils.reset_directory(path)
    assert not os.path.exists(path)


@pytest.fixture
def object_() -> Dict:
    return {f"value_{i}": i for i in range(9)}


# test 'object_to_pickle' and 'load_object_from_pickle'
def test_object_to_pickle_load_object_from_pickle(object_: Dict, tmpdir: Path):
    system_utils = SystemUtils()
    path = tmpdir / "sample.pickle"
    # create pickle file by 'object_to_pickle'
    system_utils.object_to_picle(path, object_)
    assert os.path.exists(path)
    assert os.path.isfile(path)
    # load object by 'load_object_from_pickle'
    res = system_utils.load_object_from_pickle(path)
    assert object_ == res


@pytest.fixture
def list2d() -> List[List[int]]:
    return [[i for i in range(9)] for _ in range(9)]


@pytest.mark.parametrize(('header'), [
    (None, ),
    ([f'col_{i}' for i in range(9)], )
])
# test 'list_to_csv' and 'load_list_from_csv'
def test_list_to_csv_load_list_from_csv(
        header, list2d: List[List[int]], tmpdir: Path):
    system_utils = SystemUtils()
    path = tmpdir / "sample.csv"
    # create csv file by 'list_to_csv'
    system_utils.list_to_csv(path, list2d, header)
    assert os.path.exists(path)
    assert os.path.isfile(path)
    # load list by 'load_list_from_csv'
    if header is None:
        skip_header = False
    else:
        skip_header = True
    res = system_utils.load_list_from_csv(path, skip_header)
    assert list2d == [[int(s) for s in slist] for slist in res]


@pytest.fixture
def dict_() -> Dict:
    return {f"value_{i}": i for i in range(9)}


# test 'dict_to_json' and 'load_dict_from_json'
def test_dict_from_json(dict_: Dict, tmpdir: Path):
    system_utils = SystemUtils()
    path = tmpdir / "sample.json"
    system_utils.dict_to_json(path, dict_)
    assert os.path.exists(path)
    assert os.path.isfile(path)
    res = system_utils.load_dict_from_json(path)
    assert res == dict_


# test 'zip_item' if the item is a directory
def test_zip_directory(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_havingsomefiles_d")
    system_utils.zip_item(str(path))
    zipfile_path = str(path) + ".zip"
    assert os.path.exists(zipfile_path)
    assert os.path.isfile(zipfile_path)


# test 'zip_item' if the item is a directory and naming the zip file
def test_zip_directory_named(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_havingsomefiles_d")
    zipfile_path = os.path.join(directory, "zipfile")
    system_utils.zip_item(path, zippath=str(zipfile_path))
    assert os.path.exists(str(zipfile_path) + '.zip')
    assert os.path.isfile(str(zipfile_path) + '.zip')


# test 'zip_item' if the item a file
def test_zip_file(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_1.file")
    zipfile_path = path
    system_utils.zip_item(str(path))
    assert os.path.exists(str(zipfile_path) + '.zip')
    assert os.path.isfile(str(zipfile_path) + '.zip')


# test 'zip_item' if the item a file and naming the zip file
def test_zip_file_named(directory: Path):
    system_utils = SystemUtils()
    path = os.path.join(directory, "test_1.file")
    zipfile_path = os.path.join(directory, "zipfile")
    system_utils.zip_item(str(path), zippath=str(zipfile_path))
    assert os.path.exists(str(zipfile_path) + '.zip')
    assert os.path.isfile(str(zipfile_path) + '.zip')


@pytest.fixture
def make_zip_file(directory: Path) -> str:
    path = os.path.join(directory, "test_havingsomefiles_d")
    system_utils = SystemUtils()
    system_utils.zip_item(str(path))
    yield directory


# test 'zip_item' if the item a file
def test_zip_file_added(make_zip_file: str):
    system_utils = SystemUtils()
    path = os.path.join(make_zip_file, "test_1.file")
    zipfile_path = os.path.join(make_zip_file, "test_havingsomefiles_d")
    system_utils.zip_item(str(path), zippath=str(zipfile_path), add=True)
    assert os.path.exists(str(zipfile_path) + '.zip')
    assert os.path.isfile(str(zipfile_path) + '.zip')
