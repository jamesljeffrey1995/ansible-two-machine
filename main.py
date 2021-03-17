import os
import ast

ec2_info = os.environ["dictionary"]
ec2_info = ec2_info.strip()
ec2 = ast.literal_eval(ec2_info)
print(ec2["instances"][0]["instance_id"])

