# Random Password Generator

This Python script generates a list of random passwords.

## Usage

1. Clone the repository:
git clone https://github.com/tejSSquare/password-generator
cd Random-Password-Generator

2. Run the script
python generate_passwords.py <no. of passwords> <length of password>

3.Customize the number of passwords and their length by editing the variables in the script:
num_passwords_to_generate = 5
desired_password_length = 12

Example Output
Generated 5 passwords of length 12:
aB3$9xY!pQ1@
kL0#rT2^uV4&
Zq8*Xy7!wR5%
mN6@bC1$hJ9*
pQ2%fD8^sL3&

4. Using as a Module
You can import the password generator function into another Python script:

Code : 

from generate_passwords import generate_password_list
# Generate 3 passwords of length 16
passwords = generate_password_list(3, 16)
print("Generated passwords:", passwords)


5. Requirements
Python 3.x
No external packages required

6.License
This project is open-source and available under the MIT License.


