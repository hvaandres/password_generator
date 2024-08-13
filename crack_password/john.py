import subprocess
import time

def run_john(hash_file, wordlist):
    # Prepare the John the Ripper command
    command = [
        'john',  # Command to run John the Ripper
        '--wordlist=' + wordlist,  # Wordlist path
        hash_file  # Path to the hash file
    ]

    # Run John the Ripper command
    subprocess.run(command)

    # Wait for John to finish
    time.sleep(5)

    # Check results
    result_command = ['john', '--show', hash_file]
    result = subprocess.run(result_command, capture_output=True, text=True)

    # Print output and errors
    print('John the Ripper output:\n', result.stdout)
    if result.stderr:
        print('John the Ripper errors:\n', result.stderr)

# Example usage
hash_file = 'linux-hashes.txt'
wordlist = 'rockyou.txt'

run_john(hash_file, wordlist)
