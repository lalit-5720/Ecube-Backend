import requests
import json

API_KEY = "c2979f9e886757355ce342b90717042a"
API_SECRET = "cf83c308da224df2a47f851b4394b2cd"

payload = {
    "Messages": [
        {
            "From": {
                "Email": "gopallalit2000@gmail.com",
                "Name": "Ecube Website"
            },
            "To": [
                {
                    "Email": "gopallalit2000@gmail.com",
                    "Name": "Admin"
                }
            ],
            "Subject": "Test Email",
            "TextPart": "Testing Mailjet API."
        }
    ]
}

print("Sending email...")
try:
    response = requests.post(
        'https://api.mailjet.com/v3.1/send',
        auth=(API_KEY, API_SECRET),
        headers={'Content-Type': 'application/json'},
        data=json.dumps(payload)
    )
    print("Status Code:", response.status_code)
    try:
        print("Response:", response.json())
    except:
        print("Response Text:", response.text)
except Exception as e:
    print("Exception:", str(e))
