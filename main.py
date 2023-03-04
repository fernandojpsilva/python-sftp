import pysftp as sftp
import paramiko

if __name__ == '__main__':
    cnopts = sftp.CnOpts(knownhosts='resources/known_hosts')
    #cnopts.hostkeys = None

    try:
        with sftp.Connection(host='test.rebex.net', port=22, username='demo', password='password', cnopts=cnopts) as sftp:
            print("Connected successfuly")
            print(sftp.listdir())
            sftp.get('readme.txt', preserve_mtime=True)
    except:
        print("error")