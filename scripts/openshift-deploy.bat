oc apply -f es-deployment.yaml
oc apply -f es-svc.yaml

oc apply -f elastic-search-deployment.yaml
oc apply -f elastic-search-svc.yaml
oc apply -f elastic-search-route.yaml