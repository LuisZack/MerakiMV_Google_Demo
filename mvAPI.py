import requests
import meraki
from pprint import pprint

api_key="9aad4b4218a0fcddfb28a22a7c97a688baad529f"
dash=meraki.DashboardAPI(api_key)
response_org=dash.organizations.getOrganizations()

pprint(response_org)
