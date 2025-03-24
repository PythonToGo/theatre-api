from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Theatre API",
        default_version='v1',
        description="Theatre Reservation API Docs",
        contact=openapi.Contact(email="pythontogoplease@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
def homepage(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Theatre API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c3e50, #3498db);
                color: white;
                text-align: center;
                padding: 80px;
                margin: 0;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: rgba(255, 255, 255, 0.05);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            a {
                display: inline-block;
                padding: 12px 24px;
                background-color: #ffffff;
                color: #2c3e50;
                text-decoration: none;
                font-weight: bold;
                border-radius: 8px;
                transition: background 0.3s;
            }
            a:hover {
                background-color: #f1f1f1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎭 Welcome to Theatre API</h1>
            <p>This is the backend API service for online theatre reservation system.</p>
            <a href="/api/docs/">View API Documentation</a>
        </div>
    </body>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('theatre.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', homepage),
]