# Travello Website

The Travello website is a travel booking platform that allows users to browse and book travel packages for various destinations. This README provides essential information about the project.

## Installation Instructions

To set up the Travello website on your local machine, follow these steps:

1. Clone the project repository:
   ```
   git clone https://github.com/ajaygulia17/Travello.git
   ```

2. Install the required dependencies using the requirements.txt
   ```
   pip install -r requirements.txt
   ```

3. Set up the database by running the necessary migrations. Assuming you have Django installed:
   ```
   python manage.py migrate
   ```

4. Populate the database with sample data (optional):
   ```
   python manage.py loaddata sample_data.json
   ```

5. Start the development server: 
   ```
   python manage.py runserver
   ```

6. Access the Travello website in your browser at `http://localhost:8000`.

## Usage Instructions

Once you have the Travello website up and running, you can perform the following actions:

- Browse available travel packages: Navigate through the website to explore the various travel destinations and packages on offer.

- Book a travel package: Select a desired package and proceed to book it by providing the necessary details such as traveler names, dates, and payment information.

- Manage bookings: If you are an administrator or logged in as a user who has made bookings, you can view and manage your bookings, including canceling or modifying them if permitted.


Thank you for using our Travello website for booking travel packages!
