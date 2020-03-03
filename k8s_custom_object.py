"""
  Use costum object api for istio K8s operation,

"""

from pprint import pprint as pp
from os import path
from kubernetes import client, config
import time

import yaml


def create_namespaced_customer_object(namespace,plural,object_file):
    with open(path.join(path.dirname(__file__), object_file)) as f:
        dep = yaml.safe_load(f)
        resp = customObjectApi.create_namespaced_custom_object(ISTIO_API,
                                                        ISTIO_API_VERSION,
                                                        namespace,
                                                        plural,
                                                        body=dep)
        #print('Virtual Service {} created. '.format(resp['metadata']['name']))
        return resp

def delete_namespaced_custom_object(name,namespace,plural):

    resp = customObjectApi.delete_namespaced_custom_object(ISTIO_API,
                                                           ISTIO_API_VERSION,
                                                           namespace,
                                                           plural,
                                                           name,
                                                           body=client.V1DeleteOptions(),)
    return resp

def list_namespaced_custome_object(namespace,plural):

    resp = customObjectApi.list_namespaced_custom_object(ISTIO_API,
                                                         ISTIO_API_VERSION,
                                                         namespace,
                                                         plural)
    return resp

def get_namespaced_custome_object(name,namespace,plural):

    resp = customObjectApi.get_namespaced_custom_object(ISTIO_API,
                                                         ISTIO_API_VERSION,
                                                         namespace,
                                                         plural,name)
    return resp

def patch_namespaced_custom_object(name,namespace,plural,object_file):

    with open(path.join(path.dirname(__file__), object_file)) as f:
        dep = yaml.safe_load(f)

        resp = customObjectApi.patch_namespaced_custom_object(ISTIO_API,
                                                               ISTIO_API_VERSION,
                                                               namespace,
                                                               plural,
                                                               name,
                                                               body=dep)
    return resp

if __name__ == "__main__":


    config.load_kube_config()

    customObjectApi = client.CustomObjectsApi()

    ISTIO_API = 'networking.istio.io'
    ISTIO_API_VERSION = 'v1alpha3'

    object_file = 'istio_mysql_vs.yaml'
    namespace = 'mysql'
    plural = 'virtualservices'

    '''
    plural for istio service mesh object 
    plural = virtualservices
             gateways
             destinationrules
    '''

    resp = delete_namespaced_custom_object('mysql01',namespace,plural)
    print('virtual service {} was deleted {}.'.format(resp['details']['name'],resp['status']))

    time.sleep(5)
    resp = create_namespaced_customer_object(namespace,plural,object_file)
    print('Virtual Service {} created. '.format(resp['metadata']['name']))

    namespace = 'bookinfo'
    object_file = 'istio_bookinfo_reviews.yaml'
    resp = patch_namespaced_custom_object('reviews',namespace,plural,object_file)
    pp(resp)

    namespace = 'bookinfo'

    resp = list_namespaced_custome_object(namespace,plural)
    pp(resp)

    resp = get_namespaced_custome_object('reviews',namespace,plural)
    pp(resp)
