import glob
import shutil
import os
import pickle
import csv
import json
import sys
# typing
from typing import Any, List, Union, Dict
# logging
import logging


class BaseUtils():

    def __init__(self, logger: Union[logging.Logger, None] = None):
        self.logger = logger
        if self.logger is None:
            self.logger = logging.getLogger(__name__)
            terminal = logging.StreamHandler(sys.stdout)
            terminal.setLevel(logging.INFO)
            msgfmt = "%(asctime)s in %(funcName)s(%(filename)s)"
            dtfmt = "%Y-%m-%d %I:%M:%S %p"
            fmt = logging.Formatter(msgfmt, dtfmt)
            terminal.setFormatter(fmt)
            self.logger.addHandler(terminal)

    def make_directories(self, path: str, reset: bool = False):
        self.logger.info("start util process to make directories.")
        if os.path.exists(path):
            self.logger.warning(f"'{path}' exists.")
            if reset:
                self.logger.warning(f"reset '{path}'.")
                self.reset_directory(path)
            else:
                self.logger.debug("do nothing.")
            self.logger.info("completed.")
            return
        self.logger.debug(f"make directories '{path}'.")
        os.makedirs(path)
        self.logger.info("completed.")

    def reset_directory(self, path: str):
        self.logger.info("start util process to reset a directory.")
        if not os.path.isdir(path):
            self.logger.warning(f"'{path}' is not a directory.")
            self.logger.info("completed.")
            return
        if not os.path.exists(path):
            self.logger.warning(f"'{path}' does not exist.")
            self.logger.info("completed.")
            return
        for p in glob.glob(os.path.join(path, "*")):
            if p == path:
                continue
            if os.path.isfile(p):
                self.logger.warning(f"remove a file '{p}' in '{path}'.")
                os.remove(p)
            elif os.path.isdir(p):
                self.logger.warning(f"remove a directory '{p}' in '{path}'")
                shutil.rmtree(p)
        self.logger.info("completed.")

    def obj_to_picle(self, path: str, obj: Any) -> str:
        self.logger.info(
            "start util process to convert object to pickle file.")
        self.logger.debug(f"convert {type(obj)} to '{path}'")
        with open(path, 'wb') as f:
            self.logger.debug(f"'{path}' is created.")
            pickle.dump(obj, f)
        self.logger.info("completed.")
        return path

    def load_obj_from_pickle(self, path: str) -> Any:
        self.logger.info(
            "start util process to load pickle file and generate object.")
        self.logger.info(f"load '{path}' and generate object.")
        with open(path, 'rb') as f:
            self.logger.debug(f"'{path}' is loaded.")
            obj = pickle.load(f)
        self.logger.info("completed.")
        return obj

    def list_to_csv(
            self,
            path: str, list_obj: List[List[Any]],
            header: Union[List[str], None] = None
            ):
        self.logger.info("start util process to convert list to csv file.")
        with open(path, 'w') as f:
            self.logger.debug(f"'{path}' is genereted.")
            writer = csv.writer(f)
            if header is not None:
                writer.writerow(header)
                self.logger.debug(f"header '{header}' is set.")
            writer.writerows(list_obj)
        self.logger.info("completed.")

    def load_list_from_csv(
            self, path: str, skip_header: bool = False) -> List[List[str]]:
        self.logger.info(
            "start util process to load csv file and generate list.")
        with open(path, 'r') as f:
            self.logger.debug(f"'{path}' is loaded.'")
            reader = csv.reader(f)
            self.logger.info("completed.")
            list_ = [row for row in reader]
            if skip_header:
                list_ = list_[1:]
            return list_

    def dict_to_json(self, path: str, dict_obj: Dict):
        self.logger.info(
            "start util process to convert dict to json file.")
        with open(path, 'w') as f:
            self.logger.debug(f"'{path}' is generated.")
            json.dump(dict_obj, f)
            self.logger.info("completed.")

    def load_dict_from_json(self, path: str):
        self.logger.info(
            "start util process to load json file and generate dict.")
        with open(path, 'r') as f:
            self.logger.debug(f"''{path}' is loaded.")
            self.logger.info("completed.")
            return json.load(f)

    def zip_directory(self, path: str):
        self.logger.info("start util process to zip a directory.")
        if not os.path.exists(path):
            self.logger.error("the directory cloud not be found.")
            raise FileNotFoundError(f"Could not find {path}")
        if not os.path.isdir(path):
            self.logger.error("the type is not diretory.")
            raise FileNotFoundError(f"{path} must be 第1話a directory")
        os.system(f'zip -r "{path}.zip" "{path}"')
        self.logger.debug(
            f"'zip -r \"{path}.zip\" \"{path}\"' is done.")
        self.logger.info("completed.")
