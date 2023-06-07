from rest_framework import serializers

class Ankit(object):
    def __init__(self, name,hidden):
        self.name = name
        self.hidden = hidden

# create a serializer
class AnkitSerializer(serializers.Serializer):
    # intialize fields
    name = serializers.CharField()
    hidden = serializers.HiddenField(default = 1)