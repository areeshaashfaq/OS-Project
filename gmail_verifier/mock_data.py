import random

def generate_mock_credentials(count=10):
    """
    Generates a list of mock credentials in the standard format 
    we will use for the real data.
    """
    # Hardcoded real credentials for testing
    return [
        {
            "email": "hafdivashfat@gmail.com",
            "password": "osproj1234",
            "totp_secret": None,
            "source": "manual_test"
        },
        {
            "email": "hafdivashfat@gmail.com",
            "password": "wrongpassword123",
            "totp_secret": None,
            "source": "manual_test_wrong_pass"
        }
    ]