

Istio Lab

#Project needs to be enable and install istio first 
dont forget to enable ingress gateway , disabled by default

# Deploy bookinfo sample 

https://archive.istio.io/v1.2/zh/docs/examples/bookinfo/

kubectl label namespace bookinfo istio-injection=enabled

kubectl config set-context --current --namespace=bookinfo   # change current namespace from default to bookinfo

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.2/samples/bookinfo/platform/kube/bookinfo.yaml 

kubectl get services
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
details       ClusterIP   10.43.241.198   <none>        9080/TCP   6m38s
productpage   ClusterIP   10.43.81.169    <none>        9080/TCP   6m37s
ratings       ClusterIP   10.43.195.133   <none>        9080/TCP   6m38s
reviews       ClusterIP   10.43.202.250   <none>        9080/TCP   6m38s

kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-78d78fbddf-z5d6k       2/2     Running   0          7m8s
productpage-v1-596598f447-vlnx4   2/2     Running   0          7m7s
ratings-v1-6c9dbf6b45-72jv5       2/2     Running   0          7m8s
reviews-v1-7bb8ffd9b6-xsptb       2/2     Running   0          7m8s
reviews-v2-d7d75fff8-tvpcv        2/2     Running   0          7m8s
reviews-v3-68964bc4c8-sn2b6       2/2     Running   0          7m8s

#verify bookinfo 
kubectl exec -it $(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}') -c ratings -- curl productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
                                   
#create virtual service gateway
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.2/samples/bookinfo/networking/bookinfo-gateway.yaml 

> kubectl get gateway
NAME               AGE
bookinfo-gateway   51s

#export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT # change to NodePort mapping
## just setup normal ingress load balancer , service = productpage


## setup destination rule before apply istio virtual service

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.2/samples/bookinfo/networking/destination-rule-all.yaml

#apply yaml create virtual service 
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.2/samples/bookinfo/networking/virtual-service-all-v1.yaml










