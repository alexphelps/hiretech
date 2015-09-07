from haystack import indexes

from .models import Job

class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    job_status = indexes.CharField()
    tags = indexes.MultiValueField()

    def get_model(self):
        return Job

    def prepare_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
