## Example of deployment application con Kubernetes

### Author: RafaelTorices

This is an example of deployment application con Kubernetes of simple application, in this case, a python flask web calculator.

## Requirements

- Cluster Kubernetes
- Image docker of application
- Kubectl
- Helm
- Ingress controller

## Steps to deploy manifests in Kubernetes

1. Git clone this repository
2. Create a namespace in Kubernetes (optional, can use default namespace)
3. Apply the deployment, service and ingress yaml files
   ```
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    kubectl apply -f k8s/ingress.yaml
   ```

## Steps to deploy in Kubernetes with Helm

1. Git clone this repository
2. Create a namespace in Kubernetes (optional, can use default namespace)
3. Install the helm chart
   ```
    helm install pycalc helm/app
   ```

