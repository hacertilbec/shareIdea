from rest_framework import serializers
from shareIdea.models import *


class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ('id', 'name', 'surname', 'department','statement','qualifications','email','password', 'my_projects', 'other_projects')
        read_only_fields=('id','name')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        
        project_owner = userProfileSerializer()
        participant = userProfileSerializer(many=True)

        fields = ("id", "title","description","language","starred_comment","created", "project_owner", "participant")

# We can also serialize querysets instead of model instances. To do so we simply add a many=True flag to the serializer arguments.
#serializer = SnippetSerializer(Snippet.objects.all(), many=True)
#serializer.data
# [OrderedDict([('id', 1), ('title', u''), ('code', u'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', u''), ('code', u'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', u''), ('code', u'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]