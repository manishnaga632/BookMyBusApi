
from sqlalchemy.orm import Session
from api.database.models.contact import Contact
from api.database.schemas.contact import ContactCreate
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Create Contact and Conditionally Send Email
def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    # ✅ Email sending only if enabled in .env
    if os.getenv("ENABLE_EMAIL_NOTIFICATIONS", "False").lower() == "true":
        if os.getenv("EMAIL_HOST_USER") and os.getenv("EMAIL_HOST_PASSWORD"):
            send_email(db_contact)
        else:
            print("⚠️ Email credentials not set. Email not sent.")
    else:
        print("ℹ️ Email notifications disabled via .env")

    return db_contact

# ✅ Send Email Helper
def send_email(contact: Contact):
    email_address = os.getenv("EMAIL_HOST_USER")
    email_password = os.getenv("EMAIL_HOST_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = f"New Contact Message: {contact.subject}"
    msg["From"] = email_address
    msg["To"] = email_address
    msg.set_content(
        f"""
        👤 Name: {contact.name}
        📧 Email: {contact.email}
        📌 Subject: {contact.subject}
        📝 Message: {contact.message}
        """
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Email sending failed:", str(e))

# ✅ Other DB functions remain same...
def get_all_contacts(db: Session):
    return db.query(Contact).all()

def mark_as_seen(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        return None
    contact.seen = True
    db.commit()
    db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        return contact
    return None
