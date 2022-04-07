# rest_framework_simplejwt_wechat_sso

This is a modified version [`rest_framework_simplejwt`](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) library that includes WeChat SSO.
Reason that I made this is because I needed WeChat SSO functionality in my school project.

To use it, download and copy the entire project folder of `rest_framework_simplejwt_wechat_sso` to the root of your Django project.
After that, you will be able to use it like the normal `rest_framework_simplejwt`, but with a few additional settings added for WeChat SSO functionality:

```python
SIMPLE_JWT = {
  # other settings
  'WECHAT_APP_ID': 'Your WeChat App ID',
  'WECHAT_APP_SECRET': 'Your WeChat App Secret',
}
```

In `urls.py`
```python
from rest_framework_simplejwt_wechat_sso.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
  path('token', TokenObtainPairView.as_view()),
  path('token/refresh', TokenRefreshView.as_view()),
  path('token/verify', TokenVerifyView.as_view()),
]
```

Finally in your frontend client, POST your WeChat login code to the above URL, in the request body like the following, in JSON:
```json
{
  "code": "Your WeChat login code"
}
```
You should then be returned with `access_token` and `refresh_token`, if login is successful.
