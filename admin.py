from django.contrib import admin
from jpparse.models import Variable, VariableAdmin, CodeSegment, CodeSegmentAdmin, Method, MethodAdmin, Class, ClassAdmin, GlobalVariable, GlobalVariableAdmin

admin.site.register(Method, MethodAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Variable, VariableAdmin)
admin.site.register(GlobalVariable, GlobalVariableAdmin)
admin.site.register(CodeSegment, CodeSegmentAdmin)

