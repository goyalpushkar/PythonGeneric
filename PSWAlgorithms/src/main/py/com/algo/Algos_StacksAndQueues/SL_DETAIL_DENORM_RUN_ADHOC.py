import os

if __name__ == '__main__':
    datesToRun = ['13-06-2020', '14-06-2020', '15-06-2020','16-06-2020','17-06-2020','18-06-2020']
    gp_by_acct_nbr = "63251#21700#62750#48300#31001#62630#62456#68301#49302"

    print(gp_by_acct_nbr)
    for date_index in range(len(datesToRun)):
        date_to_run = datesToRun[date_index]

        print(date_to_run)

        os.system('python /u01/apps/config/dplengine/app.py /u01/apps/config/dplengine/slconfig/SL_DETAIL_DENORM.yml ASD=$date_to_run, GrpAcctNo=$gp_by_acct_nbr, RUN_ID=1')
        os.system('python /u01/apps/config/dplengine/app.py /u01/apps/config/dplengine/slconfig/SL_DETAIL_DENORM_UNAUTH.yml ASD=$date_to_run, GrpAcctNo=$gp_by_acct_nbr, RUN_ID=2')