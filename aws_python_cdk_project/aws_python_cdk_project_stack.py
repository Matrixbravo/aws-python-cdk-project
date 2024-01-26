import os
from aws_cdk import core
from aws_cdk import aws_cloudformation as cfn
from constructs import Construct

class AwsPythonCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str,include_services: list, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Read and deploy CloudFormation templates from the 'templates folder'
        templates_folder = os.path(os.path.dirname(__file__), 'templates')
        
        for service in include_services:
            self.include_services_templates(templates_folder, service)
            
    def include_services_template(self, templates_folder: str, service: str) -> None:
        service_template_path = os.path.join(templates_folder, f'{service.lower()}_template.yaml')
        
        if os.path.exists(service_template_path):
            core.CfnInclude(self, f'{service.capitalize()}Stack',template=service_template_path)
        else:
            print(f"Template for {service} not found at {service_template_path}")
            

app = core.App()
AwsPythonCdkProjectStack(app, 'MyStack', include_services=['VPC'])
app.synth()