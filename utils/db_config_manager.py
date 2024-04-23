import os
import configparser

from os import path

from utils.constants import ROOT_PATH

_config_path = path.join(ROOT_PATH, 'config.ini')

_config = configparser.RawConfigParser()
_config.read(_config_path)


class DBConfigManager:


    sqlite_db_path = path.join(ROOT_PATH, _config.get('db_data', 'sqlite_db_path'))


