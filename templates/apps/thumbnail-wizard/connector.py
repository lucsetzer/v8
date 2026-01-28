# Example for Thumbnail Wizard: apps/thumbnail_wizard/connector.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import importlib

router = APIRouter(prefix="/thumbnail-wizard")

@router.get("/")
async def thumbnail_wizard_home(request: Request):
    """Main interface for Thumbnail Wizard"""
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    </head>
    <body>
        <main class="container">
            <h1>Thumbnail Wizard</h1>
            <p>AI-powered thumbnail evaluator</p>
            <div class="grid">
                <div>
                    <h3>Quick Actions</h3>
                    <a href="/thumbbnail-wizard/generate" role="button">Generate Thumbnails</a>
                    <a href="/thumbnail-wizard/analyze" role="button">Analyze Thumbnails</a>
                </div>
                <div>
                    <h3>About</h3>
                    <p>Analyzes thumbnail images using AI.</p>
                </div>
            </div>
            <a href="/dashboard">← Back to Dashboard</a>
        </main>
    </body>
    </html>
    """)

# Try to import actual app functionality
try:
    # Adjust import based on app's structure
    from thumbnail_wizard_app.app import generate_thumbnail, analyze_thumbnail
    
    @router.post("/generate")
    async def generate(request: Request):
        form = await request.form()
        topic = form.get("topic")
        hooks = generate_thumbnail(topic)
        return {"thumbnails": thumbnails}
        
except ImportError as e:
    print(f"⚠️ Thumbnail Wizard imports not ready: {e}")
    # Fallback routes that show "coming soon"
