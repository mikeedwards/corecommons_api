import urllib
from xml.dom.minidom import parse

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


from core.models import Language, GradeLevel, Standard, Component

class Command(BaseCommand):
    args = '<url>'
    help = 'Imports the learning standard items from a URL'

    def handle(self, *args, **options):
        document = parse(urllib.urlopen(args[0]))

        nodes = document.getElementsByTagName('LearningStandardItem')

        items = [{
            'grade_levels': [grade.childNodes[0].data for grade in node.getElementsByTagName('GradeLevel')],
            'code': [code.childNodes[0].data for code in node.getElementsByTagName('StatementCode') if len(code.childNodes) > 0],
            'statement': [code.childNodes[0].data for code in node.getElementsByTagName('Statement')][0],
            'ref_URI': [code.childNodes[0].data for code in node.getElementsByTagName('RefURI')][0],
            'document_ref_id': [code.childNodes[0].data for code in node.getElementsByTagName('LearningStandardDocumentRefId')][0],
            'parent_ref_id': [code.childNodes[0].data for code in node.getElementsByTagName('LearningStandardItemRefId') if len(code.childNodes) > 0], 
            'type': [code.childNodes[0].data for code in node.getElementsByTagName('description')][0], 
            'ref_id': node.getAttribute('RefID'), 
            'language': node.getAttribute('xml:lang')
        } for node in nodes]

        for item in items:
            if item['type'] == 'Standard':
                itemClass = Standard
            else:
                itemClass = Component
            itemObject = itemClass()
            if item['code']:
                itemObject.code = item['code'][0]
            itemObject.statement = item['statement']
            itemObject.ref_URI = item['ref_URI']
            itemObject.document_ref_id = item['document_ref_id']
            if item['parent_ref_id']:
                itemObject.parent_ref_id = item['parent_ref_id'][0]
                try:
                    itemObject.parent = Standard.objects.get(ref_id = itemObject.parent_ref_id)
                except ObjectDoesNotExist:
                    pass
            itemObject.ref_id = item['ref_id']
            itemObject.language = Language.objects.get_or_create(code=item['language'])[0]
            try:
                sid = transaction.savepoint()
                itemObject.save()
                for grade_level in item['grade_levels']:
                    itemObject.grade_levels.add(GradeLevel.objects.get_or_create(name=grade_level)[0])
                transaction.savepoint_commit(sid)
                self.stdout.write("%s imported\n" % (itemObject.code))
            except IntegrityError:
                transaction.savepoint_rollback(sid)



