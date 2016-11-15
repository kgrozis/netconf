'''
Name: get-config.py
Python: 2.7
Description: Connects to router using NetConf.  Once connected retrieve YANG XML models.
'''

#from ydk.services import CRUDService
from ydk.services import NetconfService
from ydk.providers import NetconfServiceProvider
#from ydk.models.cisco_ios_xr import Cisco_IOS_XR_shellutil_oper \
#    as xr_shellutil_oper
#from datetime import timedelta


if __name__ == "__main__":
    # create NETCONF session
    provider = NetconfServiceProvider(address="10.82.79.35",
                                      port=830,
                                      username="cisco",
                                      password="cisco",
                                      protocol="ssh")
    cfg = NetconfService()
    print(cfg.commit(provider))
    #cfg = get_config(provider)
    # create CRUD service
    #crud = CRUDService()

    # create system time object
    #system_time = xr_shellutil_oper.SystemTime()

    # read system time from device
    #system_time = crud.read(provider, system_time)

    # print system uptime
    #print("System uptime is " +
    #     str(timedelta(seconds=system_time.uptime.uptime)))

    # close NETCONF session and exit
    provider.close()
    exit()