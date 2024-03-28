Python Networking Tasks
This repository contains a set of Bash scripts and a Python script designed to interact with web servers using cURL and Python. Below is a brief overview of each script:

Task 0: cURL body size
File: 0-body_size.sh
This script takes a URL as input, sends a request to that URL using cURL, and displays the size of the body of the response in bytes.
Task 1: cURL to the end
File: 1-body.sh
When given a URL, this script sends a GET request and displays the body of the response only if the status code is 200.
Task 2: cURL Method
File: 2-delete.sh
This script sends a DELETE request to the URL provided as an argument and displays the body of the response.
Task 3: cURL only methods
File: 3-methods.sh
Given a URL, this script displays all HTTP methods accepted by the server.
Task 4: cURL headers
File: 4-header.sh
Sends a GET request to the provided URL with a custom header X-School-User-Id set to 98, and displays the body of the response.
Task 5: cURL POST parameters
File: 5-post_params.sh
This script sends a POST request to the given URL with specific parameters (email and subject) and displays the body of the response.
Task 6: Find a peak
Files: 6-peak.py, 6-peak.txt
Contains a Python function find_peak that finds a peak in a list of unsorted integers. The script 6-main.py tests this function with various inputs.
Task 7: Only status code
File: 100-status_code.sh
Sends a request to a URL provided as an argument and displays only the status code of the response.
Task 8: cURL a JSON file
File: 101-post_json.sh
Sends a JSON POST request to a URL with the contents of a file passed as the second argument. It validates if the file contains a valid JSON and displays the response accordingly.
Task 9: Catch me if you can!
File: 102-catch_me.sh
Makes a request to a specific URL that triggers the server to respond with a message containing "You got me!".
Each script is thoroughly tested and ready for use.

For more details and usage instructions, refer to the individual files in the repository.

GitHub Repository: alx-higher_level_programming
Directory: 0x10-python-network_0

For any inquiries or assistance, feel free to reach out! 🚀
