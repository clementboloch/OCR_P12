import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .factories import ClientFactory, ContractFactory, EventFactory, UserFactory
from django.contrib.auth.models import Group
from django.conf import settings
from django.test.utils import setup_test_environment, teardown_test_environment

from .create_groups import setup_groups

def add_group(user, group_name):
    group = Group.objects.get(name=group_name)
    user.groups.add(group)

@pytest.mark.django_db
def setup_users_and_data():
    client = APIClient()

    # Create users
    management_user = UserFactory()
    add_group(management_user, 'Management')
    support_user = UserFactory()
    add_group(support_user, 'Support')
    commercial_user = UserFactory()
    add_group(commercial_user, 'Commercial')

    # Create test data
    test_client = ClientFactory(commercial_contact=commercial_user)
    test_contract = ContractFactory(client=test_client)
    test_event = EventFactory(contract=test_contract, support_contact=support_user)

    return client, management_user, support_user, commercial_user, test_client, test_contract, test_event

@pytest.mark.django_db
def test_client_list():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users = [management_user, support_user, commercial_user]
    for user in users:
        client.force_authenticate(user=user)
        url = reverse('client-list')
        response = client.get(url)
        assert response.status_code == 200

@pytest.mark.django_db
def test_client_create():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users = [management_user, support_user]
    for user in users:
        client.force_authenticate(user=user)
        url = reverse('client-create')
        response = client.post(url)
        assert response.status_code == 403

@pytest.mark.django_db
def test_client_modify():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users_status = [(management_user, 403), (support_user, 403), (commercial_user, 200)]
    for user, expected_status in users_status:
        client.force_authenticate(user=user)
        url = reverse('client-modify', args=[test_client.id])
        response = client.patch(url)
        assert response.status_code == expected_status

@pytest.mark.django_db
def test_contract_list():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users = [management_user, support_user, commercial_user]
    for user in users:
        client.force_authenticate(user=user)
        url = reverse('contract-list')
        response = client.get(url)
        assert response.status_code == 200

@pytest.mark.django_db
def test_contract_create():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users_status = [(support_user, 403), (commercial_user, 403)]
    for user, expected_status in users_status:
        client.force_authenticate(user=user)
        url = reverse('contract-create')
        response = client.post(url)
        assert response.status_code == expected_status

@pytest.mark.django_db
def test_contract_modify():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users_status = [(management_user, 200), (support_user, 403), (commercial_user, 200)]
    for user, expected_status in users_status:
        client.force_authenticate(user=user)
        url = reverse('contract-modify', args=[test_contract.id])
        response = client.patch(url)
        assert response.status_code == expected_status

@pytest.mark.django_db
def test_contract_add_event():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users_status = [(management_user, 403), (support_user, 403)]
    for user, expected_status in users_status:
        client.force_authenticate(user=user)
        url = reverse('contract-add-event', args=[test_contract.id])
        response = client.post(url)
        assert response.status_code == expected_status

@pytest.mark.django_db
def test_event_list():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users = [management_user, support_user, commercial_user]
    for user in users:
        client.force_authenticate(user=user)
        url = reverse('event-list')
        response = client.get(url)
        assert response.status_code == 200

@pytest.mark.django_db
def test_event_modify():
    client, management_user, support_user, commercial_user, test_client, test_contract, test_event = setup_users_and_data()

    users_status = [(management_user, 403), (support_user, 200), (commercial_user, 403)]
    for user, expected_status in users_status:
        client.force_authenticate(user=user)
        url = reverse('event-modify', args=[test_event.id])
        response = client.patch(url)
        assert response.status_code == expected_status
