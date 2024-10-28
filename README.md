# price-pred-ml-with-kube
Test ML pipelines under Kubernetes.

# Settings
Ubuntu, VM, SSH for remote access to VM, 
VSCode, Python, Node.js, Docker Extension, Kubernetes Extension, Cloud Code (Google Cloud Platform)
GitHub, Docker Hub, 
minikube, kubectl,

# Installation
pip3 install "fastapi[standard]"
pip3 install pandas
pip3 install xgboost
pip3 install -U scikit-learn

conntrack
sudo apt-get install conntrack

crictl
VERSION="v1.30.0" # check latest version in /releases page
curl -L https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-${VERSION}-linux-amd64.tar.gz --output crictl-${VERSION}-linux-amd64.tar.gz
sudo tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
rm -f crictl-$VERSION-linux-amd64.tar.gz

# Run the app
fastapi run app/main.py --port 8000

# Docker Image
docker build -t price-pred-ml-kube1:latest . 
docker run -d --name mycontainer1 -p 8000:8000 price-pred-ml-kube1
http://192.168.1.119/docs

docker run -p 8000:8000 price-pred-ml-kube1


docker run -d --name mycontainer2 -p 9000:8000 price-pred-ml-kube
http://192.168.1.119:9000/docs (working)

HD Docker Hub Registry: 
docker login hdingdockerdesktop

docker tag price-pred-ml-kube1:latest hdingdockerdesktop/price-pred-ml-kube1:latest
docker push hdingdockerdesktop/price-pred-ml-kube1:latest

# Kubenetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

minikube service list

kubectl get deployment price-pred-ml-kube-deployment
kubectl get service price-pred-ml-kube-service

kubectl get svc
kubectl get pods


(.venv) worker003@ubuntu-white-pc:~/github/price-pred-ml-with-kube$ lsof -i:8000
COMMAND      PID      USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
kubectl.1 341537 worker003    8u  IPv4 1350869      0t0  TCP localhost:8000 (LISTEN)
kubectl.1 341537 worker003    9u  IPv6 1350870      0t0  TCP ip6-localhost:8000 (LISTEN)
(.venv) worker003@ubuntu-white-pc:~/github/price-pred-ml-with-kube$ kill 341537
(.venv) worker003@ubuntu-white-pc:~/github/price-pred-ml-with-kube$ lsof -i:8000
(.venv) worker003@ubuntu-white-pc:~/github/price-pred-ml-with-kube$ 