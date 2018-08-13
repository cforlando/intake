from django.core.management.base import BaseCommand
from intake import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        # delete PII on:
        app_id = 8239
        form_submission = models.FormSubmission.find(app_id)


        # intake_formsubmission
        # intake_filledpdf
        # intake_statusnotification?
        # intake_application_note?
        # intake_applicant?
        # intake_visitor?
        # intake_applicationbundle?
        # intake_prebuiltpdfbundle?
        # intake_applicationcontactedlogentry?


        pass
