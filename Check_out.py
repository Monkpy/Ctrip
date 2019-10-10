import time
import re


class Ck_out(object):

    def check_out(self, check):
        # check = input('离店时间：xxxx-xx-xx')  # 2019-03-26
        pat_ci = re.search('\d{4}-\d{1,2}-\d{1,2}', check)
        if pat_ci:
            spl = pat_ci[0].split('-')
            if spl[0] == time.strftime('%Y'):
                if len(spl[1]) == 1:
                    spl[1] = '0' + spl[1]
                    if spl[1] > time.strftime('%m') and '01' < spl[1] < '12':
                        if len(spl[2]) == 1:
                            spl[2] = '0' + spl[2]
                            if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                return check
                            else:
                                if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                    return check
                                else:
                                    if spl[2] <= '28' and spl[1] == 2:
                                        return check
                                    else:
                                        print('请重新输入...')
                                        ck_out.check_out(check)
                        else:
                            if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                return check
                            else:
                                if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                    return check
                                else:
                                    if spl[2] <= '28' and spl[1] == 2:
                                        return check
                                    else:
                                        print('请重新输入...')
                                        ck_out.check_out(check)

                    else:
                        if spl[1] == time.strftime('%m'):
                            if len(spl[2]) == 1:
                                spl[2] = '0' + spl[2]
                                if spl[2] > time.strftime('%d'):
                                    if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                        return check
                                    else:
                                        if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                            return check
                                        else:
                                            if spl[2] <= '28' and spl[1] == 2:
                                                return check
                                            else:
                                                print('请重新输入...')
                                                ck_out.check_out(check)
                                else:
                                    print('请重新输入...')
                                    ck_out.check_out(check)
                            else:
                                if spl[2] > time.strftime('%d'):
                                    if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                        return check
                                    else:
                                        if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                            return check
                                        else:
                                            if spl[2] <= '28' and spl[1] == 2:
                                                return check
                                            else:
                                                print('请重新输入...')
                                                ck_out.check_out(check)
                                else:
                                    print('请重新输入...')
                                    ck_out.check_out(check)

                        print('请重新输入...')
                        ck_out.check_out(check)
                else:
                    if spl[1] > time.strftime('%m') and '01' < spl[1] < '12':
                        if len(spl[2]) == 1:
                            spl[2] = '0' + spl[2]
                            if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                return check
                            else:
                                if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                    return check
                                else:
                                    if spl[2] <= '28' and spl[1] == 2:
                                        return check
                                    else:
                                        print('请重新输入...')
                                        ck_out.check_out(check)
                        else:
                            if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                return check
                            else:
                                if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                    return check
                                else:
                                    if spl[2] <= '28' and spl[1] == 2:
                                        return check
                                    else:
                                        print('请重新输入...')
                                        ck_out.check_out(check)

                    else:
                        if spl[1] == time.strftime('%m'):
                            if len(spl[2]) == 1:
                                spl[2] = '0' + spl[2]
                                if spl[2] > time.strftime('%d'):
                                    if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                        return check
                                    else:
                                        if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                            return check
                                        else:
                                            if spl[2] <= '28' and spl[1] == 2:
                                                return check
                                            else:
                                                print('请重新输入...')
                                                ck_out.check_out(check)
                                else:
                                    print('请重新输入...')
                                    ck_out.check_out(check)
                            else:
                                if spl[2] > time.strftime('%d'):
                                    if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                        return check
                                    else:
                                        if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:
                                            return check
                                        else:
                                            if spl[2] <= '28' and spl[1] == 2:
                                                return check
                                            else:
                                                print('请重新输入...')
                                                ck_out.check_out(check)
                                else:
                                    print('请重新输入...')
                                    ck_out.check_out(check)
                        else:
                            print('请重新输入...')
                            ck_out.check_out(check)
            else:
                print('请重新输入(入离店住)时间：xxxx-xx-xx')
                ck_out.check_out(check)
        else:
            print('请重新输入...')
            ck_out.check_out(check)


if __name__ == '__main__':
    ck_out = Ck_out()
