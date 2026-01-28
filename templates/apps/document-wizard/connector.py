# Example for Document Wizard: apps/document_wizard/connector.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import importlib

router = APIRouter(prefix="/document-wizard")

@router.get("/")
async def document_wizard_home(request: Request):
    """Main interface for Document Wizard"""
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    </head>
    <body>
        <main class="container">
            <h1>Document Wizard</h1>
            <p>AI-powered document evaluator</p>
            <div class="grid">
                <div>
                    <h3>Quick Actions</h3>
                    <a href="/document-wizard/generate" role="button">Generate Documents</a>
                    <a href="/hook-wizard/analyze" role="button">Analyze Documents</a>
                </div>
                <div>
                    <h3>About</h3>
                    <p>Analyzes legal/medical documents using AI.</p>
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
    from document_wizard_app.app import generate_document, analyze_document
    
    @router.post("/generate")
    async def generate(request: Request):
        form = await request.form()
        topic = form.get("topic")
        hooks = generate_document(topic)
        return {"documents": documents}
        
except ImportError as e:
    print(f"⚠️ Document Wizard imports not ready: {e}")
    # Fallback routes that show "coming soon"
