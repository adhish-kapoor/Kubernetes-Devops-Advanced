## Link for code repo
`https://github.com/adhish-kapoor/Kubernetes-Devops-Advanced`

## Docker hub URL for docker images
`https://hub.docker.com/repository/docker/adhishkapoor1607/web-api/general`

## Expose the API to fetch records from DB
To Get all users: `http://34.67.248.81:8282/` is used.
34.67.248.81 is the External IP of LoadBalancer `web-service`.
8282 is the PORT used for my service.

# Below steps are for execution reference:

## Deploying a Flask API and MySQL server on Kubernetes
This repo contains code that 
1) Deploys a MySQL server on a Kubernetes cluster.
2) Attaches a persistent volume to it, so the data remains if pods are restarting.
3) Deploys a Flask Web API to fetch users from the MySQL database.

## Getting started
1. Clone the repository
2. Pull the latest mysql image from `Dockerhub`: `docker pull mysql`
3. Build image with the Dockerfile in this repo as `docker build -t <your-username>/<image> .` : 
   In my case it is `docker build -t adhishkapoor1607/web-api .`
4. Push the image to Dockerhub: `docker push adhishkapoor1607/web-api`

## Secrets
`Kubernetes Secrets` file `mysql-secret.yaml` to store password of root user of the MySQL server.

## Deployments
Get the secrets, persistent volume in place and apply the deployments for the `MySQL` database and `Flask Web API`

1. Add secrets to your `kubernetes cluster`: `kubectl create -f mysql-secret.yaml`
2. Create the `persistent volume` and `persistent volume claim` for the database: `kubectl apply -f mysql-pv.yaml`
3. Create the `MySQL` deployment: `kubectl apply -f mysql-pod.yaml`
4. Create MySQL service: `kubectl create -f mysql-service.yaml`
5. Create the `Flask API` deployment: `kubectl apply -f web-application-deployment.yaml`

## ConfigMap
In `config-map.yaml` file, replace MYSQL_ROOT_HOST value with the IP from command `kubectl get pod k8s-mysql -o template --template={{.status.podIP}}`.
Then use command `kubectl apply -f config-map.yaml`

## Creating table to insert records
1. Use command `kubectl exec k8s-mysql -it -- bash` to connect to MySQL pod.
2. Use command `mysql -u root -p` and enter the password in the bash.
3. Create table `users` in `mysql` database and insert records.
    



