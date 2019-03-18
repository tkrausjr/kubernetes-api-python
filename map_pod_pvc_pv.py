__author__ = 'tkraus-m'

from kubernetes import client, config, watch
from pprint import pprint
import yaml
import json

## NEXT THING TO Work on is finding/printing the type of volume PV
## Use Python Interactive mode to find properties of
##
##
##
##

def main():

    ns = ""
    config.load_kube_config()
    api = client.CoreV1Api()

    # PVC Code
    try:
        pvcs = api.list_namespaced_persistent_volume_claim(
            namespace=ns, watch=False)
        print("\n---- PVCs ---\n")
        print("%-16s\t%-40s\t%-6s" % ("PVC_NAME", "PV", "PVC_REQUESTED"))
        for pvc in pvcs.items:
            print("%-16s\t%-40s\t%-6s" %
                  (pvc.metadata.name, pvc.spec.volume_name,
                   pvc.spec.resources.requests['storage']))
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_persistent_volume_claims %s\n" % e)

    # PV Code
    pvs = api.list_persistent_volume(
        watch=False)

    print("\n---- PVs ---\n")
    print("%-40s\t%-16s" % ("PV_NAME", "PV_CAPACITY"))
    for pv in pvs.items:
        print("%-40s\t%-16s" %  (pv.metadata.name,
                   pv.spec.capacity['storage']))

    '''
    # POD DEBUG Code to show entire response
    try:
        api_response = api.list_pod_for_all_namespaces( pretty=
                                                        True)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_pod_for_all_namespaces: %s\n" % e)
    '''

    # POD Code
    print("\n---- PODs ---\n")
    pods = api.list_pod_for_all_namespaces(watch=False)

    # SELECTIVE RESPONSE SHOW NS, POD NAME, and PVC
    print("%-20s\t%-40s\t%-6s" % ("POD_NAMESPACE", "POD_NAME", "PERSISTENT_VOLUME_CLAIM_0"))
    for i in pods.items:
        pod_pvc = i.spec.volumes[0].persistent_volume_claim
        if pod_pvc == None:
            pvc = "N/A"
        else:
            pvc = i.spec.volumes[0].persistent_volume_claim.claim_name


        print("%-20s\t%-40s\t%-6s" % (
                                             i.metadata.namespace,
                                             i.metadata.name, pvc
                                                    ))


main()


