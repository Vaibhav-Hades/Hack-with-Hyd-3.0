import sys, os
sys.path.append('d:/Hack with Hyd 3.0/Backend')
from app.models import incident, incident_attempt, incident_resolution, remediation, verification_event, service
print('Imported models successfully')
print('Tables:', incident.Base.metadata.tables.keys())
