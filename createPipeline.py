import boto3

def lambda_handler(event, context):
    client = boto3.client('codepipeline')
    response = client.create_pipeline(
        pipeline={
            'name': '<pipeline name>',
            'roleArn': '<Role ARN>'
            'artifactStore': {
                'type': 'S3',
                'location': '<bucket name>'
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
                                'RepositoryName': '<repository name>',
                                'BranchName': '<branch name>'
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

