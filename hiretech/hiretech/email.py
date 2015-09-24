from django.conf import settings
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template import Context, Template
from django.utils.html import strip_tags
from django.template.loader import get_template
from premailer import Premailer
from drip.drips import DripMessage

class DefaultDripEmail(DripMessage):

    @property
    def customhtml(self):
        template_url = 'emails/base_email.html'
        html_template = get_template(template_url)
        context_dict = {
            'user': self.user,
            'body': self.body
        }
        email_data = Context(context_dict)
        htmlemail = Premailer(
            html_template.render(email_data),
            base_url=settings.EMAIL_BASE_URL,
            remove_classes=False,
            strip_important=False
        ).transform()
        self._customhtml = htmlemail
        return self._customhtml

    @property
    def message(self):
        if not self._message:
            if self.drip_base.from_email_name:
                from_ = "%s <%s>" % (self.drip_base.from_email_name, self.drip_base.from_email)
            else:
                from_ = self.drip_base.from_email

            self._message = EmailMultiAlternatives(
                self.subject, self.plain, from_, [self.user.email])

            # check if there are html tags in the rendered template
            if len(self.plain) != len(self.customhtml):
                self._message.attach_alternative(self.customhtml, 'text/html')
        return self._message
