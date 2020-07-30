import boto3

def lambda_handler(event, context):
    client = boto3.client('codepipeline')
    response = client.create_pipeline(
        pipeline={
            'name': 'bahpeline',
            'roleArn': 'arn:aws:iam::148765843611:role/service-role/AWSCodePipelineServiceRole-us-east-2-MyPipeline',
            'artifactStore': {
                'type': 'S3',
                'location': 'tellesma-codepipeline'
            },
            'stages': [
                {
                    'name': 'commit',
                    'actions': [
                        {
                            'name': 'CodeCommit',
                            'runOrder': 1,
                            'actionTypeId': {
                                'category': 'Source',
                                'owner': 'AWS',
                                'provider': 'CodeCommit',
                                'version': '1'
                            },
                            'outputArtifacts' : [
                                {
                                    'name': 'artifact_name_to_pass'
                                }
                            ],
                            'configuration': {
                                'RepositoryName': 'MyRepo',
                                'BranchName': 'master'
                            }
                        }
                    ]
                },
                {
                    'name': 'approval',
                    'actions': [
                        {
                            'name': 'Approval',
                            'runOrder': 2,
                            'actionTypeId': {
                                'category': 'Approval',
                                'owner': 'AWS',
                                'provider': 'Manual',
                                'version': '1'
                            }
                        }
                    ]
                }
            ],
        }
        )
    print(response)

