from pprint import pprint
from unittest import TestCase
import gazu
from hook.python.pepper_doc_psw import Houpub
from hook.python.tests import logging_test_sw


class test_Houpub(TestCase):

    def setUp(self):
        # _identification = None

        self.a = Houpub()
        self.a.login("http://192.168.3.116/api", "pipeline@rapa.org", "netflixacademy")

    # @property
    # def identification(self):
    #     return self._identification
    # @identification.setter
    # def identification(self, value):
    #     self._identification = value
    #
    # print(identification)
    # def test_publish_working_file(self):
    #     self.a.project = 'pepper'
    #     self.a.asset = 'temp_fire'
    #     self.a.entity = 'asset'
    #     self.a.publish_working_file("simulation", "hou")

    # def test_working_file_path(self):
    #     self.a.project = 'pepper'
    #     self.a.asset = 'temp_fire'
    #     self.a.entity = 'asset'
    #     path = self.a.working_file_path("simulation", "hou", 10)
    #     print(path)

    # def test_make_next_working_path(self):
    #     self.a.project = 'pepper'
    #     self.a.asset = 'temp_fire'
    #     self.a.entity = 'asset'
    #
    #     path = self.a.make_next_working_path("simulation")
    #     print(path)

    # def test_publish_output_file(self):
    #     self.a.project = 'pepper'
    #     # self.a.asset = 'temp_fire'
    #     # self.a.entity = 'asset'
    #     self.a.sequence = 'sq01'
    #     self.a.shot = '0010'
    #     self.a.entity = 'shot'
    #     self.a.publish_output_file('FX', 'Movie_file', "test")
    # #
    def test_output_file_path(self):
        self.a.project = 'pepper'
        # self.a.asset = 'temp_fire'
        # self.a.entity = 'asset'
        self.a.sequence = 'sq01'
        self.a.shot = '0010'
        self.a.entity = 'shot'
        path = self.a.output_file_path('Movie_file', 'FX', 100)
        print(path)
        print(self.a.identification)
        # print(self.a.login())
        logger = logging_test_sw.make_logger()
        logger.debug("test")

    # def test_make_next_output_path(self):
    #     self.a.project = 'pepper'
    #     # self.a.asset = 'temp_fire'
    #     # self.a.entity = 'asset'
    #     self.a.sequence = 'sq01'
    #     self.a.shot = '0010'
    #     self.a.entity = 'shot'
    #     output_type_name = 'Movie_file'
    #     task_type_name = 'FX'
    #     path = self.a.make_next_output_path('Movie_file', 'FX')
    #     print(path)

    # def test_get_task(self):
    #     self.a.project = 'pepper'
    #     # self.a.asset = 'temp_fire'
    #     # self.a.entity = 'asset'
    #     self.a.sequence = 'sq01'
    #     self.a.shot = '0010'
    #     self.a.entity = 'shot'
    #     task = self.a.get_task("FX")
    #     print(task)

    # ------------------------------------------------------------------------------------ok

    # def test_casting_multiple_assets(self):
    #     pass

    # def test_casting_create(self):
    #     self.a.project = 'pepper'
    #     self.a.asset = 'temp_fire'
    #     self.a.entity = 'asset'
        # self.a.sequence = 'sq01'
        # self.a.shot = '0010'
        # self.a.entity = 'shot'
    #
    #     self.a.casting_create(nb)
    #     a = gazu.task.all_tasks_for_asset(self.a.asset)
    #     pprint(a)
        # gazu.task.get_task_by


        # gazu.task.new_task()
        # gazu.task.new_task_type()
        # a = gazu.task.all_tasks_for_shot
        # print(a)
