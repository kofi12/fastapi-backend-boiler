from sqlmodel import Session, select
from app.db.session import engine
from app.models.users import User
from datetime import datetime, timezone

def seed_users() -> None:
    users_to_seed = [
            {
                "email": "admin@example.com",
                "full_name": "admin"
            },
            {
                "email": "dev@example.com",
                "full_name": "dev"
            }
        ]

    with Session(engine) as session:
        for data in users_to_seed:
            existing = session.exec(
                select(User).where(User.email == data["email"])
            ).first()

            if existing:
                print(f"User already exists: {existing.email} (id={existing.id})")
                continue

            user = User(
                email=data["email"],
                full_name=data["full_name"],
                is_active=True,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )

            session.add(user)
            session.commit()
            session.refresh(user)

            print(f"Seeded user: {user.email} (id={user.id})")

if __name__ == "__main__":
    seed_users()
