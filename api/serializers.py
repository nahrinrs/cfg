from config.models import Config
from rest_framework import serializers

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('appId', 'version', 'build', 'platform', 'islocked', 'content')
        read_only_fields = ('islocked', 'content')
