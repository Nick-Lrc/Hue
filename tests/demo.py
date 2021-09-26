from colorant import Colorant


SMALL_BLOCK_LEN = 6
LARGE_BLOCK_LEN = 12


def small_block(text):
    return text.center(SMALL_BLOCK_LEN)


def large_block(text):
    return text.center(LARGE_BLOCK_LEN)


if __name__ == '__main__':
    (
        Colorant().black(small_block(' 0'))
                  .red(small_block(' 1'))
                  .green(small_block(' 2'))
                  .yellow(small_block(' 3'))
                  .blue(small_block(' 4'))
                  .magenta(small_block(' 5'))
                  .cyan(small_block(' 6'))
                  .white(small_block(' 7'))
                  .flush()
                  .lt_black(small_block(' 8'))
                  .lt_red(small_block(' 9'))
                  .lt_green(small_block('10'))
                  .lt_yellow(small_block('11'))
                  .lt_blue(small_block('12'))
                  .lt_magenta(small_block('13'))
                  .lt_cyan(small_block('14'))
                  .lt_white(small_block('15'))
                  .flush()
                  .bg_black(small_block('16'))
                  .bg_red(small_block('17'))
                  .bg_green(small_block('18'))
                  .bg_yellow(small_block('19'))
                  .bg_blue(small_block('20'))
                  .bg_magenta(small_block('21'))
                  .bg_cyan(small_block('22'))
                  .bg_white(small_block('23'))
                  .flush()
                  .bg_lt_black(small_block('24'))
                  .bg_lt_red(small_block('25'))
                  .bg_lt_green(small_block('26'))
                  .bg_lt_yellow(small_block('27'))
                  .bg_lt_blue(small_block('28'))
                  .bg_lt_magenta(small_block('29'))
                  .bg_lt_cyan(small_block('30'))
                  .bg_lt_white(small_block('31'))
                  .flush()
                  .text(large_block('normal'))
                  .bold(large_block('bold')).reset()
                  .underline(large_block('underline')).reset()
                  .reversed(large_block('reversed'))
                  .flush()
                  .err(large_block('FAIL'))
                  .ok(large_block('OK'))
                  .warn(large_block('WARN'))
                  .info(large_block('INFO'))
                  .flush()
    )
