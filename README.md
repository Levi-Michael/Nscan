
# Nscan

Nscan is a Python-based network scanning tool featuring a graphical user interface (GUI) and integrated Nmap scanning capabilities. It also offers the option to send SMS notifications using a Twilio account.

## Features

- **GUI Integration**: User-friendly interface for streamlined network scanning operations.
- **Nmap Integration**: Leverages Nmap for comprehensive network scanning.
- **SMS Notifications**: Option to send SMS alerts via Twilio upon scan completion or when specific events occur.

## Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Nmap**: Install Nmap for network scanning functionalities.
- **Twilio Account**: Required for SMS notification features.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Levi-Michael/Nscan.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Nscan
   ```

3. **Install Required Python Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Twilio (Optional)**:
   - Sign up for a Twilio account.
   - Obtain your `Account SID`, `Auth Token`, and `From` number.
   - Open the file where Twilio is configured (e.g., `twilio_config.py` or `ProjectMain.py`) and set the following values:

     ```python
     TWILIO_ACCOUNT_SID = "your_account_sid"
     TWILIO_AUTH_TOKEN = "your_auth_token"
     TWILIO_FROM = "+1234567890"  # Replace with your Twilio phone number
     ```

     Ensure these values are correctly set before running the application.

## Usage

1. **Launch the Application**:
   ```bash
   python ProjectMain.py
   ```

2. **Using the GUI**:
   - Enter the target IP address or range.
   - Select desired scanning options.
   - Initiate the scan and view results within the interface.

3. **SMS Notifications**:
   - Ensure Twilio is configured as described above.
   - Enable SMS notifications within the application settings to receive alerts.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Nmap](https://nmap.org/)
- [Twilio](https://www.twilio.com/)

For more information, visit the [Nscan GitHub repository](https://github.com/Levi-Michael/Nscan).
