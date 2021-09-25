from hue import Hue


COLOR_BANNER_LEN = 6
EFFECT_BANNER_LEN = 12


if __name__ == '__main__':
    (Hue().black(' 0'.center(COLOR_BANNER_LEN))
          .red(' 1'.center(COLOR_BANNER_LEN))
          .green(' 2'.center(COLOR_BANNER_LEN))
          .yellow(' 3'.center(COLOR_BANNER_LEN))
          .blue(' 4'.center(COLOR_BANNER_LEN))
          .magenta(' 5'.center(COLOR_BANNER_LEN))
          .cyan(' 6'.center(COLOR_BANNER_LEN))
          .white(' 7'.center(COLOR_BANNER_LEN))
          .flush())

    (Hue().lt_black(' 8'.center(COLOR_BANNER_LEN))
          .lt_red(' 9'.center(COLOR_BANNER_LEN))
          .lt_green('10'.center(COLOR_BANNER_LEN))
          .lt_yellow('11'.center(COLOR_BANNER_LEN))
          .lt_blue('12'.center(COLOR_BANNER_LEN))
          .lt_magenta('13'.center(COLOR_BANNER_LEN))
          .lt_cyan('14'.center(COLOR_BANNER_LEN))
          .lt_white('15'.center(COLOR_BANNER_LEN))
          .flush())

    (Hue().bg_black('16'.center(COLOR_BANNER_LEN))
          .bg_red('17'.center(COLOR_BANNER_LEN))
          .bg_green('18'.center(COLOR_BANNER_LEN))
          .bg_yellow('19'.center(COLOR_BANNER_LEN))
          .bg_blue('20'.center(COLOR_BANNER_LEN))
          .bg_magenta('21'.center(COLOR_BANNER_LEN))
          .bg_cyan('22'.center(COLOR_BANNER_LEN))
          .bg_white('23'.center(COLOR_BANNER_LEN))
          .flush())

    (Hue().bg_lt_black('24'.center(COLOR_BANNER_LEN))
          .bg_lt_red('25'.center(COLOR_BANNER_LEN))
          .bg_lt_green('26'.center(COLOR_BANNER_LEN))
          .bg_lt_yellow('27'.center(COLOR_BANNER_LEN))
          .bg_lt_blue('28'.center(COLOR_BANNER_LEN))
          .bg_lt_magenta('29'.center(COLOR_BANNER_LEN))
          .bg_lt_cyan('30'.center(COLOR_BANNER_LEN))
          .bg_lt_white('31'.center(COLOR_BANNER_LEN))
          .flush())

    (Hue().text('normal'.center(EFFECT_BANNER_LEN))
          .bold('bold'.center(EFFECT_BANNER_LEN)).reset()
          .underline('underline'.center(EFFECT_BANNER_LEN)).reset()
          .reversed('reversed'.center(EFFECT_BANNER_LEN))
          .flush())

    (Hue().err('FAIL'.center(EFFECT_BANNER_LEN))
          .ok('OK'.center(EFFECT_BANNER_LEN))
          .warn('WARN'.center(EFFECT_BANNER_LEN))
          .info('INFO'.center(EFFECT_BANNER_LEN))
          .flush())
