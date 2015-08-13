
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSMWeb.settings")
django.setup()

import zinnia.models

from zinnia.views.quick_entry import *
from CSMWeb.models import User

class Blog:
    def __init__(self):
        self.dump()

    def dump(self):
        self.dumpUsers()
        print "------------------"
        self.dumpEntries()

    def findUser(self, username):
        user = User.objects.filter(username=username).all()
        print user
        if not user:
            return None
        return user[0]

    def dumpUsers(self):
        print "Users:"
        for user in User.objects.all():
            print user, user.email
            #print "email: %s" % (user.email,)
            print

    def dumpEntries(self):
        print "Entries:"
        entries = zinnia.models.Entry.objects.all()
        for ent in entries:
            authors = ent.authors.all()
            print ent.pk, ent
            for author in authors:
                print "  ", author

    def addEntry(self, author, title, content):
        user = self.findUser(author)
        if not user:
            return "Can't find user"
        data = {'title': title,
                'slug': slugify(title),
                'status': PUBLISHED,
                'sites': [Site.objects.get_current().pk],
                'authors': [user.pk],
                'content_template': 'zinnia/_entry_detail.html',
                'detail_template': 'entry_detail.html',
                'creation_date': timezone.now(),
                'last_update': timezone.now(),
                'content': content,
                'tags': "dummy"}

        form = QuickEntryForm(data)
        if form.is_valid():
            form.instance.content = linebreaks(form.cleaned_data['content'])
            entry = form.save()
            print "Added and saved"
        else:
            print "problem with entry"


testContent = """
THis is the body
of the third multiline
dummy test article.
"""

def test():
    b = Blog()
    b.dump()
    b.addEntry("omohundro", "a test post", testContent)


if __name__ == '__main__':
    test()



