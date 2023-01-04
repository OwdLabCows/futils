import glob
import shutil
import os
import pickle
import csv
import json
import pandas as pd

from typing import Any, List, Union


def remove_glob(path: str, recursive: bool = True):
    for p in glob.glob(path, recursive=recursive):
        if os.path.isfile(p):
            os.remove(p)
        elif os.path.isdir(p):
            shutil.rmtree(p)


def obj_to_picle(path: str, obj: Any) -> str:
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
    return path


def load_obj_from_pickle(path: str) -> Any:
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj


def list_to_csv(
        path: str, list_obj: List[Any],
        header: Union[List[str], None] = None
        ):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerow(list_obj)


def load_list_from_csv(path: str, skip_header: bool = False) -> List[Any]:
    with open(path, 'r') as f:
        reader = csv.reader(f)
        return [row for row in reader]


def load_dict_from_json(path: str):
    with open(path, 'r') as f:
        return json.load(f)


def zip_directory(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Could not find {path}")
    if not os.path.isdir(path):
        raise FileNotFoundError(f"{path} must be a directory")
    os.system(f'zip -r "{os.path.dirname(path)}.zip" "{path}"')


def meta_exel_to_df(
        path: str, skiprows: Union(None, int) = 1,
        index_col: Union(None, List[Any]) = None
        ) -> pd.DataFrame:
    df = pd.read_excel(path, skiprows=skiprows, index_col=index_col)
    return df
