from sqlmodel import Session, select
from models.users import User
from db.session import engine
from datetime import datetime

def seed_users() -> None:
    users_to_seed = [
            {
                "email": "admin@example.com",
                "fullname": "admin"
            },
            {
                "email": "dev@example.com",
                "fullname": "dev"
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
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )

            session.add(user)
            session.commit()
            session.refresh(user)

            print(f"Seeded user: {user.email} (id={user.id})")

if __name__ == "__main__":
    seed_users()
