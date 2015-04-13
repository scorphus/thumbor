from thumbor.integration_tests import EngineTestCase


class PILTest(EngineTestCase):
    engine = 'thumbor.engines.pil'

    def test_single_params(self):
        self.exec_single_params()
