import pysftp
from urllib.parse import urlparse
import os


class Sftp:
    def __init__(self, hostname, username, password, port=2222):
        """Constructor Method"""
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        """Connects to SFTP server"""
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        try:
            self.connection = pysftp.Connection(
                host=self.hostname,
                username=self.username,
                password=self.password,
                port=self.port,
                cnopts=cnopts
            )
        except Exception as err:
            raise Exception(err)
        finally:
            print(f"Connected to {self.hostname} as {self.username}")


if __name__ == '__main__':
    sftp_url = os.environ.get("SFTPTOGO_URL")

    parsed_url = urlparse(sftp_url)

    sftp = Sftp(
        hostname=parsed_url.hostname,
        username=parsed_url.username,
        password=parsed_url.password,
    )

    if not sftp_url:
        print("First, please set environment variable SFTPTOGO_URL and try again.")
        exit(0)

    sftp.connect()