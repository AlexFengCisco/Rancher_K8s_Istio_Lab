
## remove rancher agent 
## after remove host from stack , do the following in node

docker rm -f $(docker ps -qa)
reboot
rm -rf /var/lib/rancher/state

systemctl stop firewalld
firewall-cmd --state 


## start rancher

sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher

docker image rm -f $(docker images -qa)


==============================================================
sudo docker rm -f $(sudo docker ps -qa)
sudo rm -rf /var/etcd
for m in $(sudo tac /proc/mounts | sudo awk '{print $2}'|sudo grep /var/lib/kubelet);do
 sudo umount $m||true
done
sudo rm -rf /var/lib/kubelet/
for m in $(sudo tac /proc/mounts | sudo awk '{print $2}'|sudo grep /var/lib/rancher);do
 sudo umount $m||true
done
sudo rm -rf /var/lib/rancher/
sudo rm -rf /run/kubernetes/
sudo docker volume rm $(sudo docker volume ls -q)
sudo docker ps -a
sudo docker volume ls

rm -rf /etc/ceph \
       /etc/cni \
       /etc/kubernetes \
       /opt/cni \
       /opt/rke \
       /run/secrets/kubernetes.io \
       /run/calico \
       /run/flannel \
       /var/lib/calico \
       /var/lib/etcd \
       /var/lib/cni \
       /var/lib/kubelet \
       /var/lib/rancher/rke/log \
       /var/log/containers \
       /var/log/pods \
       /var/run/calico


kubectl run -i --tty ubuntu --image=ubuntu:16.04 --restart=Never -- bash -il
apt-get update && apt-get install mysql-client -y
mysql -h mysql -p


## API lab

endpoint
https://10.75.58.92:8443/v3

username access-key
token-q586x

password secfret-key
6kdflbst8h44rfj5fmk9mxdx88rdf89sjrqh7k6qjswtk8kcs5fzt7

Bearer Token:
token-q586x:6kdflbst8h44rfj5fmk9mxdx88rdf89sjrqh7k6qjswtk8kcs5fzt7














