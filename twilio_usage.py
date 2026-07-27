"""Test file with Twilio API usage that has breaking changes."""
from twilio.rest import Client

account_sid = "AC123"
auth_token = "token123"
client = Client(account_sid, auth_token)

# Old Twilio API - calls.create with url parameter
def make_call_old(to_number):
    call = client.calls.create(
        to=to_number,
        from_="+15551234567",
        url="http://example.com/twiml"  # BREAKING: url renamed to twiml
    )
    return call

# Old Twilio API - messages.list (deprecated)
def list_messages_old():
    messages = client.messages.list(limit=20)  # BREAKING: list() deprecated, use stream()
    return messages

# Old Twilio API - recordings.list with date_created
def get_recordings_old():
    recordings = client.recordings.list(
        date_created="2024-01-01"  # BREAKING: date_created renamed to dateCreated
    )
    return recordings# test
# another test
