from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild
)
from constructs import Construct

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Define a CodeBuild project
        build_project = codebuild.PipelineProject(self, "BuildProject",
                                                  build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml")
                                                  )

        # Define the pipeline
        pipeline = codepipeline.Pipeline(self, "Pipeline")

        # Add source stage with GitHub V2 via AWS CodeStar Connections
        source_output = codepipeline.Artifact()
        pipeline.add_stage(
            stage_name="Source",
            actions=[
                codepipeline_actions.CodeStarConnectionsSourceAction(
                    action_name="GitHub_Source",
                    owner="PiyushJainGK",  # GitHub Username
                    repo="cdk-codepipeline",  # GitHub Repository Name
                    branch="feature_cdk_pipeline",  # GitHub Branch Name
                    connection_arn="arn:aws:codeconnections:us-east-1:539247462650:connection/b7754098-1b5b-49fc-9055-257e6d964c57",
                    output=source_output
                )
            ]
        )

        # Add build stage
        pipeline.add_stage(
            stage_name="Build",
            actions=[
                codepipeline_actions.CodeBuildAction(
                    action_name="CodeBuild",
                    project=build_project,
                    input=source_output
                )
            ]
        )
