from django.test import TestCase
from .forms import ReservationsForm

class TestReservationForm(TestCase):
    """
    Tests for the ReservationForm
    """

    def test_valid_form_submission(self):
        """
        Test for valid form submission
        """
        form_data = {
            'email': 'test@gmail.com',  # Using a valid email domain
            'contact_number': '1234567890',
            'number_people': '2',
            'date': '2024-06-10',
            'time': '12:00',  # Using 24-hour format
        }
        reservation_form = ReservationsForm(data=form_data)
        if not reservation_form.is_valid():
            print(reservation_form.errors)  # Print the errors for debugging
        self.assertTrue(reservation_form.is_valid(), msg='Form submission failed for valid data')

    def test_missing_email(self):
        """
        Test for missing email field
        """
        form_data = {
            'contact_number': '1234567890',
            'number_people': '2',
            'date': '2024-06-10',
            'time': '12:00',
        }
        reservation_form = ReservationsForm(data=form_data)
        self.assertFalse(reservation_form.is_valid(), msg='Form submission succeeded with missing email')

    def test_missing_contact_number(self):
        """
        Test for missing contact number field
        """
        form_data = {
            'email': 'test@gmail.com',
            'number_people': '2',
            'date': '2024-06-10',
            'time': '12:00',
        }
        reservation_form = ReservationsForm(data=form_data)
        self.assertFalse(reservation_form.is_valid(), msg='Form submission succeeded with missing contact number')

    def test_missing_number_people(self):
        """
        Test for missing number of people field
        """
        form_data = {
            'email': 'test@gmail.com',
            'contact_number': '1234567890',
            'date': '2024-06-10',
            'time': '12:00',
        }
        reservation_form = ReservationsForm(data=form_data)
        self.assertFalse(reservation_form.is_valid(), msg='Form submission succeeded with missing number of people')

    def test_missing_date(self):
        """
        Test for missing date field
        """
        form_data = {
            'email': 'test@gmail.com',
            'contact_number': '1234567890',
            'number_people': '2',
            'time': '12:00',
        }
        reservation_form = ReservationsForm(data=form_data)
        self.assertFalse(reservation_form.is_valid(), msg='Form submission succeeded with missing date')

    def test_missing_time(self):
        """
        Test for missing time field
        """
        form_data = {
            'email': 'test@gmail.com',
            'contact_number': '1234567890',
            'number_people': '2',
            'date': '2024-06-10',
        }
        reservation_form = ReservationsForm(data=form_data)
        self.assertFalse(reservation_form.is_valid(), msg='Form submission succeeded with missing time')

    def test_invalid_email_format(self):
        """
        Test for invalid email format
        """
        form_data = {
            'email': 'test.test.test.org',
            'contact_number': '1234567890',
            'number_people': '2',
            'date': '2024-06-10',
            'time': '12:00',
        }
        reservation_form = ReservationsForm(data=form_data)
        self.assertFalse(reservation_form.is_valid(), msg='Form submission succeeded with invalid email format')
