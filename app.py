#!/usr/bin/env python3

import aws_cdk as cdk

from lib.example_stack import ExampleStack


app = cdk.App()
ExampleStack(app, "example")

app.synth()
