from brainbase_labs import BrainbaseLabs
import os

# load from .env
from dotenv import load_dotenv
load_dotenv()

# create brainbase client
if os.environ["DEPLOYMENT_TYPE"] == "development":
    bb = BrainbaseLabs(
        base_url=os.environ["BRAINBASE_BASE_URL"],
        api_key=os.environ["BRAINBASE_API_KEY"]
    )
else:
    bb = BrainbaseLabs(
        api_key=os.environ["BRAINBASE_API_KEY"]
    )

# 1. list workers
workers = bb.workers.list()
# print(workers)

# 2. create worker
new_worker = bb.workers.create(
    name="Hello World Worker",
    description="Converse with the user",
    status="active"
)
print(new_worker.id)

# 3. create new flow version
new_flow = bb.workers.flows.create(
    worker_id=new_worker.id,
    path="1_hello_world.based",
    name="Hello World",
    label="v1",
    validate=False
)
print(new_flow.id)