#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Message

fake = Faker()

usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    with app.app_context():
        db.session.query(Message).delete()
        
        messages = [
            Message(body=fake.sentence(), username=rc(usernames))
            for _ in range(20)
        ]

        db.session.add_all(messages)
        db.session.commit()        
        print("Database seeded successfully!")

if __name__ == '__main__':
    make_messages()
