from django.views.decorators.csrf import csrf_exempt


from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.UserCtl import UserCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.CollegeCtl import CollegeCtl
from .ctl.CourseCtl import CourseCtl
from .ctl.SubjectCtl import SubjectCtl
from .ctl.FacultyCtl import FacultyCtl
from .ctl.MarksheetCtl import MarksheetCtl
from .ctl.MarksheetMeritListCtl import MarksheetMeritListCtl
from .ctl.StudentCtl import StudentCtl
from .ctl.TimeTableCtl import TimeTableCtl
from .ctl.ChangePasswordCtl import ChangePasswordCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl

@csrf_exempt
def action(request, page, action="get", id=0, pageNo=1):
    methodCall = page + "Ctl()." + action + "(request,{'id':id, 'pageNo':pageNo})"
    response = eval(methodCall)
    return response


# @csrf_exempt
# def action(request, page, action="get", id=0, pageNo=1):
#     try:
#         # Dynamically get controller class
#         ctl_class = globals()[page + "Ctl"]
#         ctl = ctl_class()
#
#         # Get method from controller
#         method = getattr(ctl, action)
#
#         # Call method
#         response = method(request, {"id": id, "pageNo": pageNo})
#
#         # 🔴 SAFETY: If response is None
#         if response is None:
#             return JsonResponse({
#                 "success": False,
#                 "result": {
#
#                 }
#             })
#
#         return response
#
#     except Exception as e:
#         return JsonResponse({
#             "success": False,
#             "result": {
#                 "message": str(e),
#                 "trace": traceback.format_exc()
#             }
#         })