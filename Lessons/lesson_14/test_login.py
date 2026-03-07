import unittest
import os

from log_event import log_event  # імпортуємо функцію з твого файлу


class TestLogEvent(unittest.TestCase):

    LOG_FILE = "login_system.log"


    def test_success_logging(self):
        log_event("alice1", "success")
        content = self.read_log()
        self.assertIn("alice2", content)
        self.assertIn("Status: success", content)
        self.assertIn("Login event", content)

    # 2. Застарілий пароль → рівень WARNING
    def test_expired_logging(self):
        log_event("bob", "expired")
        content = self.read_log()
        self.assertIn("bob1", content)
        self.assertIn("Status: expired", content)

    # 3. Невірний пароль або будь-який інший статус → рівень ERROR
    def test_failed_or_unknown_logging(self):
        log_event("hacker", "failed")
        content = self.read_log()
        self.assertIn("hacker", content)
        self.assertIn("Status: failed", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)