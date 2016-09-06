from unittest import TestCase
from isatools import isajson, sra
from lxml import etree
import os
import shutil
from tests import utils
import tempfile


class TestNewSraExport(TestCase):

    # TODO: Isolate testing SRA writer (don't rely on ISA JSON loader)

    def setUp(self):

        self._json_data_dir = utils.JSON_DATA_DIR
        self._sra_data_dir = utils.SRA_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

        study_id = 'BII-S-7'
        self._inv_obj = isajson.load(open(os.path.join(self._json_data_dir, study_id, study_id + '.json')))
        self._study_sra_data_dir = os.path.join(self._sra_data_dir, study_id)
        self._expected_submission_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'submission.xml'), 'rb').read())
        self._expected_project_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'project_set.xml'),
                                                                 'rb').read())
        self._expected_sample_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'sample_set.xml'),
                                                                 'rb').read())
        self._expected_exp_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'experiment_set.xml'),
                                                                  'rb').read())
        self._expected_run_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'run_set.xml'),
                                                               'rb').read())

        self._sra_default_config = {
            "sra_broker": "",
            "sra_center": "OXFORD",
            "sra_project": "OXFORD",
            "sra_lab": "Oxford e-Research Centre",
            "inform_on_status_email": "proccaserra@gmail.com",
            "inform_on_error_email": "proccaserra@gmail.com"
        }

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_sra_export_submission_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_submission_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'submission.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_submission_xml_obj, actual_submission_xml_obj))

    def test_sra_export_sample_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_sample_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'sample_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_sample_set_xml_obj, actual_sample_set_xml_obj))

    def test_sra_export_experiment_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_exp_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'experiment_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_exp_set_xml_obj, actual_exp_set_xml_obj))

    def test_sra_export_run_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_run_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'run_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_run_set_xml_obj, actual_run_set_xml_obj))

    def test_sra_export_project_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_project_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'project_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_project_set_xml_obj, actual_project_set_xml_obj))
