from unittest.mock import patch, mock_open
import pytest
from data.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('data.app.open', new_callable=mock_open, read_data="name,hire_date,department,birthday\nJohn Doe,2022-04-15,Engineering,1985-05-01\n")
def test_birthdays_endpoint_success(mock_file, client):
    """Test successful GET request to the birthdays endpoint."""
    response = client.get('/birthdays', query_string={'month': 'May', 'department': 'Engineering'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'total' in data
    assert isinstance(data['total'], int)
    assert data['total'] == 1  # Assuming the mock data contains one matching record
    assert 'employees' in data
    assert isinstance(data['employees'], list)
    # Ensure the first employee in the list matches the expected values from your mock data
    assert data['employees'][0]['name'] == 'John Doe'


@patch('data.app.open', new_callable=mock_open, read_data="name,hire_date,department,birthday\nLinda Smith,2017-05-17,Engineering,1986-07-22\n")
def test_anniversaries_endpoint_success(mock_file, client):
    """Test successful GET request to the anniversaries endpoint."""
    # Using 'May' and 'Engineering' as example parameters
    response = client.get('/anniversaries', query_string={'month': 'May', 'department': 'Engineering'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'total' in data
    assert isinstance(data['total'], int)
    assert 'employees' in data
    assert isinstance(data['employees'], list)
    # Ensure the first employee in the list matches the expected values from your mock data
    assert data['employees'][0]['name'] == 'Linda Smith'


def test_birthdays_endpoint_invalid_month(client):
    """Test the birthdays endpoint with an invalid month parameter."""
    response = client.get('/birthdays', query_string={'month': 'InvalidMonth', 'department': 'Engineering'})
    assert response.status_code == 400


@patch('data.app.open', new_callable=mock_open, read_data="name,hire_date,department,birthday\nJohn Doe,2022-04-15,Engineering,1985-05-01\n")
def test_birthdays_endpoint_missing_parameter(mock_file, client):
    """Test the birthdays endpoint missing a required parameter."""
    response = client.get('/birthdays', query_string={'month': 'May'})  # Missing 'department'
    assert response.status_code == 400  # Assume handling for missing parameters


def test_anniversaries_endpoint_invalid_month(client):
    """Test the anniversaries endpoint with an invalid month parameter."""
    response = client.get('/anniversaries', query_string={'month': 'InvalidMonth', 'department': 'Engineering'})
    assert response.status_code == 400


@patch('data.app.open', new_callable=mock_open, read_data="name,hire_date,department,birthday\nJohn Doe,2022-04-15,Engineering,1985-05-01\n")
def test_anniversaries_endpoint_missing_parameter(mock_file, client):
    """Test the anniversaries endpoint missing a required parameter."""
    response = client.get('/anniversaries', query_string={'month': 'May'})  # Missing 'department'
    assert response.status_code == 400  # Assume handling for missing parameters


@patch('data.app.open', new_callable=mock_open, read_data="name,hire_date,department,birthday\nJohn Doe,2022-04-15,Engineering,1985-05-01\nLinda Smith,2017-05-17,Engineering,1986-07-22\nCorruptedData")
def test_corrupted_csv_file(mock_file, client):
    """Test how the application handles a corrupted CSV file."""
    # Test the birthdays endpoint
    response = client.get('/birthdays', query_string={'month': 'May', 'department': 'Engineering'})
    assert response.status_code == 500  # Assume the application returns a 500 status code for server errors
    # Test the anniversaries endpoint
    response = client.get('/anniversaries', query_string={'month': 'May', 'department': 'Engineering'})
    assert response.status_code == 500  # Assume the application returns a 500 status code for server errors