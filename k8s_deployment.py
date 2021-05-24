from os import path

import yaml
#import json

from kubernetes import client, config


def create_service():
    core_v1_api = client.CoreV1Api()
    body = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name="nginx"
        ),
        spec=client.V1ServiceSpec(
            selector={"app": "nginx"},
            ports=[client.V1ServicePort(
                port=80,
                target_port=80
            )]
        )
    )
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    core_v1_api.create_namespaced_service(namespace="alexnamespace01", body=body)

def list_service(namespace):
    core_v1_api = client.CoreV1Api()
    resp = core_v1_api.list_namespaced_service_with_http_info(namespace)
    data,status,header = resp
    #print(data.items)
    service_list = []
    for i in data.items:
        if i.spec.type == 'NodePort':
            service_list.append([i.metadata.name,i.spec.type,i.spec.ports[0].node_port])
        else:
            service_list.append([i.metadata.name,i.spec.type,i.spec.ports[0].port])
    return service_list

def list_endpoints(namespace):
    core_v1_api = client.CoreV1Api()
    resp = core_v1_api.list_namespaced_endpoints_with_http_info(namespace)
    print(resp)

def create_deployment():


    with open(path.join(path.dirname(__file__), "k8s_nginx-deployment.yaml")) as f:
        dep = yaml.safe_load(f)

        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="alexnamespace01")
        print("Deployment created. status='%s'" % resp.metadata.name)

def create_ingress():
    networking_v1_beta1_api = client.NetworkingV1beta1Api()

    body = client.NetworkingV1beta1Ingress(
        api_version="networking.k8s.io/v1beta1",
        kind="Ingress",
        metadata=client.V1ObjectMeta(name="nginx", annotations={
            "nginx.ingress.kubernetes.io/rewrite-target": "/"
        }),

        spec=client.NetworkingV1beta1IngressSpec(
            rules=[client.NetworkingV1beta1IngressRule(
                host="nginx.10.75.58.92.xip.io",
                http=client.NetworkingV1beta1HTTPIngressRuleValue(
                    paths=[client.NetworkingV1beta1HTTPIngressPath(
                        path="/",
                        backend=client.NetworkingV1beta1IngressBackend(
                            service_port=80,
                            service_name="nginx")

                    )]
                )
            )
            ]
        )
    )
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    networking_v1_beta1_api.create_namespaced_ingress(
        namespace="alexnamespace01",
        body=body
    )

def list_ingress(namespace):
    networking_v1_beta1_api = client.NetworkingV1beta1Api()
    #n = client.NetworkingV1Api()
    #resp = client.NetworkingV1beta1HTTPIngressPath()

    resp = networking_v1_beta1_api.list_namespaced_ingress_with_http_info(namespace)
    data,status,header = resp
    #print(status)
    #print(header)
    #print(data.items)
    ingress_list = []
    for i in data.items:
        for j in i.spec.rules:
            #print(j.host)
            ingress_list.append([i.metadata.name,j.host])
        #print("="*100)
    return ingress_list

def list_namespace():
    core_v1_api = client.CoreV1Api()
    namespaces = core_v1_api.list_namespace()
    namespace_list = []
    #print(namespaces)

    for namespace in namespaces.items:
        namespace_list.append(namespace.metadata.name)

    return namespace_list

def istio_service():

    pass
    #TODO try k8s istio api
    #dep = yaml.safe_load(f)

    k8s_apps_v1 = client.AppsV1Api()
    #k8s_apps_v1.delete_na

def create_istio_vs():


    with open(path.join(path.dirname(__file__), "istio_mysql_vs.yaml")) as f:
        dep = yaml.safe_load(f)

        k8s_apps_v1 = client.AppsV1Api()

        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="mysql")
        print("Deployment created. status='%s'" % resp.metadata.name)



if __name__ == '__main__':
    # kube config file ~/.kube.config
    config.load_kube_config()

    namespace_list = list_namespace()
    for namespace in namespace_list:
        print(namespace)

    print("="*100)
    namespace = 'alexnamespace01'

    #create_deployment()
    #create_service()
    #create_ingress()


    namespace = 'alexnamespace01'
    service_list = list_service(namespace)
    for name,type,nodeport in service_list:
        print('{} {} {}'.format(name,type,nodeport))

    print("="*100)

    list_endpoints(namespace)

    ingress_list = list_ingress(namespace)
    for name,host in ingress_list:
        print('{} {}'.format(name,host))

    print("=" * 100)

    #create_istio_vs()