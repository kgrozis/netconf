#!/usr/bin/python
# coding=utf-8

from ncclient import manager
import logging, sys, os
from urlparse import parse_qs


def nc_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           device_params=None,
                           allow_agent=False,
                           look_for_keys=False,
                           timeout=30
            )


def parse_hello(connection):
    capabilities = []

    for capability in connection.server_capabilities:
        if capability.startswith('http'):
            for key in parse_qs(capability):
                if key.startswith('http'):
                    capabilities.append('           YANG --> ' + parse_qs(capability)[key][0])
        else:
            capability = capability.split(':')
            if capability[-1].startswith('1.'):
                capabilities.append('           ' + capability[1].upper() + ' --> ' + capability[-2] + ' ' + capability[-1])
            else:
                capabilities.append('           ' + capability[1].upper() + ' --> ' + capability[-1].split('?')[0])

    capabilities.sort()

    return connection.session_id, capabilities



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('NETCONF')

    #Variables
    host = sys.argv[1]
    #host = '172.16.159.113'
    port = 22
    user = os.getenv("USER")
    passwd = 'cisco'
    port = 830

    #Create Connection
    connection = nc_connect(host, port, user, passwd)

    id, capabilities = parse_hello(connection)

    #Session ID
    print 'Session ID: ', id
    print

    #Capabilities
    print 'Capabilities: '

    for capability in capabilities:
        print capability



'''
Optional Base Capabilities (RFC 6241)

url – the URL data store is supported (scheme=http, ftp, file, …)
startup – the startup data store is supported
writable-running – the running data store can be modified directly


Non-base capabilities

notification – Netconf asynchronous event messages (RFC 5277), also with interleave
'''


'''
Config on Router (IOS XR 5.3.0)

ssh server netconf port 830
netconf-yang agent ssh

'''

'''
USE:

./netconfxr.py host
assumes port 830, user same as OS, and password cisco


EXAMPLES:

a)
nleiva$ python netconfxr.py 172.16.159.113
Session ID:  4895

Capabilities:
           IETF --> base 1.1
           IETF --> candidate 1.0
           IETF --> ietf-inet-types
           IETF --> ietf-netconf-monitoring
           IETF --> ietf-yang-types
           IETF --> rollback-on-error 1.0
           IETF --> validate 1.1
           YANG --> Cisco-IOS-XR-cdp-cfg
           YANG --> Cisco-IOS-XR-cdp-oper
           YANG --> Cisco-IOS-XR-crypto-sam-cfg
           YANG --> Cisco-IOS-XR-crypto-sam-oper
           YANG --> Cisco-IOS-XR-ha-eem-cfg
           YANG --> Cisco-IOS-XR-ha-eem-oper
           YANG --> Cisco-IOS-XR-ifmgr-cfg
           YANG --> Cisco-IOS-XR-ifmgr-oper
           YANG --> Cisco-IOS-XR-infra-infra-cfg
           YANG --> Cisco-IOS-XR-ip-domain-cfg
           YANG --> Cisco-IOS-XR-ip-domain-oper
           YANG --> Cisco-IOS-XR-ip-iarm-datatypes
           YANG --> Cisco-IOS-XR-ipv4-io-cfg
           YANG --> Cisco-IOS-XR-ipv4-io-oper
           YANG --> Cisco-IOS-XR-ipv4-ma-cfg
           YANG --> Cisco-IOS-XR-ipv4-ma-oper
           YANG --> Cisco-IOS-XR-ipv6-ma-cfg
           YANG --> Cisco-IOS-XR-ipv6-ma-oper
           YANG --> Cisco-IOS-XR-lib-keychain-cfg
           YANG --> Cisco-IOS-XR-lib-keychain-oper
           YANG --> Cisco-IOS-XR-man-netconf-cfg
           YANG --> Cisco-IOS-XR-man-xml-ttyagent-cfg
           YANG --> Cisco-IOS-XR-man-xml-ttyagent-oper
           YANG --> Cisco-IOS-XR-parser-cfg
           YANG --> Cisco-IOS-XR-qos-ma-oper
           YANG --> Cisco-IOS-XR-rgmgr-cfg
           YANG --> Cisco-IOS-XR-rgmgr-oper
           YANG --> Cisco-IOS-XR-shellutil-cfg
           YANG --> Cisco-IOS-XR-shellutil-oper
           YANG --> Cisco-IOS-XR-tty-management-cfg
           YANG --> Cisco-IOS-XR-tty-management-datatypes
           YANG --> Cisco-IOS-XR-tty-management-oper
           YANG --> Cisco-IOS-XR-tty-server-cfg
           YANG --> Cisco-IOS-XR-tty-server-oper
           YANG --> Cisco-IOS-XR-tty-vty-cfg
           YANG --> Cisco-IOS-XR-types
nleiva$

'''
