from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Photography Blog API",
        default_version="0.0.1",
        description="API for various things in the blog",
        contact=openapi.Contact(email="maxgelmadin@gmail.com"),
        license=openapi.License(name="Max Gelmadin"),
    ),
    public=False,
)
