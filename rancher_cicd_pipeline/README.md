## Rancher 2.x CI/CD Pipeline Test

    Dockerfile
    deployment.yaml
    .rancher-pipeline,yml # created by rancher pipeline
    python https demo code with index.html
    
#### git client push    
    push to git and trigger rancher pipeline Git application webhook
    
#### pipeline started 
    
    step 1
    
    clone git repositoy to pipeline local
    
    step 2 stage
    
    docker compose with Dockerfile
    push docker image to docker hub
    
    step 3 stage
    deploy k8s deployment service and ingress load balance  with yaml file deployment.yaml

#### tips
    change docker image tag version before git push .....
    
    create deployment service and ingree load balancer from web UI, and copy the yaml file for pipeline
      

    
    