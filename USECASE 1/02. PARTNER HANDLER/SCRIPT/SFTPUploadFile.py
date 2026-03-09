import paramiko
import os


def main(local_path: str, remote_path: str, username: str, password: str, host: str, port: int = 22) -> bool:
    try:
        # Check if the local file exists
        if not os.path.isfile(local_path):
            print(f"Error: Local file {local_path} does not exist")
            return False

        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SFTP server
        ssh_client.connect(hostname=host, port=port,
                           username=username, password=password)

        # Open SFTP session
        sftp_client = ssh_client.open_sftp()

        # Make sure the remote directory exists
        remote_dir = os.path.dirname(remote_path)
        try:
            sftp_client.stat(remote_dir)
        except FileNotFoundError:
            # Create the directory structure recursively
            dir_parts = remote_dir.split('/')
            current_dir = ""
            for part in dir_parts:
                if not part:
                    continue
                current_dir += "/" + part
                try:
                    sftp_client.stat(current_dir)
                except FileNotFoundError:
                    sftp_client.mkdir(current_dir)

        # Upload the file
        sftp_client.put(local_path, remote_path)

        # Close connections
        sftp_client.close()
        ssh_client.close()

        print(f"File uploaded successfully to {remote_path}")
        return True

    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return False
