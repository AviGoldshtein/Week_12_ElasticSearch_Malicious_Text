from core.manager import Manager
import json


manager = Manager()
# manager.initialize_data()
res = manager.get_all_data()[0]
print(json.dumps(res, indent=4))