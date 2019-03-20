__author__ = 'tkraus-m'

from kubernetes import client, config, watch
from pprint import pprint
import yaml
import json


def main():

    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:\n")
    print("%-20s\t%-40s\t%-6s" % ("NAMESPACE", "POD_NAME", "POD_IP"))
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%-20s\t%-40s\t%-6s" %
              (i.metadata.namespace, i.metadata.name, i.status.pod_ip))


if __name__ == '__main__':
    main()
