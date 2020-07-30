### general python3.6+ scripts
* instances.py: lists all EC2 instances in a given account. Returns ID and IP when applicable. Depends on boto3, "regions" file (provided) and valid AWS credentials.
* listEC2.py: lists EC2 instances. Depends on boto3, and valid AWS credentials.
* list_all_pods.py: lists pods in a kubernetes cluster. Depends on a valid kubeconfig file.
* createPipeline.pt: Simple Lambda function to create a pipeline in CodePipeline
