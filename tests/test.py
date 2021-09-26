import unittest
from colorant import Colorant


TEST_TOKEN = 'test'


class TestColorant(unittest.TestCase):

    def test_flush(self):
        cr = Colorant().lt_green()
        self.assertEqual(['\u001b[0m', '\u001b[92m'], cr._buf)

        cr = cr.flush('')
        self.assertEqual(['\u001b[0m'], cr._buf)

    def test_err(self):
        container = str(Colorant().err(TEST_TOKEN))
        self.assertIn('\u001b[101m', container)
        self.assertIn('\u001b[97m', container)
        self.assertTrue(container.startswith('\u001b[0m'))
        self.assertTrue(container.endswith('test\u001b[0m'))

    def test_ok(self):
        container = str(Colorant().ok(TEST_TOKEN))
        self.assertIn('\u001b[102m', container)
        self.assertIn('\u001b[30m', container)
        self.assertTrue(container.startswith('\u001b[0m'))
        self.assertTrue(container.endswith('test\u001b[0m'))

    def test_warn(self):
        container = str(Colorant().warn(TEST_TOKEN))
        self.assertIn('\u001b[103m', container)
        self.assertIn('\u001b[30m', container)
        self.assertTrue(container.startswith('\u001b[0m'))
        self.assertTrue(container.endswith('test\u001b[0m'))

    def test_info(self):
        container = str(Colorant().info(TEST_TOKEN))
        self.assertIn('\u001b[104m', container)
        self.assertIn('\u001b[97m', container)
        self.assertTrue(container.startswith('\u001b[0m'))
        self.assertTrue(container.endswith('test\u001b[0m'))

    def test_text(self):
        self.assertEqual(
            '\u001b[0mtest\u001b[0m', str(Colorant().text(TEST_TOKEN)))

    def test_reset(self):
        self.assertEqual(
            '\u001b[0m\u001b[0m\u001b[0m', str(Colorant().reset()))

    def test_default(self):
        self.assertEqual(
            '\u001b[0m\u001b[39mtest\u001b[0m',
            str(Colorant().default(TEST_TOKEN)))

    def test_black(self):
        self.assertEqual(
            '\u001b[0m\u001b[30mtest\u001b[0m',
            str(Colorant().black(TEST_TOKEN)))

    def test_red(self):
        self.assertEqual(
            '\u001b[0m\u001b[31mtest\u001b[0m',
            str(Colorant().red(TEST_TOKEN)))

    def test_green(self):
        self.assertEqual(
            '\u001b[0m\u001b[32mtest\u001b[0m',
            str(Colorant().green(TEST_TOKEN)))

    def test_yellow(self):
        self.assertEqual(
            '\u001b[0m\u001b[33mtest\u001b[0m',
            str(Colorant().yellow(TEST_TOKEN)))

    def test_blue(self):
        self.assertEqual(
            '\u001b[0m\u001b[34mtest\u001b[0m',
            str(Colorant().blue(TEST_TOKEN)))

    def test_magenta(self):
        self.assertEqual(
            '\u001b[0m\u001b[35mtest\u001b[0m',
            str(Colorant().magenta(TEST_TOKEN)))

    def test_cyan(self):
        self.assertEqual(
            '\u001b[0m\u001b[36mtest\u001b[0m',
            str(Colorant().cyan(TEST_TOKEN)))

    def test_white(self):
        self.assertEqual(
            '\u001b[0m\u001b[37mtest\u001b[0m',
            str(Colorant().white(TEST_TOKEN)))

    def test_lt_black(self):
        self.assertEqual(
            '\u001b[0m\u001b[90mtest\u001b[0m',
            str(Colorant().lt_black(TEST_TOKEN)))

    def test_lt_red(self):
        self.assertEqual(
            '\u001b[0m\u001b[91mtest\u001b[0m',
            str(Colorant().lt_red(TEST_TOKEN)))

    def test_lt_green(self):
        self.assertEqual(
            '\u001b[0m\u001b[92mtest\u001b[0m',
            str(Colorant().lt_green(TEST_TOKEN)))

    def test_lt_yellow(self):
        self.assertEqual(
            '\u001b[0m\u001b[93mtest\u001b[0m',
            str(Colorant().lt_yellow(TEST_TOKEN)))

    def test_lt_blue(self):
        self.assertEqual(
            '\u001b[0m\u001b[94mtest\u001b[0m',
            str(Colorant().lt_blue(TEST_TOKEN)))

    def test_lt_magenta(self):
        self.assertEqual(
            '\u001b[0m\u001b[95mtest\u001b[0m',
            str(Colorant().lt_magenta(TEST_TOKEN)))

    def test_lt_cyan(self):
        self.assertEqual(
            '\u001b[0m\u001b[96mtest\u001b[0m',
            str(Colorant().lt_cyan(TEST_TOKEN)))

    def test_lt_white(self):
        self.assertEqual(
            '\u001b[0m\u001b[97mtest\u001b[0m',
            str(Colorant().lt_white(TEST_TOKEN)))

    def test_bg_default(self):
        self.assertEqual(
            '\u001b[0m\u001b[49mtest\u001b[0m',
            str(Colorant().bg_default(TEST_TOKEN)))

    def test_bg_black(self):
        self.assertEqual(
            '\u001b[0m\u001b[40mtest\u001b[0m',
            str(Colorant().bg_black(TEST_TOKEN)))

    def test_bg_red(self):
        self.assertEqual(
            '\u001b[0m\u001b[41mtest\u001b[0m',
            str(Colorant().bg_red(TEST_TOKEN)))

    def test_bg_green(self):
        self.assertEqual(
            '\u001b[0m\u001b[42mtest\u001b[0m',
            str(Colorant().bg_green(TEST_TOKEN)))

    def test_bg_yellow(self):
        self.assertEqual(
            '\u001b[0m\u001b[43mtest\u001b[0m',
            str(Colorant().bg_yellow(TEST_TOKEN)))

    def test_bg_blue(self):
        self.assertEqual(
            '\u001b[0m\u001b[44mtest\u001b[0m',
            str(Colorant().bg_blue(TEST_TOKEN)))

    def test_bg_magenta(self):
        self.assertEqual(
            '\u001b[0m\u001b[45mtest\u001b[0m',
            str(Colorant().bg_magenta(TEST_TOKEN)))

    def test_bg_cyan(self):
        self.assertEqual(
            '\u001b[0m\u001b[46mtest\u001b[0m',
            str(Colorant().bg_cyan(TEST_TOKEN)))

    def test_bg_white(self):
        self.assertEqual(
            '\u001b[0m\u001b[47mtest\u001b[0m',
            str(Colorant().bg_white(TEST_TOKEN)))

    def test_bg_lt_black(self):
        self.assertEqual(
            '\u001b[0m\u001b[100mtest\u001b[0m',
            str(Colorant().bg_lt_black(TEST_TOKEN)))

    def test_bg_lt_red(self):
        self.assertEqual(
            '\u001b[0m\u001b[101mtest\u001b[0m',
            str(Colorant().bg_lt_red(TEST_TOKEN)))

    def test_bg_lt_green(self):
        self.assertEqual(
            '\u001b[0m\u001b[102mtest\u001b[0m',
            str(Colorant().bg_lt_green(TEST_TOKEN)))

    def test_bg_lt_yellow(self):
        self.assertEqual(
            '\u001b[0m\u001b[103mtest\u001b[0m',
            str(Colorant().bg_lt_yellow(TEST_TOKEN)))

    def test_bg_lt_blue(self):
        self.assertEqual(
            '\u001b[0m\u001b[104mtest\u001b[0m',
            str(Colorant().bg_lt_blue(TEST_TOKEN)))

    def test_bg_lt_magenta(self):
        self.assertEqual(
            '\u001b[0m\u001b[105mtest\u001b[0m',
            str(Colorant().bg_lt_magenta(TEST_TOKEN)))

    def test_bg_lt_cyan(self):
        self.assertEqual(
            '\u001b[0m\u001b[106mtest\u001b[0m',
            str(Colorant().bg_lt_cyan(TEST_TOKEN)))

    def test_bg_lt_white(self):
        self.assertEqual(
            '\u001b[0m\u001b[107mtest\u001b[0m',
            str(Colorant().bg_lt_white(TEST_TOKEN)))

    def test_bold(self):
        self.assertEqual(
            '\u001b[0m\u001b[1mtest\u001b[0m',
            str(Colorant().bold(TEST_TOKEN)))

    def test_underline(self):
        self.assertEqual(
            '\u001b[0m\u001b[4mtest\u001b[0m',
            str(Colorant().underline(TEST_TOKEN)))

    def test_reversed(self):
        self.assertEqual(
            '\u001b[0m\u001b[7mtest\u001b[0m',
            str(Colorant().reversed(TEST_TOKEN)))


if __name__ == '__main__':
    unittest.main()
