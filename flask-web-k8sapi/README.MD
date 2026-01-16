
## 1 - Build Web Application that talks to K8s API
Create the Python Code. This step is already done for you. File is flask-k8sapi.py.

## 2 - Build Docker Image from your Web Application
```
 git clone https://github.com/tkrausjr/kubernetes-api-python.git
 cd kubernetes-api-python/flask-web-k8sapi
 sudo docker build -t harbor.mbentley.net/tkraus/flask-k8sapi:v1 .
 sudo docker images
 sudo docker login harbor.mbentley.net
 sudo docker push harbor.mbentley.net/tkraus/flask-k8sapi:v1
```
## 3 - Build / Update Kubernetes object YAML
Update the flask-k8sapi-deploy.yaml file in ./kubernetes folder to reflect whatever registry you pushed the docker image to. Change the ***spec.template.spec.containers[0].image:*** field in the Deployment Manifest (***flask-k8sapi-deploy.yaml*** ). 

## 4 - Deploy Kubernetes objects
```
kubectl vsphere login --server 10.1.8.6 --vsphere-username administrator@vsphere.local --insecure-skip-tls-verify --tanzu-kubernetes-cluster-name vks-01 --tanzu-kubernetes-cluster-namespace testing123
kubectl label --overwrite ns default pod-security.kubernetes.io/enforce=privileged
kubectl apply -f ./kubernetes/
kubectl get svc -w
```
## 5 - Test the Python Flask Application

From a browser, access the application at ***http://<EXTERNAL-IP>*** on default port 80.


### Reference [Basic K8s API Flask App](https://www.google.com/search?q=build+a+simple+kubernetes+web+based+application+k8s+api&sca_esv=492d03d456b59a14&rlz=1C5GCCA_en&udm=50&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpV6Bbbmx4QVaoKkiRQ2jlwvCHF0Eqz8cUq4JjDCZnrJG3IQ9hSM-GoYfSAqo_zJgC8GHuEE9ehM7VlFnv8pyn_4gwgnnAqmsxpqy1E8YGqcDS9cptS67pcIpPqn4IMgzGMeCqJHb-zTRxeehyYmiPr22wi7vtH9t-0PG7m_AIs8H2mc6dH6OEJ2wczdXosTAaf6qSFA&aep=1&ntc=1&sa=X&ved=2ahUKEwjgusfchI6SAxVPMlkFHUvhMbUQ2J8OegQIBRAE&biw=1704&bih=963&dpr=2&aic=0&mstk=AUtExfASzBrNy4FZFO8ASFIrrjvkTaSOwyJrfh-l5t5IxCElfFQOEepkTRzNR1zKAfK0cuaSokPfj8T7xuwdoQ-D0PYubJZJUBwl5-jaDdo8kwnba8nn2Y3rclW10RbwqvuHRK-13SUZJWMpoGjCnK1HlArAMAi3zF2D6hq6vy9pg5w3DPoPYNJ5t4iVaYTONWM2yLXaTW_oLKxURj6BnQmS3_NN9THVIkf2SuOUKfYlMEKbgPdo0tHMsEB31Q&csuir=1&atvm=2).


