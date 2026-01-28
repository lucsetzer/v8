# app.py - FOUNDATION
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from apps.app1.routes import router as app1_router
import os

# Initialize
app = FastAPI(title="PromptSalchemy")

# Templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_dirs = [
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "apps", "app1", "templates"),
    os.path.join(BASE_DIR, "apps", "app2", "templates"),
    # Add all your app template directories
]
templates = Jinja2Templates(directory=template_dirs[0])

# Create routers for each section
public_router = APIRouter()
dashboard_router = APIRouter(prefix="/dashboard")

# 1. Public routes
@public_router.get("/")
async def frontpage(request: Request):
    return templates.TemplateResponse("frontpage.html", {"request": request})

@public_router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# 2. Dashboard routes
@dashboard_router.get("/")
async def dashboard_home(request: Request):
    return templates.TemplateResponse("dashboard/dashboard.html", {"request": request})

@dashboard_router.get("/settings")
async def dashboard_settings(request: Request):
    return templates.TemplateResponse("dashboard/settings.html", {"request": request})

# Register routers
app.include_router(public_router)
app.include_router(dashboard_router)

app.include_router(app1_router)

# Health check
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "connected_apps": ["app1"],
        "total_apps": 6
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
