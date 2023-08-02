# File Encryption/Decryption Program

This program allows users to encrypt and decrypt text files using the AES symmetric encryption algorithm. The encryption and decryption functionality is implemented using the **cryptography** library in Python.

## Installation

To run the program, follow these steps:

1. Make sure you have Python installed on your system (Python 3.6 or higher is recommended).

2. Clone or download this repository to your local machine.

3. Navigate to the project directory in the terminal or command prompt.

4. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

The program provides a command-line interface to interact with the encryption/decryption functionality. Follow the prompts to specify the input file, output file, and encryption key.

### Encryption

To encrypt a file, run the following command:

```bash
python enc_decrpt_file.py
```

You will be prompted to choose 'e' for encryption. Then, you can choose to use an existing key ('e') or generate a new one ('n'). If generating a new key, the new key will be displayed for your reference.

### Decryption

To decrypt a file, run the following command:

```bash
python enc_decrpt_file.py
```

You will be prompted to choose 'd' for decryption. Enter the encryption key that was used for encryption.

### Note

- The program will display appropriate error messages if the input file does not exist or if the encryption key is incorrect.

- For encryption, you can either use an existing key by providing the path to the key file or generate a new key.

- For decryption, you need to provide the encryption key that was used during encryption.

- The encrypted or decrypted file will be saved to the specified output file path.

- The program uses the AES encryption algorithm provided by the cryptography library to ensure secure and efficient encryption/decryption.

- If any errors occur during the process, they will be logged to the console for troubleshooting.

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests if you have any suggestions or improvements.