# Example for Hook Wizard: apps/hook_wizard/connector.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import importlib

router = APIRouter(prefix="/hook-wizard")

@router.get("/")
async def hook_wizard_home(request: Request):
    """Main interface for Hook Wizard"""
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    </head>
    <body>
        <main class="container">
            <h1>🎣 Hook Wizard</h1>
            <p>AI-powered viral hook generator</p>
            <div class="grid">
                <div>
                    <h3>Quick Actions</h3>
                    <a href="/hook-wizard/generate" role="button">Generate Hooks</a>
                    <a href="/hook-wizard/analyze" role="button">Analyze Hooks</a>
                </div>
                <div>
                    <h3>About</h3>
                    <p>Creates engaging social media hooks using AI.</p>
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
    from hook_wizard_app.app import generate_hook, analyze_hook
    
    @router.post("/generate")
    async def generate(request: Request):
        form = await request.form()
        topic = form.get("topic")
        hooks = generate_hook(topic)
        return {"hooks": hooks}
        
except ImportError as e:
    print(f"⚠️ Hook Wizard imports not ready: {e}")
    # Fallback routes that show "coming soon"
