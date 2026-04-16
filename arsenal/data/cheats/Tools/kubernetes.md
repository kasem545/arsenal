# kubernetes

% kubernetes, k8s, kubectl

#plateform/linux #target/local #cat/UTILS 

## Print all contexts
```
kubectl config get-contexts
```

## Print current context of kubeconfig
```
kubectl config current-context
```

## Set context of kubeconfig
```
kubectl config use-context <context>
```

## Print resource documentation
```
kubectl explain <resource>
```

## Get nodes (add option '-o wide' for details)
```
kubectl get nodes
```

## Get namespaces
```
kubectl get namespaces
```

## Get pods from namespace (add option '-o wide' for details)
```
kubectl get pods -n <NAMESPACE>
```

## Get pods from all namespace (add option '-o wide' for details)
```
kubectl get pods --all-namespaces
```

## Get services from namespace
```
kubectl get services -n <NAMESPACE>
```

## Get details from resource on namespace
```
kubectl describe <resource>/<NAME> -n <NAMESPACE>
```

## Print logs from namespace
```
kubectl logs -f pods/<NAME> -n <NAMESPACE>
```

## Get deployments
```
kubectl get deployments -n <NAMESPACE>
```

## Edit deployments
```
kubectl edit deployment/<NAME> -n <NAMESPACE>
```

## Drain node in preparation for maintenance
```
kubectl drain <NAME>
```

## Mark node as schedulable
```
kubectl uncordon <NAME>
```

## Mark node as unschedulable
```
kubectl cordon <NAME>
```

## Display resource (cpu/memory/storage) usage
```
kubectl top <type>
```