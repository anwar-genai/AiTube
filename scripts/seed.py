import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

from app.db import SessionLocal
from app import models


def main():
    db = SessionLocal()
    try:
        user = models.User(email="demo@example.com")
        db.add(user)
        db.commit()
        db.refresh(user)
        print("Seeded user", user.id)
    finally:
        db.close()


if __name__ == "__main__":
    main()


