from faker import Faker

fakegen = Faker()

def generate_random_json():
    """Generate a json with random values using Faker."""
    return {
        'first_name': fakegen.first_name(),
        'last_name': fakegen.last_name(),
        'phone_number': fakegen.phone_number(),
        'address': fakegen.address(),
        'country': fakegen.country()
    }