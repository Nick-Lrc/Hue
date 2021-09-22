from __future__ import annotations


# Control Sequence Introducer
CSI = '\u001b['
FIN = 'm'


def csi_seq(sgr):
    """Returns a CSI sequence.

    Parameters
    ----------
    sgr: str
        Select Graphic Rendition parameters
    
    Returns
    -------
    str
        Resulting CSI sequence.
    """
    return f'{CSI}{sgr}{FIN}'


class Hue:
    RESET = csi_seq(0)
    BANNER_LEN = 6

    def __init__(self):
        self._buf = []
        self.reset()

    def info(self, text=None):
        return self.lt_white().lt_blue_bg()._add_banner('INFO', text)

    def fail(self, text=None):
        return self.lt_white().lt_red_bg()._add_banner('FAIL', text)

    def warn(self, text=None):
        return self.black().lt_yellow_bg()._add_banner('WARN', text)

    def ok(self, text=None):
        return self.black().lt_green_bg()._add_banner('OK', text)

    def black(self, text=None):
        return self._add(Foreground.BLACK, text)

    def red(self, text=None):
        return self._add(Foreground.RED, text)

    def green(self, text=None):
        return self._add(Foreground.GREEN, text)

    def yellow(self, text=None):
        return self._add(Foreground.YELLOW, text)

    def blue(self, text=None):
        return self._add(Foreground.BLUE, text)

    def magenta(self, text=None):
        return self._add(Foreground.MAGENTA, text)

    def cyan(self, text=None):
        return self._add(Foreground.CYAN, text)

    def white(self, text=None):
        return self._add(Foreground.WHITE, text)

    def lt_black(self, text=None):
        return self._add(Foreground.LT_BLACK, text)

    def lt_red(self, text=None):
        return self._add(Foreground.LT_RED, text)

    def lt_green(self, text=None):
        return self._add(Foreground.LT_GREEN, text)

    def lt_yellow(self, text=None):
        return self._add(Foreground.LT_YELLOW, text)

    def lt_blue(self, text=None):
        return self._add(Foreground.LT_BLUE, text)

    def lt_magenta(self, text=None):
        return self._add(Foreground.LT_MAGENTA, text)

    def lt_cyan(self, text=None):
        return self._add(Foreground.LT_CYAN, text)

    def lt_white(self, text=None):
        return self._add(Foreground.LT_WHITE, text)

    def black_bg(self, text=None):
        return self._add(Background.BLACK, text)

    def red_bg(self, text=None):
        return self._add(Background.RED, text)

    def green_bg(self, text=None):
        return self._add(Background.GREEN, text)

    def yellow_bg(self, text=None):
        return self._add(Background.YELLOW, text)

    def blue_bg(self, text=None):
        return self._add(Background.BLUE, text)

    def magenta_bg(self, text=None):
        return self._add(Background.MAGENTA, text)

    def cyan_bg(self, text=None):
        return self._add(Background.CYAN, text)

    def white_bg(self, text=None):
        return self._add(Background.WHITE, text)

    def lt_black_bg(self, text=None):
        return self._add(Background.LT_BLACK, text)

    def lt_red_bg(self, text=None):
        return self._add(Background.LT_RED, text)

    def lt_green_bg(self, text=None):
        return self._add(Background.LT_GREEN, text)

    def lt_yellow_bg(self, text=None):
        return self._add(Background.LT_YELLOW, text)

    def lt_blue_bg(self, text=None):
        return self._add(Background.LT_BLUE, text)

    def lt_magenta_bg(self, text=None):
        return self._add(Background.LT_MAGENTA, text)

    def lt_cyan_bg(self, text=None):
        return self._add(Background.LT_CYAN, text)

    def lt_white_bg(self, text=None):
        return self._add(Background.LT_WHITE, text)

    def bold(self, text=None):
        return self._add(Decoration.BOLD, text)

    def underline(self, text=None):
        return self._add(Decoration.UNDERLINE, text)

    def reversed(self, text=None):
        return self._add(Decoration.REVERSED, text)

    def reset(self):
        return self._add(Hue.RESET)

    def reset_fg(self):
        return self._add(Foreground.RESET)

    def reset_bg(self):
        return self._add(Background.RESET)

    def text(self, text=None):
        return self._add(text=text)

    def _add(self, csi_seq=None, text=None):
        if csi_seq:
            self._buf.append(csi_seq)
        if text:
            self._buf.append(text)
        return self

    def _add_banner(self, banner, text=None):
        self.text(banner.center(Hue.BANNER_LEN)).reset()
        if text:
            return self._add(' ', text)
        return self

    def __str__(self):
        self.reset()
        return ''.join(self._buf)


class Foreground:
    BLACK = csi_seq(30)
    RED = csi_seq(31)
    GREEN = csi_seq(32)
    YELLOW = csi_seq(33)
    BLUE = csi_seq(34)
    MAGENTA = csi_seq(35)
    CYAN = csi_seq(36)
    WHITE = csi_seq(37)
    LT_BLACK = csi_seq(90)
    LT_RED = csi_seq(91)
    LT_GREEN = csi_seq(92)
    LT_YELLOW = csi_seq(93)
    LT_BLUE = csi_seq(94)
    LT_MAGENTA = csi_seq(95)
    LT_CYAN = csi_seq(96)
    LT_WHITE = csi_seq(97)
    RESET = csi_seq(39)


class Background:
    BLACK = csi_seq(40)
    RED = csi_seq(41)
    GREEN = csi_seq(42)
    YELLOW = csi_seq(43)
    BLUE = csi_seq(44)
    MAGENTA = csi_seq(45)
    CYAN = csi_seq(46)
    WHITE = csi_seq(47)
    LT_BLACK = csi_seq(100)
    LT_RED = csi_seq(101)
    LT_GREEN = csi_seq(102)
    LT_YELLOW = csi_seq(103)
    LT_BLUE = csi_seq(104)
    LT_MAGENTA = csi_seq(105)
    LT_CYAN = csi_seq(106)
    LT_WHITE = csi_seq(107)
    RESET = csi_seq(49)


class Decoration:
    BOLD = csi_seq(1)
    UNDERLINE = csi_seq(4)
    REVERSED = csi_seq(7)
