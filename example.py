from baseutils import BaseUtils
import logging
# import sys # comment in if set logger to BaseUtils


# logging setting (if you want to see log)
logging.basicConfig(
    level=logging.DEBUG
)

# create instance
base_utils = BaseUtils()
# set logger optionally as follows
# logger = logging.getLogger(__name__)
# terminal = logging.StreamHandler(sys.stdout)
# terminal.setLevel(logging.DEBUG)
# logger.addHandler(terminal)
# base_utils = BaseUtils(logger)

# convert dict to pickle file
dict_ = {
    "name": "David",
    "value": 12,
}
base_utils.obj_to_picle("/path/to/dict.pickle", dict_)

# load pickle file and generete a dict object
res = base_utils.load_obj_from_pickle(
    "/path/to/dict.pickle")
print(res)

# convert list to csv file
list_ = [
    [j for i in range(5)]
    for j in range(9)]
base_utils.list_to_csv("/path/to/csvfile.csv", list_)

# load csv file and generate a list object
res = base_utils.load_list_from_csv("/path/to/csvfile.csv")
print(res)

# load json file and generate a dict object
res = base_utils.load_dict_from_json("/path/to/jsonfile.json")
print(res)

# reset a directory
base_utils.reset_directory(
    "/path/to/directory")

# zip a directory
base_utils.zip_directory(
    "/path/to/directory_for_zip")

# load meta excel file
res = base_utils.meta_exel_to_df(
    "/path/to/meta_excelfile.xlsx")
print(res)
