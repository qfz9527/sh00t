import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from configuration.models import ModuleMaster, CaseMaster


print("This will reset everything in the database and set up as fresh.")
print("Are you wanna do this?")
try:
    answer = raw_input("[No] | Yes?\n") or ""
except NameError:
    answer = input("[No] | Yes?\n") or ""
if "yes" == answer.lower():
    ModuleMaster.objects.all().delete()
    CaseMaster.objects.all().delete()

    with open('configuration/data/wahh.json') as wahh_file:
        methodology = json.load(wahh_file)
    for method in methodology['checklist']['Functionality']:
        module = ModuleMaster(name=method)
        module.save()
        for case in methodology['checklist']['Functionality'][method]['tests']:
            case = CaseMaster(name=case, module=module)
            case.save()
