'''
Supported APIs (* is preferred version):
core                                     v1
apiregistration.k8s.io                   *v1,v1beta1
extensions                               v1beta1
apps                                     v1
events.k8s.io                            v1beta1
authentication.k8s.io                    *v1,v1beta1
authorization.k8s.io                     *v1,v1beta1
autoscaling                              *v1,v2beta1,v2beta2
batch                                    *v1,v1beta1
certificates.k8s.io                      v1beta1
networking.k8s.io                        *v1,v1beta1
policy                                   v1beta1
rbac.authorization.k8s.io                *v1,v1beta1
storage.k8s.io                           *v1,v1beta1
admissionregistration.k8s.io             *v1,v1beta1
apiextensions.k8s.io                     *v1,v1beta1
scheduling.k8s.io                        *v1,v1beta1
coordination.k8s.io                      *v1,v1beta1
node.k8s.io                              v1beta1
discovery.k8s.io                         v1beta1
crd.projectcalico.org                    v1
monitoring.coreos.com                    v1
authentication.istio.io                  v1alpha1
rbac.istio.io                            v1alpha1
config.istio.io                          v1alpha2
networking.istio.io                      v1alpha3
security.istio.io                        v1beta1
cluster.cattle.io                        v3
metrics.k8s.io                           v1beta1
'''

from kubernetes import client, config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.


    config.load_kube_config()

    print("Supported APIs (* is preferred version):")
    print("%-40s %s" %
          ("core", ",".join(client.CoreApi().get_api_versions().versions)))



    for api in client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        print("%-40s %s" % (api.name, ",".join(versions)))


if __name__ == '__main__':
    main()
