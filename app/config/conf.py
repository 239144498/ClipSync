# -*- coding: utf-8 -*-
# @Time    : 2023/5/28
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : config.py
# @Software: PyCharm
import logging
import configparser

from typing import Optional
from app.config.setupsetting import ROOT_DIR, CONFIG


class Config:
    _instance = None

    @staticmethod
    def get_config() -> 'Config':
        """
        Get the config (singleton)
        The config is loaded from file.
        If the file does not exist, default values will be set.

        :return:
        """

        if Config._instance is None:
            Config()
        return Config._instance

    def __init__(self):
        """
        Creates a new Config instance.
        Should not be called.
        Instead use get_config.
        """

        if Config._instance is not None:
            raise Exception("Config is a singleton")
        else:
            Config._instance = self

        self.directory = ROOT_DIR
        self.file = CONFIG / "config.ini"
        self._new_config = not self.file.is_file()
        self.config = configparser.ConfigParser()

        self._read()

        # will be set from main
        self.api_port: Optional[int] = None
        self.ui_port: Optional[int] = None

    def _read(self):
        """
        Loads the config from file.
        If the file does not exist, default values will be set.
        """

        logging.info("reading config file: {}".format(self.file))

        # get default values
        self.config.read(CONFIG / "default.ini")

        # get the actual values
        self.config.read(self.file)

        # save the config just in case new values were added
        self.save()

    def save(self):
        """
        Saves the config to.
        """

        self.directory.mkdir(parents=True, exist_ok=True)

        with open(self.file, 'w', encoding="utf-8") as configfile:
            self.config.write(configfile)

    @property
    def new_config(self) -> bool:
        """
        True if the config was newly created.
        This is the case when the application was run the first time.
        """

        return self._new_config


conf = Config()

