from __future__ import annotations
from hue import Hue


if __name__ == '__main__':
    print(
        Hue().black('0  '.rjust(6))
             .red('1  '.rjust(6))
             .green('2  '.rjust(6))
             .yellow('3  '.rjust(6))
             .blue('4  '.rjust(6))
             .magenta('5  '.rjust(6))
             .cyan('6  '.rjust(6))
             .white('7  '.rjust(6)))

    print(
        Hue().lt_black('8  '.rjust(6))
             .lt_red('9  '.rjust(6))
             .lt_green('10  '.rjust(6))
             .lt_yellow('11  '.rjust(6))
             .lt_blue('12  '.rjust(6))
             .lt_magenta('13  '.rjust(6))
             .lt_cyan('14  '.rjust(6))
             .lt_white('15  '.rjust(6)))

    print(
        Hue().black_bg('16  '.rjust(6))
             .red_bg('17  '.rjust(6))
             .green_bg('18  '.rjust(6))
             .yellow_bg('19  '.rjust(6))
             .blue_bg('20  '.rjust(6))
             .magenta_bg('21  '.rjust(6))
             .cyan_bg('22  '.rjust(6))
             .white_bg('23  '.rjust(6)))

    print(
        Hue().lt_black_bg('24  '.rjust(6))
             .lt_red_bg('25  '.rjust(6))
             .lt_green_bg('26  '.rjust(6))
             .lt_yellow_bg('27  '.rjust(6))
             .lt_blue_bg('28  '.rjust(6))
             .lt_magenta_bg('29  '.rjust(6))
             .lt_cyan_bg('30  '.rjust(6))
             .lt_white_bg('31  '.rjust(6)))
    print(
        Hue().text('normal   '.rjust(12))
             .bold('bold    '.rjust(12))
             .reset()
             .underline('underline  '.rjust(12))
             .reset()
             .reversed('reversed  '.rjust(12)))
    print()
    
    print(Hue().fail('Something went wrong.'))
    print(Hue().ok('Everything is fine.'))
    print(Hue().warn('Need attention.'))
    print(Hue().info('Some information.'))
