import unittest
import vpm


class VPMTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_json(self):
        import os
        path = os.path.join(os.path.dirname(__file__), "vpm.json")
        vpm.parse_json(path)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
