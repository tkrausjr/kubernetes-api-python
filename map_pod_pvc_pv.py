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

    config.load_kube_config()
    api = client.CoreV1Api()

    # Load the PODs, PVCS, and PVS Objects
    # PVS not currently used - Only needed this for actual SIZE Of the PV if it is different than what was requrested in PVC

    pods = api.list_pod_for_all_namespaces(watch=False)
    pvcs = api.list_namespaced_persistent_volume_claim(namespace="", watch=False)
    pvs = api.list_persistent_volume(
        watch=False)

    # HACKY - Python doesnt natively support pandas like DB Table functionality
    # Need to build a LIST of DICTS. List below
    # Dicts will be appended in the loop
    pod_storage_list = []

    for i in pods.items:
        pod_pvcs = i.spec.volumes[0].persistent_volume_claim

        #Check for truthiness of pod_pvc to see if it contains anything or is None
        if pod_pvcs:
            pod_storage_dict = {}
            pod_pvc = i.spec.volumes[0].persistent_volume_claim.claim_name
            pod_storage_dict['pod_namespace'] = i.metadata.namespace
            pod_storage_dict['pod_name'] = i.metadata.name
            pod_storage_dict['pod_pvc'] = i.spec.volumes[0].persistent_volume_claim.claim_name

            for j in pvcs.items:
                if j.metadata.name == i.spec.volumes[0].persistent_volume_claim.claim_name:
                    pod_storage_dict['pod_volume_name'] = j.spec.volume_name
                    pod_storage_dict['pod_pvc_request_size'] = j.spec.resources.requests['storage']
                    #DEBUG
                    # print("POD Storage Dict " + str(pod_storage_dict))
            pod_storage_list.append(pod_storage_dict)
        else:
            pvc = "N/A"

    # Now crack open the LIST of DICTS
    print("pod_storage_list = " + str(pod_storage_list))
    print('\nOpen up the LIST of DICTS stored in pod_storage_list ')
    print('Found {} PODs with Persistent Volume Claims'.format(len(pod_storage_list)))
    for x in pod_storage_list:
        print('\n')
        for key, value in x.items():
            print('{}: {}'.format(key, value))




main()



