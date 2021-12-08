from api.utils import generate_random_json

def test_generate_random_json():
    data = generate_random_json()
    assert isinstance(generate_random_json(), dict)
    assert all(k in data for k in ('first_name', 'last_name', 'phone_number', 'address', 'country'))