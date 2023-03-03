import pysftp as sftp
import paramiko

if __name__ == '__main__':
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None

    try:
        with sftp.Connection(host='localhost', port=8000, username='root', password='', cnopts=cnopts) as sftp:
            print("Connected successfuly")
            sftp.listdir()
    except:
        print("error")