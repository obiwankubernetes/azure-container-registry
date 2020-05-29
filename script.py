# make sure azure cli is installed and updated version
# az --version

# sign in to azure
# az login

# create resource group
# az group create --name ACRrg --location eastus

# create acr service
# az acr create --resource-group ACRrg --name SamACRTrainingHelloWorld --sku Basic --admin-enabled true

# login to acr service created
# az acr login --name SamACRTrainingHelloWorld

# Tag docker images for ACR purposes
# print list to see login server name
# az acr list --resource-group ACRrg --query "[].{acrLoginServer:loginServer}" --output table

# tag for ACR (used docker tutoial image instead of helloworld b/c it was working for some reason)
# docker tag docker101tutorial samacrtraininghelloworld.azurecr.io/docker101tutorial

# push to ACR
# docker push samacrtraininghelloworld.azurecr.io/docker101tutorial

# check to see docker image  is there in ACR
# az acr repository list --name SamACRTrainingHelloWorld --output table

# check to see tags in ACR
# az acr repository show-tags --name SamACRTrainingHelloWorld --repository docker101tutorial --output table