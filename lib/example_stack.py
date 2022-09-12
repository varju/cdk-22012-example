from constructs import Construct
from aws_cdk import Stack
import aws_cdk.aws_lambda as lambdas
from aws_cdk.aws_lambda_python_alpha import PythonLayerVersion


class ExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        PythonLayerVersion(
                self,
                'LibraryLayer',
                entry='layer',
                compatible_runtimes=[lambdas.Runtime.PYTHON_3_9],
                compatible_architectures=[lambdas.Architecture.ARM_64],
            )
