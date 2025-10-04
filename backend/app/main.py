import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(title="AITube Backend", version="0.1.0")

    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[frontend_url, "*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from .routers import channels, videos, summaries, monitor
    app.include_router(channels.router, prefix="/channels", tags=["channels"])
    app.include_router(videos.router, prefix="/videos", tags=["videos"])
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    app.include_router(monitor.router, prefix="/monitor", tags=["monitor"])

    @app.get("/health")
    def health():
        return {"status": "ok"}

    # Auto-create tables in dev (idempotent)
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass

    return app


app = create_app()


