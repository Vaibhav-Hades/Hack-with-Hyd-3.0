from fastapi import FastAPI

app = FastAPI(title="RESOLVE Backend API")

@app.get("/health")
async def health_check():
    """Simple health check endpoint used by deployment platforms."""
    return {"status": "ok"}

# Future endpoints will be defined in separate router modules according to API_CONTRACT.md.
