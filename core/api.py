from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from core.models import Standard, Component, GradeLevel, Language

class StandardResource(ModelResource):
    grade_levels = fields.ToManyField('core.api.GradeLevelResource', 'grade_levels', full=True)
    parent = fields.ToOneField('self', 'parent', full=True, null=True)

    class Meta:
        queryset = Standard.objects.all()
        resource_name = 'standard'
        detail_uri_name = 'ref_id'
        filtering = {
            "code": ALL,
            "statement": ALL,
            "grade_levels": ALL_WITH_RELATIONS
        }

class ComponentResource(ModelResource):
    grade_levels = fields.ToManyField('core.api.GradeLevelResource', 'grade_levels', full=True)
    parent = fields.ToOneField('core.api.StandardResource', 'parent', full=True, null=True)

    class Meta:
        queryset = Component.objects.all()
        resource_name = 'component'
        detail_uri_name = 'ref_id'
        filtering = {
            "code": ALL,
            "statement": ALL,
            "grade_levels": ALL_WITH_RELATIONS
        }

class GradeLevelResource(ModelResource):
    class Meta:
        fields = ['name']
        queryset = GradeLevel.objects.all()
        resource_name = 'grade_level'
        include_resource_uri = False
        filtering = {
            "name": ALL,
        }
