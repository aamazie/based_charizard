# based_charizard
in the post-apocalyptic world, created by the ratata software, the war beneath kernel needed a weapon...

Malware Scanner in Python for Buffer Overflow and RAT Detection and Prevention

python malware scanner.

dependency:

pip install psutil

Implementing the Permissions Setup:

To set up permissions statically:

Linux:

Run the scanner with sudo:

sudo ./based_charizard.py

Or set the binary with the setuid bit (not generally recommended for security reasons):

sudo chown root:root based_charizard.py

sudo chmod u+s based_charizard.py

Windows:

Run the program as Administrator.

Use a task scheduler to run the program with elevated privileges.

