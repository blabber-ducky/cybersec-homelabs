import requests
import json
import sys

# ServiceDesk Plus API URL and API Key
sdplus_url = 'https://127.0.0.1:8777/api/v3/requests'
api_key = '720974F0-CEA9-4C7E-9173-4DA822D2D6FA'

# Function to create a ticket
def create_ticket(subject, description):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    data = {
        "request": {
            "subject": subject,
            "description": description,
            "priority": "High",
            "requester": "SIEM"
        }
    }
    
    response = requests.post(sdplus_url, headers=headers, data=json.dumps(data), verify=False)
    
    if response.status_code == 201:
        print('Ticket created successfully.')
    else:
        print('Failed to create ticket:', response.text)

if __name__ == '__main__':
    # Read Wazuh alert JSON data
    alert_data = json.loads(sys.stdin.read())
    
    alert_subject = alert_data.get('rule', {}).get('description', 'Wazuh Alert')
    alert_description = json.dumps(alert_data, indent=4)
    
    create_ticket(alert_subject, alert_description)
