from robot.api import logger
from robot.libraries.BuiltIn import  BuiltIn,RobotNotRunningError
import logging
from core.dirtylog.singleton import Singleton
import argparse
from unittest.mock import Mock
from pathlib import Path


class DirtyLogger(Singleton):
    FILEPATH ="logs"
    FILENAME ="robot.log"
    def __init__(self):
        try:
            self.logger = logging.getLogger("DirtyLogger")
            self.robot_logger = logger
            self.builtin = BuiltIn()

            execpath = self.builtin.get_variable_value("${EXECDIR}")
            self.path = self.create_path_if_not_exist(Path(execpath,self.FILEPATH))
            self.handler = logging.FileHandler(Path(self.path,self.FILENAME))

            formatter = self.get_currentframe()
            self.handler.setLevel("DEBUG")
            self.handler.setFormatter(formatter)
            self.logger.addHandler(self.handler)
            self.logger.info("testing")
            self.level = self.get_log_level()
            self.builtin.set_log_level("TRACE")
        except RobotNotRunningError:
            self.level="TRACE"
            self.builtin= Mock()
    def get_log_level(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-L","--Loglevel",type=str, default="TRACE")
        known_args,_= parser.parse_known_args()
        self.level = vars(known_args)["Loglevel"]
        return self.level

    def create_path_if_not_exist(self,path):
        if not path.exists():
            Path.mkdir(path,parents=True,exist_ok=True)
        return path

    def get_currentframe(self):
        frame = logging.currentframe()
        filepath =Path(frame.f_code.co_filename)
        if filepath.is_relative_to(Path.cwd()):
            filepath= filepath.relative_to(Path.cwd())
        line = frame.f_lineno

        return logging.Formatter(f"%(asctime)s- {filepath},line:{line}-%(levelname)s-%(message)s")

if __name__=="__main__":
    class Frame:
        def __init__(self):
            self.get_frame()
        def get_frame(self):
            frame = logging.currentframe()
            filepath =Path(frame.f_code.co_filename)
            file_path=filepath.relative_to(Path.cwd())
            print(filepath,Path.cwd())
    # DirtyLogger()
    # print(dir())#获取当前文件的属性
    ab= "d"
    Frame()
    # print(vars(ab))