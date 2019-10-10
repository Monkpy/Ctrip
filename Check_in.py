import re
import time


class Ck_in(object):

    def check_in(self, check):
        # check = input('入住时间：xxxx-xx-xx')  # 2019-03-26
        pat_ci = re.search('\d{4}-\d{1,2}-\d{1,2}', check)  # 时间格式化抓取
        if pat_ci:
            spl = pat_ci[0].split('-')  # 切片处理
            if spl[0] == time.strftime('%Y'):  # 判断输入年份是否与当前年份相等
                if len(spl[1]) == 1:  # 判断月份位数
                    spl[1] = '0' + spl[1]  # 月份不足两位的填0
                    if spl[1] > time.strftime('%m') and '01' < spl[1] < '12':  # 月份大于当月且在12个月当中
                        if len(spl[2]) == 1:  # 判断日期位数
                            spl[2] = '0' + spl[2]  # 日期位数不足两位前面填0
                            if spl[2] <= '31' and spl[1] in ['01', '03', '05', '07', '08', '10', '12']:  # 日期小于31天
                                return check  # 格式，日期正确返回时间
                            else:
                                if spl[2] <= '30' and spl[1] in ['04', '06', '09', '11']:  # 日期小于30天
                                    return check
                                else:
                                    if spl[2] <= '28' and spl[1] == 2:  # 特殊日期28天（闰年2月没有判断）
                                        return check
                                    else:
                                        print('请重新输入...')
                                        ck_in.check_in(check)
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
                                        ck_in.check_in(check)

                    else:
                        if spl[1] == time.strftime('%m'):
                            if len(spl[2]) == 1:
                                spl[2] = '0' + spl[2]
                                if spl[2] >= time.strftime('%d'):
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
                                                ck_in.check_in(check)
                                else:
                                    print('请重新输入...')
                                    ck_in.check_in(check)
                            else:
                                if spl[2] >= time.strftime('%d'):
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
                                                ck_in.check_in(check)
                                else:
                                    print('请重新输入...')
                                    ck_in.check_in(check)

                        print('请重新输入...')
                        ck_in.check_in(check)
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
                                        ck_in.check_in(check)
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
                                        ck_in.check_in(check)

                    else:
                        if spl[1] == time.strftime('%m'):
                            if len(spl[2]) == 1:
                                spl[2] = '0' + spl[2]
                                if spl[2] >= time.strftime('%d'):
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
                                                ck_in.check_in(check)
                                else:
                                    print('请重新输入...')
                                    ck_in.check_in(check)
                            else:
                                if spl[2] >= time.strftime('%d'):
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
                                                ck_in.check_in(check)
                                else:
                                    print('请重新输入...')
                                    ck_in.check_in(check)
                        else:
                            print('请重新输入...')
                            ck_in.check_in(check)
            else:
                print('请重新输入...')
                ck_in.check_in(check)
        else:
            print('请重新输入...')
            ck_in.check_in(check)


if __name__ == '__main__':
    ck_in = Ck_in()




