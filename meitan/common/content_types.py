from django.template.loader import render_to_string

class RenderCTMixin(object):
    template_name = None

    def get_template_data(self):
        return {
            'ctx': self
        }

    def render(self, **kwargs):
        try:
            return render_to_string(self.template_name, self.get_template_data())
        except Exception as e:
            print 'provide tempalte name'
            raise e
