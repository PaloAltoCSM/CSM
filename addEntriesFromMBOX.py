
from BlogAPI import Blog
import MailAPI.MailParser as MP

HTML_TEMPLATE = """%(body)s"""

class Parser(MP.MailParser):
    def saveAsHTML(self, key, part, subject):
        self.saveToBlog(key, part, subject, "HTML")

    def saveAsTXT(self, key, part, subject):
        self.saveToBlog(key, part, subject, "TXT")

    def saveToBlog(self, key, part, subject, ttype):
        body = part.get_payload(decode=True)
        post = self.postsByKey[key]
        author_username = post['author_username']
        author_name = post['author_name']
        author_email = post['author_email']
        date = post['date']
        vals = {'body': body,
                'subject': subject}
        htmlStr = HTML_TEMPLATE % vals
        #htmlStr = "this is dummy body."
        #subject = "Dummy Subject"
        author = author_username
        self.blog.checkUser(author, author_name, author_email)
        print "author:", author, author_name
        print "title:", subject
        print "body:", htmlStr[:10]
        self.blog.addEntry(author, subject, htmlStr, date)

def run():
    blog = Blog()
    mboxDir = "C:/kimber/CSM"
    mp = Parser("CSM", mboxDir)
    mp.blog = blog
#    mp.scan(20)
    mp.scan()
#    mp.group()

if __name__ == '__main__':
    run()



