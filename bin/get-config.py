'''
Name: get-config.py
Python: 2.7
Description: Connects to router using NetConf.  Once connected retrieve YANG XML models.
'''

from ydk.services import NetconfService, Datastore
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ip_domain_cfg \
    as xr_ip_domain_cfg
import logging

if __name__ == "__main__":
    # create NETCONF session
    provider = NetconfServiceProvider(address="10.82.79.35",
                                      port=830,
                                      username="cisco",
                                      password="cisco",
                                      protocol="ssh")

   # Create NetConfService instance
    cfg = NetconfService()

    # Commit XRv9K prior to retrieving configuration
    print(cfg.commit(provider))

    # create object 
    ip_domain = xr_ip_domain_cfg.IpDomain()

    # get configuration from netconf device 
    ip_domain = cfg.get_config(provider, Datastore.running, ip_domain)

    # close NETCONF session and exit
    provider.close()
    exit()