import unittest
import os
from log_event import log_event, LOG_PATH

class TestLogEvent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(LOG_PATH):
            os.remove(LOG_PATH)

    def setUp(self):
        pass

    def read_log(self):
        if not os.path.exists(LOG_PATH):
            return ""
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            return f.read()

    def test_success_logging(self):
        log_event("Maxim", "success")
        content = self.read_log()
        self.assertIn("Maxim", content)

    def test_expired_logging(self):
        log_event("Artem", "expired")
        content = self.read_log()
        self.assertIn("Artem", content)

    def test_failed_logging(self):
        log_event("project", "failed")
        content = self.read_log()
        self.assertIn("project", content)

if __name__ == "__main__":
    unittest.main()