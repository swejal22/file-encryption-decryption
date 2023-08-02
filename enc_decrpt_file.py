from cryptography.fernet import Fernet
import logging


def generate_key():
    """Generates a new encryption key and returns it."""

    try:
        key = Fernet.generate_key()
    except Exception as e:
        logging.error(e)
        raise

    return key


def encrypt_file(input_file, output_file, key):
    """Encrypts a file using the given key and saves the encrypted file to the output file path."""

    try:
        with open(input_file, "rb") as file:
            data = file.read()
    except FileNotFoundError as e:
        logging.error(e)
        raise

    try:
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
    except Exception as e:
        logging.error(e)
        raise

    try:
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
    except FileNotFoundError as e:
        logging.error(e)
        raise


def decrypt_file(input_file, output_file, key):
    """Decrypts a file using the given key and saves the decrypted file to the output file path."""

    try:
        with open(input_file, "rb") as file:
            encrypted_data = file.read()
    except FileNotFoundError as e:
        logging.error(e)
        raise

    try:
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
    except Exception as e:
        logging.error(e)
        raise

    try:
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
    except FileNotFoundError as e:
        logging.error(e)
        raise


def main():
    """Prompts the user for the input file, output file, and encryption key, and then encrypts or decrypts the file accordingly."""

    logging.basicConfig(level=logging.INFO)

    choice = input(
        "Do you want to encrypt or decrypt the file? (Enter 'e' for encrypt, 'd' for decrypt): "
    )

    try:
        if choice == "e":
            key_option = input(
                "Do you want to use an existing key or generate a new one? (Enter 'e' for existing, 'n' for new): "
            )

            if key_option == "e":
                key_file = input("Enter the path of the key file: ")
                with open(key_file, "rb") as file:
                    key = file.read()
            elif key_option == "n":
                key = generate_key()
                print("New Key:")
                print(key)

        elif choice == "d":
            key = input("Enter the encryption key: ")
        else:
            raise ValueError("Invalid choice.")

        input_file = input("Enter the path of the input file: ")
        output_file = input("Enter the path of the output file: ")

        if choice == "e":
            encrypt_file(input_file, output_file, key)
        elif choice == "d":
            decrypt_file(input_file, output_file, key)
        else:
            raise ValueError("Invalid choice.")
    except Exception as e:
        logging.error(e)
        raise


if __name__ == "__main__":
    main()
