import email
from email.parser import BytesParser, Parser
from email.policy import default
from email.message import EmailMessage


def read_em():
    with open("dict/em.txt", 'rb') as fp:
        content = BytesParser(policy=default).parse(fp,headersonly=False)
        print('To: {}'.format(content['to']))
        print('From: {}'.format(content['from']))
        print('Subject: {}'.format(content['subject']))
        print('Recipient username: {}'.format(content['to'].addresses[0].username))
        print('Sender name: {}'.format(content['from'].addresses[0].display_name))
        print('Body: {}'.format(content.get_body(preferencelist=('related', 'html', 'plain')).get_content()))
        # Got the hint on accessing the body without headers using get_body from https://stackoverflow.com/questions/21449085/python-3-4-email-contentmanager-how-to-use @Brandon Rhodes

if __name__ == '__main__':
    read_em()
